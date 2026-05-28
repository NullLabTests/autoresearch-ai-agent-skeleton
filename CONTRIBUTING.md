# Contributing

Thanks for considering contributing to AutoResearch AI Agent Skeleton.

## How to Contribute

### Improving the Evolution System

- **Add new signals**: Extend the signal pools in `auto_evolve.py` or add keyword checks to `evaluate.py`.
- **Tune mutation weights**: Adjust strategy probabilities in `mutate.py` (line 130-133).
- **Write new strategies**: Add mutation strategies to `mutate.py` following the existing pattern.

### Submitting Changes

1. Fork the repo and create a branch from `dev`.
2. Make focused, single-purpose changes.
3. Test by running `python eval.py` to verify scoring still works.
4. Open a pull request against `dev`.

### Bug Reports & Feature Requests

Use the [issue templates](.github/ISSUE_TEMPLATE/) — they help us understand the context quickly.

## Code Style

- Python: ruff-compatible. Run `ruff check .` before committing.
- Keep files self-contained when possible.
- Add comments for non-obvious behavior, not for basic operations.

## Questions?

Open a [discussion](https://github.com/NullLabTests/autoresearch-ai-agent-skeleton/discussions).
