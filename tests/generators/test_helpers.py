import pytest
from pathlib import Path
from aegis_cli.generators.helpers import generate_from_template

def test_generate_from_template_success(tmp_path, mock_templates):
    """Test successful generation from a template."""
    output_file = tmp_path / "output.md"
    context = {"project_name": "MyTestProject"}
    result = generate_from_template("SECURITY.md.j2", output_file, context)
    assert result is True
    assert output_file.exists()
    assert "SECURITY: MyTestProject" in output_file.read_text()

def test_generate_from_template_creates_parent_dir(tmp_path, mock_templates):
    """Test that the parent directory for the output file is created."""
    output_file = tmp_path / "new_dir" / "output.md"
    result = generate_from_template("SECURITY.md.j2", output_file, {"project_name": "Test"})
    assert result is True
    assert output_file.exists()

def test_generate_from_template_missing_template(tmp_path):
    """Test failure when the template file does not exist."""
    result = generate_from_template("non_existent.j2", tmp_path / "out.txt", {})
    assert result is False

def test_generate_from_template_render_error(tmp_path, mock_templates):
    """Test failure when template rendering fails due to missing context."""
    result = generate_from_template("SECURITY.md.j2", tmp_path / "out.txt", {})
    assert result is False