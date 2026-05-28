#!/usr/bin/env python3
import os
import re
import subprocess
import tempfile
import shutil
from pathlib import Path

def evaluate_generated_project(project_path: str) -> float:
    """Try to actually run the generated project and score it."""
    score = 40.0
    project_path = Path(project_path)
    
    if not project_path.exists():
        return 30.0
    
    # Check for basic structure
    if (project_path / "pyproject.toml").exists() or (project_path / "requirements.txt").exists():
        score += 15
    
    if any((project_path).rglob("*.py")):
        score += 10
    
    # Try to run it (very carefully)
    try:
        # Simple test: can we at least parse the main Python files?
        py_files = list(project_path.rglob("*.py"))[:3]
        for py in py_files:
            result = subprocess.run(
                ["python", "-m", "py_compile", str(py)],
                capture_output=True,
                timeout=10
            )
            if result.returncode == 0:
                score += 8
    except Exception:
        pass
    
    # Bonus for modern tooling
    if (project_path / "pyproject.toml").exists():
        score += 7
    
    return min(100.0, round(score, 1))


def evaluate_population():
    scores = {}
    for f in sorted(os.listdir("population")):
        if f.endswith(".txt"):
            path = os.path.join("population", f)
            with open(path) as file:
                raw = file.read()
            content = raw.lower()
            
            score = 30.0
            
            # --- Tech stack signals ---
            if "ollama" in content:
                score += 6
            if "local" in content:
                score += 3
            if "langgraph" in content:
                score += 5
            if "react" in content or "react loop" in content:
                score += 3
            if "pydantic" in content:
                score += 3
            if "httpx" in content:
                score += 2
            if "rich" in content:
                score += 2
            if "structlog" in content:
                score += 2
            if "tenacity" in content:
                score += 2
            if "tiktoken" in content:
                score += 1
            if "pytest" in content:
                score += 2
            if "ruff" in content:
                score += 1
            if "mypy" in content:
                score += 1
            if "pre-commit" in content or "precommit" in content:
                score += 2
            
            # --- Quality signals ---
            if "pyproject.toml" in content:
                score += 4
            if "requirements.txt" in content:
                score += 1
            if "type hint" in content or "type hints" in content:
                score += 3
            if "error handling" in content:
                score += 2
            if "logging" in content:
                score += 2
            if "test" in content or "tests" in content:
                score += 2
            if "async" in content:
                score += 2
            if "streaming" in content or "stream" in content:
                score += 2
            if "retry" in content:
                score += 2
            if "context window" in content or "context management" in content:
                score += 2
            if "token tracking" in content or "token count" in content:
                score += 2
            if "fallback" in content:
                score += 2
            if "main()" in content or "entrypoint" in content or "__main__" in content:
                score += 2
            if "asyncio" in content:
                score += 1
            if "async generator" in content:
                score += 1
            if "custom exception" in content:
                score += 1
            if "dataclass" in content:
                score += 1
            if "enum" in content:
                score += 1
            if "env" in content and ("example" in content or ".env" in content):
                score += 2
            if "docker-compose" in content:
                score += 2
            if "makefile" in content or "taskfile" in content:
                score += 2
            if ".gitignore" in content or "gitignore" in content:
                score += 2
            if "docstring" in content:
                score += 2
            if "parallel" in content or "concurrent" in content:
                score += 2
            if "rate limit" in content or "ratelimit" in content:
                score += 2
            if "caching" in content or "cache" in content:
                score += 2
            if "pydantic" in content and ("setting" in content or "basesetting" in content):
                score += 2
            if "ci" in content or "github action" in content or "gitlab ci" in content:
                score += 2
            if "src/" in content:
                score += 2
            if "__init__.py" in content:
                score += 2
            if "dockerfile" in content:
                score += 2
            if "memory" in content or "persistence" in content:
                score += 2
            if "session" in content or "conversation" in content:
                score += 2
            if "tool calling" in content or "function calling" in content:
                score += 2
            if "coverage" in content or "--cov" in content:
                score += 2
            if "healthcheck" in content or "health check" in content:
                score += 2
            if "development" in content and "depend" in content:
                score += 2
            if "openai" in content and "compatible" in content:
                score += 2
            if "cli" in content or "command line" in content:
                score += 2
            if "timeout" in content or "deadline" in content:
                score += 2
            if "middleware" in content or "interceptor" in content:
                score += 2
            if "observability" in content or "monitoring" in content or "tracing" in content:
                score += 2
            if "metrics" in content or "prometheus" in content:
                score += 2
            if "websocket" in content or "sse" in content or "server-sent" in content:
                score += 2
            if "safety" in content or "guardrail" in content:
                score += 2
            if "event" in content and "driven" in content:
                score += 2
            if "serialization" in content or "serialize" in content:
                score += 2
            if "state" in content and ("management" in content or "machine" in content):
                score += 2
            if "multi-turn" in content or "multi-step" in content:
                score += 2
            if "embedding" in content or "vector" in content:
                score += 2
            if "rag" in content or "retrieval" in content:
                score += 2
            if "tokenizer" in content or "tokenize" in content:
                score += 2
            if "thread" in content and ("safe" in content or "safety" in content):
                score += 2
            if "validation" in content and ("config" in content or "schema" in content):
                score += 2
            if "dependency injection" in content or "di" in content:
                score += 2
            if "callback" in content or "webhook" in content:
                score += 2
            if "feedback" in content or "self-critique" in content:
                score += 2
            if "ablation" in content:
                score += 2
            if "semantic" in content and ("cache" in content or "search" in content):
                score += 2
            
            # --- Security & Auth ---
            if "auth" in content or "authentication" in content:
                score += 2
            if "api key" in content or "secret" in content:
                score += 2
            if "sanitization" in content or "sanitize" in content:
                score += 2
            if "encrypt" in content:
                score += 2
            
            # --- Performance ---
            if "connection pool" in content or "pooling" in content:
                score += 2
            if "lazy" in content and ("load" in content or "init" in content):
                score += 2
            if "background" in content and ("task" in content or "worker" in content):
                score += 2
            if "batch" in content:
                score += 2
            if "circuit breaker" in content:
                score += 2
            
            # --- Storage ---
            if "database" in content or "sqlite" in content or "postgres" in content:
                score += 2
            if "migration" in content and ("alembic" in content or "db" in content):
                score += 2
            if "redis" in content:
                score += 2
            if "file" in content and ("storage" in content or "system" in content):
                score += 2
            
            # --- Testing depth ---
            if "integration" in content and ("test" in content or "testing" in content):
                score += 2
            if "e2e" in content or "end-to-end" in content:
                score += 2
            if "snapshot" in content:
                score += 2
            if "property" in content and ("test" in content or "based" in content):
                score += 2
            if "mock" in content or "fixture" in content:
                score += 2
            
            # --- Documentation ---
            if "sphinx" in content or "mkdocs" in content:
                score += 2
            if "openapi" in content or "swagger" in content:
                score += 2
            if "changelog" in content:
                score += 2
            
            # --- Deployment & Ops ---
            if "kubernetes" in content or "k8s" in content:
                score += 2
            if "systemd" in content or "supervisor" in content:
                score += 2
            if "health" in content and ("endpoint" in content or "probe" in content):
                score += 2
            if "graceful" in content and ("shutdown" in content or "signal" in content):
                score += 2
            if "dependabot" in content or "renovate" in content:
                score += 2
            
            # --- Design Patterns ---
            if "factory" in content:
                score += 2
            if "strategy" in content:
                score += 2
            if "observer" in content:
                score += 2
            if "repository" in content:
                score += 2
            if "pipeline" in content:
                score += 2
            
            # --- Advanced Code Quality ---
            if "cyclomatic" in content:
                score += 2
            if "coverage" in content and ("threshold" in content or "percent" in content):
                score += 2
            if "format" in content or "formatter" in content:
                score += 2
            
            # --- Ollama/Model Specific ---
            if "keep_alive" in content or "num_ctx" in content:
                score += 2
            if "vision" in content or "multimodal" in content:
                score += 2
            if "mirostat" in content or "top_p" in content or "top_k" in content:
                score += 2
            
            # --- Project files ---
            if "dockerignore" in content or ".dockerignore" in content:
                score += 2
            if "editorconfig" in content or ".editorconfig" in content:
                score += 2
            if "dependabot" in content or "renovate" in content:
                score += 2
            if "makefile" in content and ("target" in content or "phony" in content):
                score += 2
            
            # --- Streaming / Real-time ---
            if "chunk" in content or "delta" in content:
                score += 2
            
            # --- Configuration ---
            if "env" in content and ("file" in content or "loader" in content):
                score += 2
            if "config" in content and ("hierarchical" in content or "multi-env" in content):
                score += 2
            
            # --- Output structure ---
            if "```" in content:
                score += 3
            if "." in raw and ("readme" in content or "README" in raw):
                score += 2
            if "installable" in content or "pip install" in content:
                score += 2
            if "runnable" in content or "python -m" in content:
                score += 2
            
            # --- Comprehensiveness ---
            words = len(content.split())
            if words > 150:
                score += 2
            if words > 250:
                score += 2
            if words > 350:
                score += 2
            if words > 450:
                score += 2
            
            # --- Specificity: mentions concrete versions/pins ---
            if "==" in content or ">=" in content:
                score += 2
            if ">=" in content and "0" in content:
                score += 1
            if re.search(r'>=\s*\d+\.\d+\.\d+', content):
                score += 2
            
            scores[f] = round(min(350.0, score), 1)
            print(f"{f}: {scores[f]}")
    
    if scores:
        best = max(scores, key=scores.get)
        print(f"\nBest prompt this round: {best} ({scores[best]})")
    return scores


if __name__ == "__main__":
    evaluate_population()
