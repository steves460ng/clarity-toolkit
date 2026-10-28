# Clarity Toolkit

An unofficial, MIT-licensed ChatGPT plugin adapted from five productivity skills in [mattpocock/skills](https://github.com/mattpocock/skills).

Internal instructions, templates, metadata, and development scripts are English. Questions and deliverables follow the user's language, including explicit requests for another output language.

## Included workflows

| Skill | Purpose |
| --- | --- |
| `grill-me` | Start an interview to clarify requirements or stress-test a plan. |
| `grilling` | Work through decisions in dependency order, usually one to three questions at a time. |
| `to-questionnaire` | Draft questions for someone who holds missing information. |
| `wait-what` | Re-explain a confusing message with the missing context. |
| `handoff` | Prepare a grounded handoff for another person or session. |

No MCP server or runtime scripts are required. Four entry skills require explicit user intent; the shared `grilling` procedure preserves upstream implicit invocation. The host determines how users select and invoke skills. The plugin does not provide durable memory, send questionnaires, or implement interview plans. File downloads depend on host tools; Markdown is the fallback.

## Build and verify

Requires Python 3.9 or newer and PyYAML. Run from the repository root:

```sh
python -m pip install -r requirements.txt
python build_source.py
python scripts/validate_package.py clarity-toolkit --archive dist/clarity-toolkit-0.1.1.zip
python scripts/test_validator.py
python scripts/check_simulation_records.py
python scripts/test_review_regressions.py
```

The installable package is `dist/clarity-toolkit-0.1.1.zip`. The source package lives in `clarity-toolkit/`; this repository root also contains development tools. Importing or installing a custom plugin requires a supporting ChatGPT account and host workflow. Publishing this repository alone does not install the plugin or submit it to a public plugin directory.

The build creates a fresh candidate, validates its exact file inventory, and replaces the previous output, with rollback on promotion failure. Stale support files cannot survive a rebuild. The validator checks this package's required fields and strict SemVer; it is not a complete external JSON Schema validator.

## Tests and evidence

- Ten malformed-package cases exercise validation failures.
- Eight regression tests cover stale evidence, missing baselines, source additions/deletions, optimized Python, clean rebuilds, failed builds, reproducible ZIPs, and valid/invalid versions.
- `tests/self_simulations.json` contains thirteen author-performed walkthroughs with example outputs and self-review notes. The English and Korean examples are intentionally outside the shipped plugin.
- Walkthrough evidence is bound to the reviewed skill, template, and policy hashes. A changed source requires a new semantic review and explicit baseline update. Running the checker never refreshes the baseline automatically.
- These walkthroughs are not independent model executions. Installed-host routing, skill loading, file delivery, and repeated-run quality remain unverified. A passing record check does not establish general model compliance.

Generated local reports are written to `reports/` and excluded from version control. `upstream/snapshot.json` preserves the pinned original source and blob hashes. Version 0.1.1 improves the development and verification pipeline; user-facing skill behavior is unchanged from 0.1.0.

## License and attribution

MIT licensed. Original copyright: Copyright (c) 2026 Matt Pocock. The original copyright and permission notice are preserved in `LICENSE` and in the plugin package. See `THIRD_PARTY_NOTICES.md` for the source commit and adaptation scope.

This project is an unofficial adaptation and is not affiliated with or endorsed by Matt Pocock.
