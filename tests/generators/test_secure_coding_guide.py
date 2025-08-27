import pytest
from pathlib import Path
from aegis_cli.generators.secure_coding_guide import generate_secure_coding_guide

def test_generate_secure_coding_guide_success(temp_project_dir, mock_templates):
    """Test successful SecureCodingGuide.md generation"""
    output_dir = temp_project_dir / 'security'
    output_dir.mkdir()
    
    result = generate_secure_coding_guide(output_dir, 'javascript')
    assert result == True
    
    guide_file = output_dir / 'SecureCodingGuide.md'
    assert guide_file.exists()
    assert 'Guide: javascript' in guide_file.read_text(encoding='utf-8')

def test_generate_secure_coding_guide_no_output_dir(temp_project_dir, mock_templates):
    """Test SecureCodingGuide.md generation without existing output directory"""
    output_dir = temp_project_dir / 'security'
    
    result = generate_secure_coding_guide(output_dir, 'javascript')
    assert result == False

def test_generate_secure_coding_guide_missing_template(temp_project_dir):
    """Test SecureCodingGuide.md generation with missing template"""
    output_dir = temp_project_dir / 'security'
    output_dir.mkdir()
    
    template_path = Path(__file__).parent.parent.parent / 'templates' / 'SecureCodingGuide.md.j2'
    if template_path.exists():
        template_path.unlink()

    result = generate_secure_coding_guide(output_dir, 'javascript')
    assert result == False