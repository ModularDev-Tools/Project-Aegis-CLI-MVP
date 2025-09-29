import pytest
import tempfile
import shutil
from pathlib import Path
from unittest.mock import Mock, patch
import subprocess

@pytest.fixture
def temp_project_dir():
    """Create a temporary project directory for testing"""
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        yield temp_path

@pytest.fixture
def git_repo(temp_project_dir):
    """Create a temporary git repository."""
    git_dir = temp_project_dir
    # Change to the temp dir to run git init
    subprocess.run(["git", "init"], cwd=git_dir, check=True, capture_output=True)
    return git_dir


@pytest.fixture
def js_project(temp_project_dir):
    """Create a JavaScript project structure"""
    (temp_project_dir / 'package.json').write_text('{}')
    return temp_project_dir

@pytest.fixture
def java_project(temp_project_dir):
    """Create a Java project structure"""
    (temp_project_dir / 'pom.xml').write_text('<project></project>')
    return temp_project_dir

@pytest.fixture
def rust_project(temp_project_dir):
    """Create a Rust project structure"""
    (temp_project_dir / 'Cargo.toml').write_text('[package]')
    return temp_project_dir

@pytest.fixture
def python_project(temp_project_dir):
    """Create a Python project structure"""
    (temp_project_dir / 'requirements.txt').write_text('')
    return temp_project_dir

@pytest.fixture
def empty_project(temp_project_dir):
    """Create an empty project structure"""
    return temp_project_dir

@pytest.fixture
def mock_templates():
    """Mock template files for testing"""
    templates_dir = Path(__file__).parent.parent / 'src' / 'aegis_cli' / 'templates'
    templates_dir.mkdir(exist_ok=True, parents=True)
    
    original_contents = {}
    mock_files = {
        'SECURITY.md.j2': "SECURITY: {{ project_name }}",
        'dependabot.yml.j2': 'dependabot: {{ package_ecosystem }}',
        'SecureCodingGuide.md.j2': "Guide: {{ language }}",
    }

    for filename, mock_content in mock_files.items():
        file_path = templates_dir / filename
        if file_path.exists():
            original_contents[file_path] = file_path.read_text(encoding='utf-8')
        file_path.write_text(mock_content, encoding='utf-8')
    
    yield
    
    # Restore original templates
    for file_path, original_content in original_contents.items():
        file_path.write_text(original_content, encoding='utf-8')
    
    # Remove any files that were created by the mock
    for filename in mock_files:
        file_path = templates_dir / filename
        if file_path not in original_contents:
            file_path.unlink(missing_ok=True)