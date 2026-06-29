# model-route-lint

`model-route-lint` is a small local CLI that lint model routing configs for missing fallbacks, budgets, and safety tiers.

## Why it is useful

LLM routing tables become production control planes. This CLI checks route configs for brittle fallback and governance gaps.

## Key features

- reads text, JSON, JSONL, or CSV inputs
- returns Markdown or JSON reports
- supports severity-based CI exit codes
- keeps all checks deterministic and offline
- includes focused rules for this project:
- `missing-fallback`: model route has no fallback
- `missing-budget`: route budget control is missing
- `missing-safety-tier`: safety tier is not declared

## Installation

```bash
python -m pip install -e ".[dev]"
```

## Usage

```bash
model-route-lint examples/sample.txt
model-route-lint examples/sample.txt --json
model-route-lint path/to/input.txt --fail-on medium --out report.md
python -m model_route_lint --help
```

Example input:

```text
route support_agent model gpt-x fallback: none max_cost: missing safety_tier: none
```

## CLI options

```text
model-route-lint INPUT [--format auto|text|jsonl|csv|json] [--json]
             [--fail-on low|medium|high] [--out PATH]
```

`INPUT` is any model routing YAML, JSON, or notes. The tool exits with code `2` when findings meet the selected
threshold, which makes it easy to use in GitHub Actions or release checks.

## Workflow

```mermaid
flowchart LR
    A[input file] --> B[format reader]
    B --> C[project-specific rules]
    C --> D[risk score]
    D --> E[Markdown or JSON report]
```

## Tests

```bash
ruff check .
pytest
python -m model_route_lint --help
```

## License

MIT
