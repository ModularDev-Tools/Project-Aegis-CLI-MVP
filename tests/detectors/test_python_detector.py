import pytest
from pathlib import Path
from aegis_cli.detectors.python_detector import PythonDetector

def test_python_detector_detects_requirements_txt(temp_project_dir):
    """Test detection with requirements.txt"""
    detector = PythonDetector()
    (temp_project_dir / 'requirements.txt').write_text('')
    assert detector.detect(temp_project_dir) == True

def test_python_detector_detects_pyproject_toml(temp_project_dir):
    """Test detection with pyproject.toml"""
    detector = PythonDetector()
    (temp_project_dir / 'pyproject.toml').write_text('')
    assert detector.detect(temp_project_dir) == True

def test_python_detector_detects_setup_py(temp_project_dir):
    """Test detection with setup.py"""
    detector = PythonDetector()
    (temp_project_dir / 'setup.py').write_text('')
    assert detector.detect(temp_project_dir) == True

def test_python_detector_no_python_files(temp_project_dir):
    """Test no detection without Python files"""
    detector = PythonDetector()
    assert detector.detect(temp_project_dir) == False

def test_python_detector_multiple_files(temp_project_dir):
    """Test detection with multiple Python files"""
    detector = PythonDetector()
    (temp_project_dir / 'requirements.txt').write_text('')
    (temp_project_dir / 'setup.py').write_text('')
    assert detector.detect(temp_project_dir) == True