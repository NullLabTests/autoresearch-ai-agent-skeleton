#!/usr/bin/env python3
import os
import re
import random

ADDITIONS_POOL = [
    # Structure
    "\nStructure: src/ package with __init__.py, core.py, tools.py, config.py",
    "\nInclude a .env.example with OLLAMA_HOST, MODEL_NAME, TEMPERATURE",
    "\nAdd a Makefile with targets: install, run, test, lint, clean",
    "\nInclude docker-compose.yml with Ollama service",
    "\nAdd pre-commit config with ruff and mypy",
    # Quality
    "\nUse structlog for structured logging with JSON output",
    "\nImplement retry logic with tenacity for LLM calls",
    "\nAdd input validation with Pydantic models throughout",
    "\nInclude comprehensive error handling with custom exceptions",
    "\nUse asyncio.gather for parallel tool execution",
    # Testing
    "\nInclude pytest tests with mocking for Ollama",
    "\nAdd property-based tests with hypothesis where applicable",
    # Output
    "\nOutput raw markdown code blocks: ```filename.py ... ```",
    "\nEach file must be syntactically valid Python - no placeholder comments",
    "\nMake the agent installable with `pip install -e .`",
    "\nInclude a '5 minute quickstart' section in README",
    # Local models
    "\nOptimize prompts for 7B-13B local models - be specific and structured",
    "\nAdd model fallback chain: qwen2.5:7b -> llama3.2:3b -> phi3:mini",
    "\nInclude token tracking and context window management",
]

CROSSOVER_CHUNKS = [
    "Use: LangGraph for orchestration, Ollama for inference, Pydantic for validation.",
    "Tech stack: langgraph, ollama, pydantic, httpx, rich, structlog, pytest.",
    "Include pyproject.toml with all dependencies pinned.",
    "Type hints on every function signature. No exceptions.",
    "Async-first design with asyncio throughout.",
    "README must include: install, configure, run, test, extend sections.",
    "Output every file in ```filename language code blocks.",
    "The agent must work with Ollama/local models out of the box.",
]


def read_scores() -> dict:
    scores = {}
    try:
        with open("results.log") as f:
            for line in f:
                m = re.search(r"(\w+\.txt).*?(\d+\.?\d*)", line)
                if m:
                    scores[m.group(1)] = float(m.group(2))
    except FileNotFoundError:
        pass
    return scores


def get_best_prompt_file() -> str:
    scores = read_scores()
    files = [f for f in os.listdir("population") if f.endswith(".txt")]
    if not files:
        return None
    if scores:
        scored = [(f, scores.get(f, 0)) for f in files]
        scored.sort(key=lambda x: -x[1])
        return scored[0][0]
    return random.choice(files)


def mutate():
    files = [f for f in os.listdir("population") if f.endswith(".txt")]
    if not files:
        return

    best_file = get_best_prompt_file()
    source = os.path.join("population", best_file)
    with open(source) as f:
        content = f.read()

    strategy = random.choices(
        ["append", "crossover", "rewrite_section", "combine"],
        weights=[0.3, 0.3, 0.2, 0.2],
    )[0]

    if strategy == "append":
        addition = random.choice(ADDITIONS_POOL)
        new_content = content + addition

    elif strategy == "crossover":
        other = random.choice([f for f in files if f != best_file] or files)
        with open(os.path.join("population", other)) as f:
            other_content = f.read()
        chunk = random.choice(CROSSOVER_CHUNKS)
        new_content = content + "\n" + chunk

    elif strategy == "rewrite_section":
        addition = random.choice(ADDITIONS_POOL)
        lines = content.split("\n")
        insert_at = random.randint(len(lines) // 2, len(lines))
        lines.insert(insert_at, addition)
        new_content = "\n".join(lines)

    else:
        other = random.choice([f for f in files if f != best_file] or files)
        with open(os.path.join("population", other)) as f:
            other_content = f.read()
        half1 = content[: len(content) // 2]
        half2 = other_content[len(other_content) // 2 :]
        new_content = half1 + "\n" + half2

    new_name = f"prompt_{len(files)+1:03d}.txt"
    with open(os.path.join("population", new_name), "w") as f:
        f.write(new_content)

    print(f"Created mutated prompt: {new_name} (from {best_file}, strategy={strategy})")


if __name__ == "__main__":
    mutate()
