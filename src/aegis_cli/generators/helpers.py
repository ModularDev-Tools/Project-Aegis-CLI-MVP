from pathlib import Path
import jinja2
import logging

logger = logging.getLogger(__name__)

def generate_from_template(template_name: str, output_path: Path, context: dict) -> bool:
    """
    Generates a file from a Jinja2 template.

    Args:
        template_name: The name of the template file in the 'templates' directory.
        output_path: The full path where the generated file will be saved.
        context: A dictionary of context variables to pass to the template.

    Returns:
        True if the file was generated successfully, False otherwise.
    """
    try:
        template_dir = Path(__file__).resolve().parent.parent / 'templates'
        template_file = template_dir / template_name

        if not template_file.exists():
            logger.error(f"Template file not found: {template_file}")
            return False

        with open(template_file, 'r', encoding='utf-8') as f:
            template = jinja2.Template(f.read(), undefined=jinja2.StrictUndefined)

        content = template.render(**context)

        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(content, encoding='utf-8')
        return True
    except Exception as e:
        logger.error(f"Failed to generate {output_path.name} from {template_name}: {e}", exc_info=True)
        return False