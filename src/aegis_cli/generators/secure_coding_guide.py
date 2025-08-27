from pathlib import Path
import jinja2
import logging

logger = logging.getLogger(__name__)

def generate_secure_coding_guide(output_dir: Path, language: str) -> bool:
    try:
        template_path = Path(__file__).parent.parent.parent.parent / 'templates' / 'SecureCodingGuide.md.j2'
        if not template_path.exists():
            logger.error(f"Template file not found: {template_path}")
            return False

        with open(template_path, 'r', encoding='utf-8') as f:
            try:
                template = jinja2.Template(f.read())
            except jinja2.TemplateError as te:
                logger.error(f"Jinja2 template error: {te}")
                return False

        try:
            content = template.render(language=language)
        except Exception as re:
            logger.error(f"Error rendering template: {re}")
            return False

        guide_file = output_dir / 'SecureCodingGuide.md'
        try:
            guide_file.write_text(content, encoding='utf-8')
        except Exception as we:
            logger.error(f"Error writing guide file: {we}")
            return False

        logger.info(f"SecureCodingGuide.md generated successfully at {guide_file}")
        return True

    except Exception as e:
        logger.exception(f"Unexpected error generating SecureCodingGuide.md: {e}")
        return False