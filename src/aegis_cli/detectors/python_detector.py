import logging
from .base_detector import LanguageDetector
from pathlib import Path

logger = logging.getLogger(__name__)

class PythonDetector(LanguageDetector):
    def detect(self, project_path: Path) -> bool:
        python_files = [
            'requirements.txt',
            'pyproject.toml',
            'setup.py',
            'Pipfile',
            'poetry.lock',
            'setup.cfg'
        ]
        try:
            for file in python_files:
                file_path = project_path / file
                if file_path.exists():
                    logger.info(f"Detected Python file: {file_path}")
                    return True
            logger.info(f"No Python-specific files found in {project_path}")
            return False
        except Exception as e:
            logger.error(f"Error while detecting Python files in {project_path}: {e}")
            return False