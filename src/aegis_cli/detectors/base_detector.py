import logging
from pathlib import Path
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)

class LanguageDetector(ABC):
    """Abstract base class for language detectors"""

    @abstractmethod
    def detect(self, project_path: Path) -> bool:
        """
        Detect if this language is present in the project.

        Returns:
            bool: True if language is detected, False otherwise.

        Raises:
            Exception: If an error occurs during detection.
        """