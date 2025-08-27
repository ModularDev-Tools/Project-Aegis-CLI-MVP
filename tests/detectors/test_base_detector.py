import pytest
from aegis_cli.detectors.base_detector import LanguageDetector

def test_base_detector_abstract():
    """Test that base detector is abstract"""
    with pytest.raises(TypeError):
        LanguageDetector()  # Should raise error since it's abstract

def test_base_detector_abstract_method():
    """Test that detect method is abstract"""
    class ConcreteDetector(LanguageDetector):
        def detect(self, project_path):
            return True
    
    detector = ConcreteDetector()
    assert detector.detect(None) == True