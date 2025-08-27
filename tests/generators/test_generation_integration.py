import pytest
from pathlib import Path
from aegis_cli.generators import generate_security_files

def test_generate_security_files_success(js_project, mock_templates):
    """Test successful generation of all security files"""
    output_dir = js_project / 'security'
    output_dir.mkdir()
    
    result = generate_security_files(js_project, output_dir, 'javascript', False)
    assert result == True
    
    # Check all files were created
    assert (output_dir / 'SECURITY.md').exists()
    assert (output_dir / 'SecureCodingGuide.md').exists()
    assert (js_project / '.github' / 'dependabot.yml').exists()

def test_generate_security_files_no_output_dir(js_project, mock_templates):
    """Test generation without existing output directory"""
    output_dir = js_project / 'security'
    
    result = generate_security_files(js_project, output_dir, 'javascript', False)
    assert result == True

def test_generate_security_files_verbose(js_project, mock_templates, capsys):
    """Test verbose generation"""
    output_dir = js_project / 'security'
    output_dir.mkdir()
    
    result = generate_security_files(js_project, output_dir, 'javascript', True)
    assert result == True
    
    captured = capsys.readouterr()
    assert 'Generating files in:' in captured.out

def test_generate_security_files_partial_failure(js_project, mock_templates):
    """Test behavior when some generators fail"""
    output_dir = js_project / 'security'
    output_dir.mkdir()
    
    # Remove one template to cause partial failure
    template_path = Path(__file__).parent.parent.parent / 'templates' / 'SECURITY.md.j2'
    if template_path.exists():
        template_path.unlink()
    
    result = generate_security_files(js_project, output_dir, 'javascript', False)
    assert result == False  # Should fail overall if any generator fails