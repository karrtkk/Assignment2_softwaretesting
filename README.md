# Bowling Game – QA Package

## Quickstart
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
pip install -U pip pytest pytest-cov

python run_scenarios.py
python -m pytest -q
python -m pytest --cov=bowling_game --cov-report=term-missing
```

## Generate API docs
```bash
python -m pydoc -w bowling_game
python -m pydoc -w run_scenarios
# move the generated HTML files into ./docs
```
