import pytest
from pathlib import Path
from aegis_cli.generators.dependabot_yml import generate_dependabot_yml

def test_generate_dependabot_yml_javascript(temp_project_dir, mock_templates):
    """Test dependabot.yml generation for JavaScript"""
    result = generate_dependabot_yml(temp_project_dir, 'javascript')
    assert result == True
    
    dependabot_file = temp_project_dir / '.github' / 'dependabot.yml'
    assert dependabot_file.exists()
    assert 'dependabot: npm' in dependabot_file.read_text()

def test_generate_dependabot_yml_python(temp_project_dir, mock_templates):
    """Test dependabot.yml generation for Python"""
    result = generate_dependabot_yml(temp_project_dir, 'python')
    assert result == True
    
    dependabot_file = temp_project_dir / '.github' / 'dependabot.yml'
    assert dependabot_file.exists()
    assert 'dependabot: pip' in dependabot_file.read_text()

def test_generate_dependabot_yml_creates_github_dir(temp_project_dir, mock_templates):
    """Test that .github directory is created if it doesn't exist"""
    result = generate_dependabot_yml(temp_project_dir, 'javascript')
    assert result == True
    assert (temp_project_dir / '.github').exists()

def test_generate_dependabot_yml_missing_template(temp_project_dir):
    """Test dependabot.yml generation with missing template"""
    template_path = Path(__file__).parent.parent.parent / 'templates' / 'dependabot.yml.j2'
    if template_path.exists():
        template_path.unlink()

    result = generate_dependabot_yml(temp_project_dir, 'javascript')
    assert result == False