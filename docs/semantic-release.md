# Semantic Release Guide

This project uses semantic release to automate versioning and changelog generation based on commit messages.

## Commit Message Format

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### Types

- `feat`: A new feature (triggers minor version bump)
- `fix`: A bug fix (triggers patch version bump)
- `docs`: Documentation only changes (no release)
- `style`: Changes that do not affect the meaning of the code (no release)
- `refactor`: A code change that neither fixes a bug nor adds a feature (triggers patch version bump)
- `perf`: A code change that improves performance (triggers patch version bump)
- `test`: Adding missing tests or correcting existing tests (no release)
- `build`: Changes that affect the build system (triggers patch version bump)
- `ci`: Changes to CI configuration files and scripts (no release)
- `chore`: Other changes that don't modify src or test files (no release)
- `revert`: Reverts a previous commit (triggers patch version bump)

### Breaking Changes

To trigger a major version bump, include `BREAKING CHANGE:` in the commit footer or add `!` after the type:

```
feat!: remove deprecated API endpoint

BREAKING CHANGE: The /api/v1/old-endpoint has been removed.
```

### Examples

```
feat: add housing price prediction model
fix: resolve data validation error in price calculator
docs: update API documentation
refactor: optimize database queries
perf: improve model training performance
```

## Release Process

1. The workflow runs automatically on pushes to `main`
2. It analyzes commit messages since the last release
3. If release-worthy commits are found:
   - Calculates the new version number
   - Updates `pyproject.toml` version
   - Generates/updates `CHANGELOG.md`
   - Creates a Git tag
   - Publishes a GitHub Release

## Skipping Releases

To skip the release process, include `[skip ci]` in your commit message:

```
chore: update documentation [skip ci]
```

## Workflow Features

- **Idempotent**: Safe to re-run on the same commit
- **Fail-safe**: Validates repository structure before proceeding
- **Transparent**: Detailed logs and error messages
- **Automated**: No manual intervention required
