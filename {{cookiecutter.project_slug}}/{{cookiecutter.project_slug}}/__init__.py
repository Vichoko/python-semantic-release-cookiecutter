"""{{ cookiecutter.project_name }}.

{{ cookiecutter.project_description }}
"""
# {{ cookiecutter.project_name }}
__version__ = "0.1.0"
__author__ = "{{ cookiecutter.author_name }}"
__email__ = "{{ cookiecutter.author_email }}"

# Add your main package imports here
# Example:
# from .main import main_function

{{ cookiecutter.project_description }}

## Installation

```bash
# Using Poetry (recommended)
poetry install

# Using pip
pip install {{ cookiecutter.project_slug }}
```

## Usage

```python
import {{ cookiecutter.project_slug }}

# Your code here
```

## Development

This project uses Poetry for dependency management and packaging.

```bash
# Install dependencies
poetry install

# Run tests
poetry run pytest

# Format code
poetry run black .
poetry run isort .

# Lint code
poetry run flake8
```

{% if cookiecutter.include_semantic_release == "yes" -%}
## Releases

This project uses semantic-release for automated versioning and releases. Commits should follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

- `feat:` for new features (minor version bump)
- `fix:` for bug fixes (patch version bump)
- `docs:` for documentation changes (no version bump)
- `style:`, `refactor:`, `perf:`, `build:`, `ci:`, `chore:` for other changes (patch version bump)

{% endif -%}
## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

{% if cookiecutter.license != "None" -%}
## License

This project is licensed under the {{ cookiecutter.license }} License - see the LICENSE file for details.
{% endif -%}

## Author

{{ cookiecutter.author_name }} - {{ cookiecutter.author_email }}
