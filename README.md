# Project: Aegis-CLI

A Simple Tool to Automate Security Docs

The Problem

Every good project needs a SECURITY.md file, a dependabot.yml config, and basic security guidelines. But let's be honest—nobody wants to write them. It’s boring, repetitive, and easy to forget. So, most projects don't have them until it's too late.

The Solution

A simple command-line tool to do the grunt work. It scans your project, figures out what language you're using (Python, JavaScript, etc.), and generates those essential security starter files.

It turns a 15-minute chore into a 3-second command.

Disclaimer: Read This First

Let's be crystal clear: this tool is a starting point, not a magic bullet. It generates boilerplate security documentation based on best practices. It is NOT a vunlerability scanner, a security audit tool, or a replacement for a real security strategy. You still need to do the hard work of writing secure code and using dedicated security tools.

What It Does

    Detects Your Tech Stack: Scans your project to figure out what you're building with (currently supports Python and JavaScript, more on the way).

    Generates Essential Files: Automatically creates a /security folder in your project with:

        SECURITY.md: A solid, customizable policy for how to report vulnerabilities.

        dependabot.yml: A ready-to-use GitHub Actions config to keep your dependencies updated.

        SecureCodingGuide.md: A language-specific check list of common-sense security practices.

How to Install It

Get it from PyPI:
Bash

pip install praximous-aegis-cli

Or, if you want to hack on it yourself, clone the repo:
Bash

git clone https://github.com/JamesTheGiblet/Praximous-Aegis-CLI.git
cd Praximous-Aegis-CLI
pip install -e .

How to Use It

Just point it at your project directory.
Bash

aegis path/to/your/project

It will detect the language and generate the files in a new /security folder inside your project.

Optional Flags:

    --output custom/directory: Put the generated files somewhere else.

    --verbose: See the full scan report as it runs.

    --dry-run: See what it would do without actually writing any files.

What You Get

File	Purpose
SECURITY.md	A clear policy on how to responsibly disclose vulnerabilities.
dependabot.yml	A config for GitHub's Dependabot to automate dependency updates.
SecureCodingGuide.md	A checklist of best practices for the detected language.

Want to Go Deeper? (The Paid Guide)

The free tool gets you started with the basics. But if you want to learn about industry-grade security strategies, penetration testing, and building a secure development lifecycle (SDLC), I'm putting together a comprehensive guide.

It's for serious builders who want to move beyond the fundamentals. You can find out more at jamesthegiblet.co.uk.

The Roadmap

Perfect is the imaginary friend of never shipped, but here's what's next:

    Support for more languages (Java, Go, Rust).

    Optional integration with tools like Snyk or OSV.

    Better dynamic customization of the generated files.

License

This is licensed under the MIT License.

I had a custom license written up ("Praximous Ritual License"), but honestly, they're a pain and just scare people off. Just use the tool, build on it, do what you want.

Stop neglecting the basics. The code is the proof, and good security docs are part of that proof.
