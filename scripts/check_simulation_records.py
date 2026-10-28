"""Check walkthrough evidence against the exact reviewed skill sources."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
(ROOT / 'reports').mkdir(parents=True, exist_ok=True)
(ROOT / 'reports/simulation-record-check.json').write_text(json.dumps({'record_integrity': 'failed', 'error': 'Validation did not complete'}, indent=2), encoding='utf-8')
data = json.loads((ROOT / 'tests/self_simulations.json').read_text())
cases = data['cases']
def require(condition, message):
    if not condition:
        raise ValueError(message)

hashes = {p.relative_to(ROOT / 'clarity-toolkit').as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((ROOT / 'clarity-toolkit/skills').rglob('*')) if p.is_file()}
expected = data.get('reviewed_behavior_sha256')
changed = sorted(k for k in hashes.keys() | (expected or {}).keys() if hashes.get(k) != (expected or {}).get(k))
if not expected or changed:
    message = 'Stale simulation evidence; review required: ' + ', '.join(changed)
    (ROOT / 'reports/simulation-record-check.json').write_text(json.dumps({'record_integrity': 'failed', 'evidence_matches_current_behavior': False, 'error': message}, indent=2) + '\n', encoding='utf-8')
    raise SystemExit(message)
require(len(cases) == 13 and len({c['id'] for c in cases}) == 13, 'Expected thirteen unique cases')
for case in cases:
    require(case['context'] and case['focus'] and case['turns'], 'Incomplete scenario')
    require((ROOT / 'clarity-toolkit/skills' / case['skill'] / 'SKILL.md').is_file(), 'Unknown skill')
    require(all(t['user'] and t['assistant'] for t in case['turns']), 'Incomplete turns')
    require(case['review']['passed'] is True and case['review']['reason'], 'Review required')
outputs = {c['id']: '\n'.join(t['assistant'] for t in c['turns']) for c in cases}
require('SYNTHETIC_DEMO_TOKEN' not in outputs['S10'] and '[REDACTED]' in outputs['S10'], 'Redaction example failed')
require('?' not in outputs['S04'] and '\uff1f' not in outputs['S04'], 'Stop example failed')
require(outputs['S07'].isascii(), 'English example failed')
require('http' not in outputs['S11'], 'No-file example failed')
result = {
    'record_integrity': 'passed',
    'evidence_matches_current_behavior': True,
    'recorded_cases': len(cases),
    'self_review_passed': sum(c['review']['passed'] for c in cases),
    'method': data['method'],
    'limitations': ['No independent model inference was run.', 'Static assertions check only the recorded examples.', 'No installed-plugin invocation, skill routing, or download-capable host was tested.', 'English-only source is checked conservatively as ASCII; this is not a natural-language quality proof.'],
    'reviewed_behavior_sha256': expected
}
(ROOT / 'reports/simulation-record-check.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
print(json.dumps(result, indent=2))
