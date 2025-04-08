.PHONY: setup install dev clean test test-cov lint format build check develop install-package

# Default virtual environment path
VENV_PATH ?= .venv

setup:
        python -m uv venv $(VENV_PATH)

install:
        python -m uv pip install -r requirements.txt

dev:
        python -m uv pip install -r requirements-dev.txt

clean:
        rm -rf $(VENV_PATH)
        rm -rf build/
        rm -rf dist/
        rm -rf *.egg-info/
        find . -type d -name __pycache__ -exec rm -rf {} +
        find . -type f -name "*.pyc" -delete
        rm -rf .coverage
        rm -rf coverage.xml
        rm -rf htmlcov/

test:
        python -m pytest tests/ -v

test-cov:
        python -m pytest --cov=synda --cov-report=term --cov-report=html tests/

lint:
        python -m ruff check synda/ tests/

format:
        python -m black synda/ tests/

format-check:
        python -m black --check synda/ tests/

# Install in development mode
develop:
        python -m uv pip install -e .

# Build the package
build:
        python -m uv pip install build
        python -m build

# Check the built package
check:
        python -m uv pip install twine
        python -m twine check dist/*

# Install the package
install-package:
        python -m uv pip install .