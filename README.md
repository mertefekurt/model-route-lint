<img src="assets/readme-cover.svg" alt="Model Route Lint cover" width="100%" />

# Model Route Lint

Lint model routing configs for missing fallbacks, budgets, and safety tiers.

![stack](https://img.shields.io/badge/stack-Python-be185d?style=flat-square) ![python](https://img.shields.io/badge/python-3.11-4b5563?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-2563eb?style=flat-square) ![ci](https://img.shields.io/badge/ci-GitHub%20Actions-16a34a?style=flat-square)

## Workflow

1. Collect the review notes or exported records.
2. Run `model-route-lint` against the file.
3. Read the findings in Markdown, or switch to JSON for automation.
4. Fail CI only at the severity level you care about.

## Checks

| Rule | Severity | What it catches |
| --- | --- | --- |
| `missing-fallback` | high | model route has no fallback |
| `missing-budget` | medium | route budget control is missing |
| `missing-safety-tier` | low | safety tier is not declared |

## Command line

```bash
python -m pip install -e ".[dev]"
model-route-lint examples/sample.txt
model-route-lint examples/sample.txt --json --fail-on medium
```

## Sample risky input

```text
examples/sample.txt
```

## Project shape

```text
.github/        CI workflow
examples/       sample inputs
src/            package source
tests/          test coverage
.gitignore      project file
pyproject.toml  package metadata
```
