"""Exercise packaging failures; these tests do not evaluate model behavior."""
import json
import shutil
import tempfile
from pathlib import Path
from validate_package import validate

SOURCE = Path(__file__).resolve().parents[1] / 'clarity-toolkit'

def mutate(case, root):
    manifest_path = root / 'plugin.json'
    manifest = json.loads(manifest_path.read_text())
    if case == 'missing_schema':
        del manifest['$schema']
    elif case == 'long_subtitle':
        manifest['extensions']['com.openai']['interface']['shortDescription'] = 'x' * 31
    elif case == 'wrong_capabilities_type':
        manifest['extensions']['com.openai']['interface']['capabilities'] = 'Interactive'
    elif case == 'broken_reference':
        (root / 'skills/grilling/SKILL.md').write_text((root / 'skills/grilling/SKILL.md').read_text() + '\n[Missing](missing.md)\n')
    elif case == 'escaping_reference':
        (root / 'skills/grilling/SKILL.md').write_text((root / 'skills/grilling/SKILL.md').read_text() + '\n[Outside](../../../outside.md)\n')
    elif case == 'string_policy':
        (root / 'skills/grill-me/agents/openai.yaml').write_text('interface:\n  display_name: Grill Me\n  short_description: Interview\npolicy:\n  allow_implicit_invocation: "false"\n')
    elif case == 'missing_skill':
        shutil.rmtree(root / 'skills/handoff')
    elif case == 'missing_license_notice':
        (root / 'LICENSE').write_text('MIT\n')
    elif case == 'non_english_source':
        (root / 'README.md').write_text('Non-English sample: \uac00\n')
    elif case == 'unexpected_runtime_script':
        (root / 'runtime.sh').write_text('echo unexpected\n')
    manifest_path.write_text(json.dumps(manifest))

validate(SOURCE)
results = []
for case in ['missing_schema', 'long_subtitle', 'wrong_capabilities_type', 'broken_reference', 'escaping_reference', 'string_policy', 'missing_skill', 'missing_license_notice', 'non_english_source', 'unexpected_runtime_script']:
    with tempfile.TemporaryDirectory() as temporary:
        root = Path(temporary) / SOURCE.name
        shutil.copytree(SOURCE, root)
        mutate(case, root)
        try:
            validate(root)
        except (ValueError, KeyError, FileNotFoundError) as error:
            results.append({'case': case, 'result': 'rejected_as_expected', 'reason': str(error)})
        else:
            raise AssertionError('Invalid package accepted: ' + case)
print(json.dumps({'status': 'passed', 'negative_cases': len(results), 'results': results}, indent=2))
