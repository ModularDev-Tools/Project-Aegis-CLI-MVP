from pathlib import Path
from .security_md import generate_security_md
from .dependabot_yml import generate_dependabot_yml
from .secure_coding_guide import generate_secure_coding_guide

def generate_security_files(project_path: Path, output_dir: Path, language: str, verbose: bool = False) -> bool:
    """Generate all security files"""
    
    try:
        # Create output directory if it doesn't exist
        output_dir.mkdir(exist_ok=True)
        
        if verbose:
            print(f"Generating files in: {output_dir}")
        
        # Generate each file
        success1 = generate_security_md(output_dir, language, project_path.name)
        success2 = generate_dependabot_yml(project_path, language)
        success3 = generate_secure_coding_guide(output_dir, language)
        
        if verbose:
            print("All security files generated successfully!")
            
        return success1 and success2 and success3
        
    except Exception as e:
        if verbose:
            print(f"Error generating security files: {e}")
        return False