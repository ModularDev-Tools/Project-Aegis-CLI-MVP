import logging
from .base_detector import LanguageDetector
from pathlib import Path

logger = logging.getLogger(__name__)

class JavaScriptDetector(LanguageDetector):
    def detect(self, project_path: Path) -> bool:
        js_files = [
            'package.json',
            'yarn.lock',
            'package-lock.json',
            'node_modules'
        ]
        try:
            result = any((project_path / file).exists() for file in js_files)
            logger.info(f"Detection result for {project_path}: {result}")
            return result
        except Exception as e:
            logger.error(f"Error detecting JavaScript files in {project_path}: {e}", exc_info=True)
            return False