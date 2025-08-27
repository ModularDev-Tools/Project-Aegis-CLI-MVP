from pathlib import Path
import jinja2
import logging

logger = logging.getLogger(__name__)

def get_package_ecosystem(language: str) -> str | None:
    """Maps a language to a GitHub Dependabot package ecosystem."""
    ecosystems = {
        "python": "pip",
        "javascript": "npm",
    }
    return ecosystems.get(language.lower())

def generate_dependabot_yml(project_path: Path, language: str) -> bool:
    try:
        template_path = Path(__file__).parent.parent.parent.parent / 'templates' / 'dependabot.yml.j2'
        if not template_path.exists():
            logger.error(f"Template file not found: {template_path}")
            return False

        try:
            with open(template_path, 'r', encoding='utf-8') as f:
                template = jinja2.Template(f.read())
        except Exception as e:
            logger.error(f"Failed to read template file: {e}")
            return False

        try:
            package_ecosystem = get_package_ecosystem(language)
            if not package_ecosystem:
                logger.warning(f"No dependabot ecosystem for language '{language}'. Skipping file generation.")
                return True # Not a failure, just nothing to do

            content = template.render(package_ecosystem=package_ecosystem)
        except jinja2.TemplateError as e:
            logger.error(f"Failed to render template: {e}")
            return False

        github_dir = project_path / '.github'
        try:
            github_dir.mkdir(exist_ok=True)
        except Exception as e:
            logger.error(f"Failed to create .github directory: {e}")
            return False

        dependabot_file = github_dir / 'dependabot.yml'
        try:
            dependabot_file.write_text(content, encoding='utf-8')
        except Exception as e:
            logger.error(f"Failed to write dependabot.yml: {e}")
            return False

        logger.info(f"dependabot.yml generated successfully at {dependabot_file}")
        return True

    except Exception as e:
        logger.exception(f"Unexpected error generating dependabot.yml: {e}")
        return False