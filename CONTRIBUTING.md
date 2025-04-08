# Contributing to Synda

Thank you for your interest in contributing to Synda! This document provides guidelines and instructions for contributing to the project.

## Development Environment Setup

Synda uses [uv](https://github.com/astral-sh/uv) for dependency management and virtual environment creation.

### Prerequisites

- Python 3.10 or higher
- uv (can be installed with `pip install uv`)

### Setting Up Your Development Environment

1. Clone the repository:
   ```bash
   git clone https://github.com/timothepearce/synda.git
   cd synda
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   # Using Make
   make setup
   make dev
   
   # Or manually
   uv venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   uv pip install -r requirements-dev.txt
   uv pip install -e .
   ```

## Development Workflow

### Running Tests

```bash
# Run all tests
make test

# Run tests with coverage
make test-cov

# Or manually
python -m pytest tests/
python -m pytest --cov=synda tests/
```

### Code Formatting and Linting

We use Black for code formatting and Ruff for linting:

```bash
# Format code
make format

# Check formatting
make format-check

# Run linter
make lint

# Or manually
python -m black synda/ tests/
python -m black --check synda/ tests/
python -m ruff check synda/ tests/
```

### Continuous Integration

We use GitHub Actions for continuous integration. The following workflows are available:

- **Test**: Runs tests on multiple Python versions and operating systems
- **Code Coverage**: Generates and uploads code coverage reports
- **Dependency Review**: Scans dependencies for security vulnerabilities
- **Publish**: Publishes the package to PyPI when a new release is created

These workflows run automatically on push to main and on pull requests.

### Adding Dependencies

To add a new dependency:

1. Add it to `requirements.txt` (for runtime dependencies) or `requirements-dev.txt` (for development dependencies)
2. Install it with:
   ```bash
   # For runtime dependencies
   uv pip install -r requirements.txt
   
   # For development dependencies
   uv pip install -r requirements-dev.txt
   ```

## Pull Request Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests to ensure they pass
5. Format your code with Black
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

## Code of Conduct

Please be respectful and considerate of others when contributing to this project. We aim to foster an inclusive and welcoming community.

## License

By contributing to Synda, you agree that your contributions will be licensed under the project's Apache 2.0 license.