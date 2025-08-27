import pytest
from pathlib import Path
from aegis_cli.generators.security_md import generate_security_md

def test_generate_security_md_success(temp_project_dir, mock_templates):
    """Test successful SECURITY.md generation"""
    output_dir = temp_project_dir / 'security'
    output_dir.mkdir()
    
    result = generate_security_md(output_dir, 'javascript', 'test-project')
    assert result == True
    
    security_file = output_dir / 'SECURITY.md'
    assert security_file.exists()
    assert 'SECURITY: test-project' in security_file.read_text()

def test_generate_security_md_no_output_dir(temp_project_dir, mock_templates):
    """Test SECURITY.md generation without existing output directory"""
    output_dir = temp_project_dir / 'security'
    
    result = generate_security_md(output_dir, 'javascript', 'test-project')
    assert result == False  # Should fail because directory doesn't exist

def test_generate_security_md_missing_template(temp_project_dir):
    """Test SECURITY.md generation with missing template"""
    output_dir = temp_project_dir / 'security'
    output_dir.mkdir()
    
    template_path = Path(__file__).parent.parent.parent / 'templates' / 'SECURITY.md.j2'
    if template_path.exists():
        template_path.unlink()

    result = generate_security_md(output_dir, 'javascript', 'test-project')
    assert result == False  # Should fail without template

def test_generate_security_md_default_project_name(temp_project_dir, mock_templates):
    """Test SECURITY.md generation with default project name"""
    output_dir = temp_project_dir / 'security'
    output_dir.mkdir()
    
    result = generate_security_md(output_dir, 'javascript', None)
    assert result == True
    
    security_file = output_dir / 'SECURITY.md'
    assert 'SECURITY: Our Project' in security_file.read_text()