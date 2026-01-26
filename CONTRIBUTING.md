# Contributing to Robust Document OCR Preprocessing Pipeline

Thank you for your interest in contributing to this project! We welcome contributions from everyone.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Coding Guidelines](#coding-guidelines)
- [Testing](#testing)
- [Pull Request Process](#pull-request-process)
- [Documentation](#documentation)
- [Reporting Issues](#reporting-issues)

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

- Use the [Bug Report template](.github/ISSUE_TEMPLATE/bug_report.md)
- Include detailed steps to reproduce
- Provide environment information
- Add screenshots if applicable

### Suggesting Enhancements

- Use the [Feature Request template](.github/ISSUE_TEMPLATE/feature_request.md)
- Explain the problem you're trying to solve
- Describe your proposed solution
- Consider alternatives

### Code Contributions

- Fix bugs
- Implement new features
- Improve performance
- Enhance documentation
- Add test cases

## Development Setup

1. **Fork the repository** on GitHub
2. **Clone your fork**:
   ```bash
   git clone https://github.com/yourusername/robust-document-ocr-preprocessing.git
   cd robust-document-ocr-preprocessing
   ```

3. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install dependencies**:
   ```bash
   pip install -e .[dev]
   ```

5. **Install pre-commit hooks**:
   ```bash
   pip install pre-commit
   pre-commit install
   ```

## Coding Guidelines

### Python Style

- Follow [PEP 8](https://peps.python.org/pep-0008/) style guide
- Use [Black](https://black.readthedocs.io/) for code formatting
- Use [isort](https://pycqa.github.io/isort/) for import sorting
- Type hints are encouraged but not required

### Code Quality

- Write clear, readable code
- Add docstrings for all public functions and classes
- Include comments for complex logic
- Keep functions focused and small
- Follow the existing code patterns

### Commit Messages

- Use present tense ("Add feature" not "Added feature")
- First line: 50 characters or less
- Reference issues when applicable (e.g., "Fixes #123")
- Include detailed explanation in body if needed

## Testing

### Running Tests

```bash
pytest
```

### Test Coverage

```bash
pytest --cov=src --cov-report=html
```

### Writing Tests

- Add tests for new features
- Update tests for bug fixes
- Test edge cases
- Use descriptive test names
- Keep tests focused and fast

## Pull Request Process

1. **Create a branch** for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following the coding guidelines

3. **Run tests** to ensure nothing breaks:
   ```bash
   pytest
   ```

4. **Update documentation** if needed

5. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request** on GitHub using the PR template

7. **Address review feedback** and update your PR

## Documentation

- Update docstrings when changing function behavior
- Keep README.md up to date
- Add examples for new features
- Update architecture documentation if needed

## Reporting Issues

- Search existing issues before creating new ones
- Use the appropriate issue template
- Provide as much detail as possible
- Include reproduction steps
- Be responsive to follow-up questions

## Community

- Join our discussions
- Help answer questions
- Review other contributions
- Share your use cases

Thank you for contributing to making this project better!