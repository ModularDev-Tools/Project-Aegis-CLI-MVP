# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2023-10-27

### Added

- **Expanded Language Support**: Aegis now detects and generates guides for **Java** and **Rust** projects, in addition to Python and JavaScript.
- **Git Hook Integration**: A new `aegis install-hook` command sets up a pre-commit Git hook to ensure security files are present before committing.
- **Compliance Check Command**: A new `aegis check` command allows for manual or CI-based verification that essential security files exist.
- **List Languages Command**: A new `aegis list-languages` command displays all currently supported languages.

### Changed

- **Project Refactoring**: The internal codebase has been refactored for improved maintainability and separation of concerns.
- **Enhanced CLI Output**: The `check` command now uses colored output for better readability.
- **Updated Documentation**: The `README.md` has been updated to reflect all new 2.0 features.

## [1.0.0] - 2023-10-26

### Initial Release

- Initial release of Project Aegis CLI.
- Language detection for Python and JavaScript.
- Generation of `SECURITY.md`, `dependabot.yml`, and language-specific `SecureCodingGuide.md`.
- Support for `--dry-run`, `--verbose`, and `--output` options.
