import pytest
from pathlib import Path
from aegis_cli.detectors.javascript_detector import JavaScriptDetector

def test_javascript_detector_detects_package_json(temp_project_dir):
    """Test detection with package.json"""
    detector = JavaScriptDetector()
    (temp_project_dir / 'package.json').write_text('{}')
    assert detector.detect(temp_project_dir) == True

def test_javascript_detector_detects_yarn_lock(temp_project_dir):
    """Test detection with yarn.lock"""
    detector = JavaScriptDetector()
    (temp_project_dir / 'yarn.lock').write_text('')
    assert detector.detect(temp_project_dir) == True

def test_javascript_detector_detects_package_lock_json(temp_project_dir):
    """Test detection with package-lock.json"""
    detector = JavaScriptDetector()
    (temp_project_dir / 'package-lock.json').write_text('{}')
    assert detector.detect(temp_project_dir) == True

def test_javascript_detector_no_js_files(temp_project_dir):
    """Test no detection without JS files"""
    detector = JavaScriptDetector()
    assert detector.detect(temp_project_dir) == False

def test_javascript_detector_multiple_files(temp_project_dir):
    """Test detection with multiple JS files"""
    detector = JavaScriptDetector()
    (temp_project_dir / 'package.json').write_text('{}')
    (temp_project_dir / 'yarn.lock').write_text('')
    assert detector.detect(temp_project_dir) == True