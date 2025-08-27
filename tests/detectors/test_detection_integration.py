import pytest
from pathlib import Path
from aegis_cli.detectors import detect_language

def test_detect_language_javascript(js_project):
    """Test language detection for JavaScript"""
    result = detect_language(js_project)
    assert result == 'javascript'

def test_detect_language_python(python_project):
    """Test language detection for Python"""
    result = detect_language(python_project)
    assert result == 'python'

def test_detect_language_none(empty_project):
    """Test language detection returns None for unknown projects"""
    result = detect_language(empty_project)
    assert result is None

def test_detect_language_verbose(js_project, capsys):
    """Test verbose language detection"""
    result = detect_language(js_project, verbose=True)
    captured = capsys.readouterr()
    assert result == 'javascript'
    assert 'Detected javascript project' in captured.out

def test_detect_language_priority(js_project, python_project):
    """Test detection priority (first match wins)"""
    # Create a project with both JS and Python files
    (js_project / 'requirements.txt').write_text('')
    result = detect_language(js_project)
    assert result == 'javascript'  # JS should be detected first