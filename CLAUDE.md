# Trucker RAG evals

Learning project: a minimal RAG over a trucking FAQ knowledge base, evaluated with pytest and DeepEval.
The goal is the evaluation, not the assistant.

## How to work with me
- I'm building this step by step to learn. Do ONE step at a time and stop.
- Before writing code, explain what you'll do and why. Wait for my OK.
- Prefer small, reviewable changes. Don't touch files outside the current step.
- Tell me which tests you ran and their real results. Never claim something passes without running it.

## Design decisions
- Two JSON files, two roles: data/knowledge_base.json is what the RAG retrieves from;
  evals/golden_dataset.json is the test cases (JSON array, not JSONL).
- Golden case fields: id, input, expected_output, expected_sources, category.
  Empty expected_sources = out-of-scope question.
- Retrieval: BM25 (rank_bm25), top 3, no vector DB for now.
- Generation: LLM answers only from retrieved context and cites entry IDs; fallback without calling the model when nothing is retrieved.
- Tests that call an LLM are marked `llm`; `pytest -m "not llm"` must run free.
- Knowledge base content: public FMCSA rules only, nothing from my client work.

## Environment
macOS, zsh, Python 3.12, venv in .venv.

## Steps
1. Environment, dependencies, config, first commit
2. Knowledge base
3. Golden dataset + src/dataset.py
4. Retriever + tests/test_retrieval.py
5. Generator + pipeline
6. tests/test_citations.py
7. DeepEval: tests/test_generation.py
8. tests/test_safety.py
9. CI + README
