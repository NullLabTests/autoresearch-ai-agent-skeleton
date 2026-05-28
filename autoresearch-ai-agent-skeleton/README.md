# Grounded Prompt Evolution System

This is the core engine that drives the prompt optimization loop.

## How It Works

1. **`mutate.py`** — Takes the highest-scoring prompt from the population and creates a new variant by appending, crossbreeding, rewriting, or combining.
2. **`evaluate.py`** — Scores all prompts against 200+ quality signals (tech stack, code quality, testing, security, performance, etc.).
3. **`reflect.py`** — Records rankings, statistics, and observations about what differentiates elite prompts.

## Usage

```bash
# Run one complete generation
python mutate.py && python evaluate.py && python reflect.py

# Or run the full automated loop
chmod +x run_evolution.sh
./run_evolution.sh
```

## Population

All prompts live in `population/`. The latest results are in `results.log`. Full historical record is in `reflection.md`.

Current best: **prompt_031.txt** (422/500)
