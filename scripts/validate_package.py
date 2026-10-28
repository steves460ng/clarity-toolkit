"""Validate this private skills-only package; not a full JSON Schema validator."""
import argparse
import hashlib
import json
import re
import stat
import zipfile
from pathlib import Path
import yaml

EXPECTED = {'grill-me', 'grilling', 'to-questionnaire', 'wait-what', 'handoff'}
SEMVER = re.compile(r'(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)(?:-((?:0|[1-9][0-9]*|[0-9]*[A-Za-z-][0-9A-Za-z-]*)(?:\.(?:0|[1-9][0-9]*|[0-9]*[A-Za-z-][0-9A-Za-z-]*))*))?(?:\+([0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*))?')

def validate(root):
    root = Path(root).resolve()
    checks = []
    def check(condition, message):
        if not condition:
            raise ValueError(message)
        checks.append(message)
    manifest = json.loads((root / 'plugin.json').read_text(encoding='utf-8'))
    check(manifest.get('$schema') == 'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json', 'Portable schema declaration')
    name = manifest.get('name', '')
    check(bool(re.fullmatch(r'[a-z0-9](?:[a-z0-9.-]{0,62}[a-z0-9])?', name)) and '--' not in name and '..' not in name and root.name == name, 'Valid package name and root directory')
    check(isinstance(manifest.get('version'), str) and bool(SEMVER.fullmatch(manifest['version'])), 'Strict SemVer release version')
    check(not {'skills', 'mcpServers', 'apps', 'interface'}.intersection(manifest), 'No legacy top-level declarations')
    interface = manifest['extensions']['com.openai']['interface']
    check(all(isinstance(interface.get(k), str) and interface[k].strip() for k in ['displayName', 'shortDescription', 'longDescription', 'developerName']), 'Nonblank presentation fields')
    check(len(interface['shortDescription']) <= 30, 'Subtitle length at most 30')
    check(isinstance(interface.get('capabilities'), list) and all(isinstance(v, str) and v.strip() for v in interface['capabilities']), 'Capability array')
    check(isinstance(interface['defaultPrompt'], list) and 1 <= len(interface['defaultPrompt']) <= 3 and all(isinstance(v, str) and v.strip() for v in interface['defaultPrompt']), 'Default prompts')
    files = sorted(p for p in root.rglob('*') if p.is_file())
    expected_files = {'plugin.json', 'LICENSE', 'README.md', 'THIRD_PARTY_NOTICES.md'}
    expected_files.update(f'skills/{name}/{file}' for name in EXPECTED for file in ['SKILL.md', 'agents/openai.yaml'])
    expected_files.update({'skills/handoff/references/handoff-template.md', 'skills/to-questionnaire/references/questionnaire-template.md'})
    check({p.relative_to(root).as_posix() for p in files} == expected_files, 'Exact source inventory; no stale or unrelated files')
    check(not any(p.is_symlink() for p in root.rglob('*')), 'No symlinks')
    check(all(p.name == 'LICENSE' or p.suffix in {'.md', '.json', '.yaml'} for p in files), 'Only intended text components; no runtime scripts or credentials')
    check(not any(p.name.startswith('.') or any(part.startswith('.') for part in p.relative_to(root).parts) for p in files), 'No hidden files')
    for p in files:
        content = p.read_text(encoding='utf-8')
        check(content.isascii(), f'English ASCII source: {p.relative_to(root)}')
        for link in re.findall(r'\]\(([^)]+)\)', content):
            if '://' in link or link.startswith('#'):
                continue
            target = (p.parent / link.split('#')[0]).resolve()
            check(target.is_relative_to(root) and target.is_file(), f'Contained reference: {p.relative_to(root)} -> {link}')
    skill_files = list((root / 'skills').glob('*/SKILL.md'))
    check({p.parent.name for p in skill_files} == EXPECTED and len(skill_files) == 5, 'Exactly five portable skills')
    check(len(list((root / 'skills').rglob('SKILL.md'))) == 5, 'No hidden or nested skills')
    for p in skill_files:
        content = p.read_text()
        check(len(p.read_bytes()) <= 1024 * 1024 and content.startswith('---\n'), f'Skill size and frontmatter: {p.parent.name}')
        meta = yaml.safe_load(content.split('---', 2)[1])
        check(meta['name'] == p.parent.name and isinstance(meta.get('description'), str) and bool(meta['description'].strip()), f'Skill identity: {p.parent.name}')
        agent = yaml.safe_load((p.parent / 'agents/openai.yaml').read_text())
        check(set(agent['policy']) == {'allow_implicit_invocation'} and type(agent['policy']['allow_implicit_invocation']) is bool and agent['policy']['allow_implicit_invocation'] == (p.parent.name == 'grilling'), f'Invocation policy: {p.parent.name}')
        check(all(isinstance(agent['interface'].get(k), str) and agent['interface'][k].strip() for k in ['display_name', 'short_description']), f'Agent metadata: {p.parent.name}')
    license_text = (root / 'LICENSE').read_text()
    check('Copyright (c) 2026 Matt Pocock' in license_text and 'Permission is hereby granted' in license_text and 'THE SOFTWARE IS PROVIDED' in license_text, 'Original MIT copyright, permission and warranty notice')
    check('59db609eb1e18aaf59b63284d0e52255aff0c63c' in (root / 'THIRD_PARTY_NOTICES.md').read_text(), 'Pinned provenance')
    return checks

def archive(root, output):
    root, output = Path(root).resolve(), Path(output).resolve()
    if output.is_relative_to(root):
        raise ValueError('Archive must be outside the package')
    validate(root)
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as z:
        for p in sorted(root.rglob('*')):
            if p.is_file():
                entry = zipfile.ZipInfo(p.relative_to(root.parent).as_posix(), (2026, 10, 29, 0, 0, 0))
                entry.compress_type = zipfile.ZIP_DEFLATED
                entry.external_attr = (stat.S_IFREG | 0o644) << 16
                z.writestr(entry, p.read_bytes())
    with zipfile.ZipFile(output) as z:
        expected = {p.relative_to(root.parent).as_posix(): p.read_bytes() for p in root.rglob('*') if p.is_file()}
        if len(z.namelist()) != len(expected) or set(z.namelist()) != set(expected):
            raise ValueError('Archive entries do not match source')
        for name, data in expected.items():
            if z.read(name) != data:
                raise ValueError('Archive content mismatch: ' + name)
    return {'path': str(output), 'files': len(expected), 'sha256': hashlib.sha256(output.read_bytes()).hexdigest()}

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('root', type=Path)
    parser.add_argument('--archive', type=Path)
    args = parser.parse_args()
    checks = validate(args.root)
    result = {'status': 'passed', 'checks': len(checks), 'details': checks}
    if args.archive:
        result['archive'] = archive(args.root, args.archive)
    print(json.dumps(result, indent=2))
