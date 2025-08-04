Praximous-Aegis-CLI is a command-line ritual designed to scan your codebase, detect its language and dependencies, and generate essential security documentation tailored to your tech stack. Whether you're launching a solo project or overseeing a distributed team, this tool automates the first—and often overlooked—layer of good governance.
Table of Contents
 * Disclaimer
 * Features
 * Installation
 * Usage
 * Generated Files Breakdown
 * Premium Expansion
 * Attribution & Community
 * Roadmap
 * License
Disclaimer
This tool provides a foundational layer of security documentation and configuration. Praximous-Aegis-CLI is not a vulnerability scanner or a replacement for a comprehensive security strategy. It is designed to automate best practices and provide a starting point for security governance. Always conduct thorough code reviews and use dedicated security tools and services.
⚙️ Features
 * 🔍 Language Detection
   Scans project files to determine framework and ecosystem (supports Python, JavaScript; more coming soon).
 * 📜 Security Documentation Generator
   Automatically generates:
   * SECURITY.md: A detailed, customizable policy based on best practices.
   * dependabot.yml: GitHub-ready config for dependency automation.
   * SecureCodingGuide.md: Language-specific checklist to ward off common vulnerabilities.
 * 🧠 Self-Evolving Roadmap
   Tracks upcoming feature drops, supported languages, and premium security expansions.
🚀 Installation
Install from PyPI:
pip install praximous-aegis-cli

Or for local development:
git clone https://github.com/JamesTheGiblet/Praximous-Aegis-CLI.git
cd Praximous-Aegis-CLI
pip install -e .

🧪 Usage
Basic ritual invocation:
aegis path/to/your/project

This will output:
 * A new /security/ folder in your project root.
 * Your SECURITY.md, dependabot.yml, and SecureCodingGuide.md tailored to the detected ecosystem.
Optional flags:
--output custom/directory      # Set a custom folder for generated files
--verbose                      # See full scan report during generation
--dry-run                      # Run without writing files (preview mode)

📁 Generated Files Breakdown
| File | Purpose |
|---|---|
| SECURITY.md | Outlines policy, contact info, supported versions, and tools. |
| dependabot.yml | GitHub config for automated updates and vulnerability alerts. |
| SecureCodingGuide.md | Framework-specific checklist to support clean, secure builds. |
✨ Premium Expansion
The Praximous Aegis Roadmap is an advanced builder’s guide to securing your project across its lifecycle. Available soon via jamesthegiblet.co.uk:
 * Industry-grade compliance checklists
 * Penetration testing templates
 * SDLC integration strategies
 * Security culture blueprints
Join the waitlist or become a supporter to unlock deeper layers of defense and mythic mastery.
📣 Attribution & Community
Crafted by James the Giblet—digital architect and mythic builder.
Open-source license applies to this tool and generated files. Respect the ritual, fork with clarity.
Contributors welcome: create PRs with modular additions, clean commits, and glyph-rich documentation.
🧭 Roadmap
Next releases will include:
 * Support for more languages (e.g., Java, Go, Rust)
 * Optional integration with Snyk or OSV
 * Discord-powered contributor rituals
 * Dynamic README customization
🕊️ License
Licensed under the Praximous Ritual License (PRL) v1.0. Fork freely, but attribute mythic lineage.
