# Setup Instructions for {{ cookiecutter.project_name }}

This document provides step-by-step instructions for setting up your new Python project with semantic release capabilities.

## Prerequisites

- Python {{ cookiecutter.python_version }}+
- Poetry (for dependency management)
- Git
- GitHub account

## Initial Setup

### 1. Install Dependencies

```bash
# Install Poetry if you haven't already
curl -sSL https://install.python-poetry.org | python3 -

# Install project dependencies
poetry install
```

### 2. Initialize Git Repository

```bash
git init
git add .
git commit -m "feat: initial project setup"
git branch -M main
git remote add origin https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git
git push -u origin main
```

{% if cookiecutter.include_semantic_release == "yes" -%}
## Semantic Release Configuration

### GitHub Personal Access Token Setup

To enable automated releases, you need to create a Personal Access Token (PAT) with the appropriate permissions:

#### Step 1: Create a Personal Access Token

1. Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Set a meaningful name (e.g., "{{ cookiecutter.project_slug }}-semantic-release")
4. Set expiration (recommended: 1 year)
5. Select the following scopes:
   - `repo` (Full control of private repositories)
   - `write:packages` (Upload packages to GitHub Package Registry)

6. Click "Generate token"
7. **Important**: Copy the generated token immediately (you won't be able to see it again)

#### Step 2: Add Token to Repository Secrets

1. Navigate to your repository on GitHub
2. Go to Settings → Secrets and variables → Actions
3. Click "New repository secret"
4. Name: `SEMANTIC_RELEASE_TOKEN`
5. Value: Paste the token you copied in Step 1
6. Click "Add secret"

#### Step 3: Configure Repository Settings

1. Go to Settings → General → Features
2. Ensure "Issues" is enabled (required for semantic-release)
3. Go to Settings → Actions → General
4. Under "Actions permissions", ensure actions are enabled
5. Under "Workflow permissions", select "Read and write permissions"

### Branch Protection (Optional but Recommended)

To ensure semantic-release can push to your main branch:

1. Go to Settings → Branches
2. Add a branch protection rule for `main`
3. Enable "Restrict pushes that create files"
4. Under "Restrict pushes that create files", add your PAT as an exception
5. Or ensure the PAT has admin permissions to bypass restrictions

{% endif -%}
## Development Workflow

### Running Tests

```bash
# Run all tests
poetry run pytest

# Run tests with coverage
poetry run pytest --cov={{ cookiecutter.project_slug }}
```

### Code Formatting and Linting

```bash
# Format code with Black
poetry run black .

# Sort imports with isort
poetry run isort .

# Lint with flake8
poetry run flake8
```

### Making Changes

{% if cookiecutter.include_semantic_release == "yes" -%}
This project uses [Conventional Commits](https://www.conventionalcommits.org/) for automated versioning:

- `feat:` - New features (triggers minor version bump)
- `fix:` - Bug fixes (triggers patch version bump)
- `docs:` - Documentation changes (no version bump)
- `style:`, `refactor:`, `perf:`, `build:`, `ci:`, `chore:` - Other changes (triggers patch version bump)

Example commit messages:
```bash
git commit -m "feat: add new awesome feature"
git commit -m "fix: resolve issue with data processing"
git commit -m "docs: update README with new examples"
```

### Release Process

Releases are automated through GitHub Actions:

1. Make your changes following conventional commit format
2. Push to the `main` branch
3. GitHub Actions will automatically:
   - Analyze commits to determine version bump
   - Generate changelog
   - Create a new release
   - Update version in `pyproject.toml`

{% endif -%}
## Troubleshooting

### Common Issues

1. **Semantic Release Token Issues**
   - Ensure the token has the correct permissions
   - Check that the token hasn't expired
   - Verify the secret name is exactly `SEMANTIC_RELEASE_TOKEN`

2. **Poetry Installation Issues**
   - Make sure you're using Python {{ cookiecutter.python_version }}+
   - Try `poetry env use python{{ cookiecutter.python_version }}`

3. **Test Failures**
   - Run `poetry install` to ensure all dependencies are installed
   - Check that your Python version matches the project requirements

### Getting Help

- Check the [Poetry documentation](https://python-poetry.org/docs/)
- Review [Semantic Release documentation](https://semantic-release.gitbook.io/)
- Check [Conventional Commits specification](https://www.conventionalcommits.org/)

## Next Steps

1. Replace the example code in `{{ cookiecutter.project_slug }}/main.py`
2. Add your project-specific dependencies to `pyproject.toml`
3. Update the README.md with project-specific information
4. Write comprehensive tests for your functionality
5. Set up continuous integration if needed

Happy coding! 🚀
