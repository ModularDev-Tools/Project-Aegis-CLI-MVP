from pathlib import Path
import jinja2
import logging

logger = logging.getLogger(__name__)

def generate_security_md(output_dir: Path, language: str, project_name: str = None) -> bool:
    try:
        template_path = Path(__file__).parent.parent.parent.parent / 'templates' / 'SECURITY.md.j2'
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
            content = template.render(
                language=language,
                project_name=project_name or "Our Project"
            )
        except Exception as e:
            logger.error(f"Failed to render template: {e}")
            return False

        security_file = output_dir / 'SECURITY.md'
        try:
            security_file.write_text(content, encoding='utf-8')
        except Exception as e:
            logger.error(f"Failed to write SECURITY.md file: {e}")
            return False

        logger.info(f"SECURITY.md generated successfully at {security_file}")
        return True

    except Exception as e:
        logger.exception(f"Unexpected error generating SECURITY.md: {e}")
        return False