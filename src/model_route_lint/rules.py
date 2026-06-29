from __future__ import annotations

from model_route_lint.models import Rule

PROJECT_NAME = 'model-route-lint'
DESCRIPTION = 'Lint model routing configs for missing fallbacks, budgets, and safety tiers.'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "service", "dataset", "route", "metric", "field", "path")
HIGH_SAMPLE = (
                  'route support_agent model gpt-x fallback: none max_cost: missing safety_'
                  'tier: none'
              )
MEDIUM_SAMPLE = '\\b(max_cost|budget|token_limit)\\s*[:=]\\s*(none|null|missing)\\b'
CLEAN_SAMPLE = (
                   'route summarizer model small fallback compact-model max_cost 0.02 safety'
                   '_tier standard'
               )

RULES = (
    Rule(
        code='missing-fallback',
        severity='high',
        pattern='\\bfallback\\s*[:=]\\s*(none|null|missing)\\b',
        message='model route has no fallback',
        recommendation='Add a fallback model or explicit degraded-mode behavior.',
    ),
    Rule(
        code='missing-budget',
        severity='medium',
        pattern='\\b(max_cost|budget|token_limit)\\s*[:=]\\s*(none|null|missing)\\b',
        message='route budget control is missing',
        recommendation='Set a max cost or token budget for the route.',
    ),
    Rule(
        code='missing-safety-tier',
        severity='low',
        pattern='\\bsafety_tier\\s*[:=]\\s*(none|null|missing)\\b',
        message='safety tier is not declared',
        recommendation='Declare safety posture for this model path.',
    ),
)
