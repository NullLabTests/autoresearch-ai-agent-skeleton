![](https://img.shields.io/badge/status-active-success)
![](https://img.shields.io/badge/license-MIT-67ac09)
![](https://img.shields.io/badge/python-3.12%2b-007ec6)
![](https://img.shields.io/badge/generations-33-blueviolet)
![](https://img.shields.io/badge/score-422%2f500-brightgreen)
![](https://img.shields.io/badge/population-33%20prompts-orange)

# AutoResearch AI Agent Skeleton

**Evolutionary prompt optimization for AI agent code generation.**

This project uses a genetic algorithm to automatically evolve prompts that generate better and better AI agent project skeletons. Starting from a simple seed prompt, it iteratively mutates, evaluates, and selects the fittest prompts — treating prompt engineering as a search problem rather than a manual craft.

## How It Works

The system implements a **"modify → evaluate → keep/revert"** loop, inspired by [Andrej Karpathy's `autoresearch`](https://github.com/karpathy/autoresearch) project. Karpathy's original concept applied this loop to autonomously improve training code. We borrowed the core idea and applied it to **evolving AI agent prompts** instead.

### The Evolutionary Loop

```
               ┌─────────────────┐
               │   Population    │
               │  (33 prompts)   │
               └────────┬────────┘
                        │
                        ▼
               ┌─────────────────┐
               │    mutate.py    │
               │  (crossover /   │
               │   append /      │
               │   rewrite)      │
               └────────┬────────┘
                        │
                        ▼
               ┌─────────────────┐
               │   evaluate.py   │
               │  (200+ quality  │
               │    signals)     │
               └────────┬────────┘
                        │
                        ▼
               ┌─────────────────┐
               │   reflect.py    │
               │  (rank, observe,│
               │   persist)      │
               └────────┬────────┘
                        │
                        ▼
               ┌─────────────────┐
               │  Select best →  │
               │  repeat (gen++) │
               └─────────────────┘
```

### Components

| File | Purpose |
|------|---------|
| `mutate.py` | Creates new prompt variants from the best current prompt using four strategies: append (add a new instruction), crossover (merge with another prompt), rewrite_section (insert mid-prompt), and combine (splice halves of two prompts). |
| `evaluate.py` | Scores each prompt against 200+ quality signals across categories: tech stack, code quality, testing depth, security, performance, documentation, deployment, design patterns, and more. Scores range from 35 (basic) to 500+ (production-grade). |
| `reflect.py` | Records each generation's rankings, computes statistics (average, spread, min/max), and extracts observations about what differentiates elite prompts. All data persists to `reflection.md`. |
| `run_evolution.sh` | Orchestrates the full loop: mutate → evaluate → reflect → commit → repeat. Run it and let evolution do the rest. |
| `prompt.txt` | The seed prompt used in the top-level outer loop (simple eval-only system). |
| `program.md` | Instructions for running the optimization loop with OpenCode or Cursor. |

### Mutation Strategies

1. **Append** (30%) — Adds a random quality-improving instruction to the end of the best prompt
2. **Crossover** (30%) — Merges a chunk from another prompt into the best prompt
3. **Rewrite Section** (20%) — Inserts a new instruction at a random position in the prompt
4. **Combine** (20%) — Splices the first half of the best prompt with the second half of another

## Current Status

**Latest Generation:** 33
**Best Prompt:** `prompt_031.txt` — **422/500**
**Population Size:** 33 prompts
**Score Progression:** 35 → 86 → 92 → 140 → 196 → 286 → 330 → 422

The best prompt generates production-ready agent projects with:
- Full `src/package/` layout with 20+ modules
- LangGraph ReAct loop + Ollama local models
- Pydantic v2 config, Pydantic validation, type hints everywhere
- Async/await, streaming, SSE/websocket support
- OpenTelemetry + Prometheus + Grafana observability
- OAuth2/JWT auth, rate limiting, encryption
- pytest with hypothesis, snapshot, benchmark, fuzz testing
- Docker, docker-compose, Kubernetes, systemd deployment
- Design patterns: factory, strategy, observer, repository, pipeline
- CI/CD with GitHub Actions + dependabot + pre-commit

## Quick Start

```bash
# Clone the repo
git clone https://github.com/NullLabTests/autoresearch-ai-agent-skeleton.git
cd autoresearch-ai-agent-skeleton

# Run a single evaluation on the current prompt
python eval.py

# Or run the full evolutionary loop (Linux/macOS)
cd autoresearch-ai-agent-skeleton
chmod +x run_evolution.sh
./run_evolution.sh
```

### Using with OpenCode or Cursor

1. Open this repo in OpenCode or Cursor
2. Edit `prompt.txt` to improve it
3. Run `python eval.py` to see if your change improved the score
4. If score goes up → commit. If down → revert.
5. Repeat.

(See `program.md` for detailed instructions.)

## Project Structure

```
autoresearch-ai-agent-skeleton/
├── README.md              # This file
├── LICENSE                # MIT license
├── program.md             # Instructions for OpenCode/Cursor
├── prompt.txt             # Seed prompt (outer loop)
├── eval.py                # Simple score evaluator (outer loop)
├── .gitignore
└── autoresearch-ai-agent-skeleton/  # Core evolution system
    ├── mutate.py          # Genetic mutation engine
    ├── evaluate.py        # 200+ signal scoring engine
    ├── reflect.py         # Generation reflection & insights
    ├── run_evolution.sh   # Full automation script
    ├── reflection.md      # Historical record of all generations
    ├── population/        # Evolved prompts
    │   ├── prompt_001.txt # Generation 1
    │   ├── prompt_002.txt
    │   └── ...            # 33 prompts and counting
    └── results.log        # Latest evaluation results
```

## Credits

This project is inspired by [Andrej Karpathy's `autoresearch`](https://github.com/karpathy/autoresearch), which introduced the elegant "modify → evaluate → keep/revert" loop for autonomous code improvement. We applied the same principle to the domain of prompt engineering — evolving prompts instead of training code.

## License

MIT — see [LICENSE](LICENSE) for details.
