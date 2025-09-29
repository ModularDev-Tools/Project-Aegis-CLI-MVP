# Contributing to Project Aegis CLI

First off, thank you for considering contributing to Project Aegis! Your help is invaluable in making this tool better for everyone.

## How Can I Contribute?

### Reporting Bugs

If you encounter a bug, please [open an issue](https://github.com/JamesTheGiblet/Project-Aegis-CLI/issues) and include the following information:

- A clear and descriptive title.
- Steps to reproduce the bug.
- The version of Aegis CLI you are using.
- Your operating system and Python version.
- Any relevant error messages or logs.

### Suggesting Enhancements

Have an idea for a new feature or an improvement to an existing one? We'd love to hear it! Please [open an issue](https://github.com/JamesTheGiblet/Project-Aegis-CLI/issues) and use the "Feature Request" template if available. Describe your idea with as much detail as possible.

### Pull Requests

We welcome pull requests for bug fixes and new features. Here’s how to get started:

#### 1. Set Up Your Environment

1. **Fork the repository** on GitHub.
2. **Clone your fork** locally:

    ```bash
    git clone https://github.com/YOUR_USERNAME/Project-Aegis-CLI.git
    cd Project-Aegis-CLI
    ```

3. **Create a virtual environment** to keep dependencies isolated:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

4. **Install the project in editable mode** with test dependencies. This command is also found in the `README.md`:

    ```bash
    pip install -e .[test]
    ```

    This will install the project so that your changes to the source code are immediately reflected when you run the `aegis` command.

#### 2. Make Your Changes

1. Create a new branch for your feature or bugfix:

    ```bash
    git checkout -b your-feature-name
    ```

2. Write your code! Ensure it follows the existing style.
3. Add or update tests for your changes.

#### 3. Run Tests

Before submitting your pull request, please run the test suite to ensure everything is working correctly:

```bash
pytest
```

#### 4. Submit a Pull Request

Push your branch to your fork and open a pull request. In your PR description, please explain the changes you've made and link to any relevant issues.

Thank you for your contribution!
