"""Main module for {{ cookiecutter.project_name }}."""


def hello_world() -> str:
    """Return a hello world message.

    Returns:
        str: A greeting message.
    """
    return "Hello, World from {{ cookiecutter.project_name }}!"


def main() -> None:
    """Main entry point for the application."""
    print(hello_world())


if __name__ == "__main__":
    main()
