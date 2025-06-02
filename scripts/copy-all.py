#!/usr/bin/env python3
"""
Simple script to recursively list all git-tracked files and print their contents to full-repo.txt
"""

import subprocess
import sys
from pathlib import Path


def get_git_files():
    """Get list of all git-tracked files"""
    try:
        result = subprocess.run(
            ["git", "ls-files"],
            capture_output=True,
            text=True,
            check=True
        )
        return [line.strip() for line in result.stdout.splitlines() if line.strip()]
    except subprocess.CalledProcessError as e:
        print(f"Error getting git files: {e}")
        sys.exit(1)


def read_file_content(file_path):
    """Read file content, handling binary files gracefully"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except UnicodeDecodeError:
        return f"[Binary file: {file_path}]"
    except Exception as e:
        return f"[Error reading {file_path}: {e}]"


def main():
    """Main function to generate full-repo.txt"""
    print("Getting git-tracked files...")
    git_files = get_git_files()
    
    print(f"Found {len(git_files)} files")
    
    output_path = Path("full-repo.txt")
    
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write("# Full Repository Contents\n\n")
        
        for file_path in git_files:
            print(f"Processing: {file_path}")
            
            # Write file header
            output_file.write(f"## {file_path}\n\n")
            
            # Get file extension for syntax highlighting
            ext = Path(file_path).suffix.lstrip('.')
            if ext:
                output_file.write(f"```{ext}\n")
            else:
                output_file.write("```\n")
            
            # Write file content
            content = read_file_content(file_path)
            output_file.write(content)
            
            # Ensure content ends with newline
            if content and not content.endswith('\n'):
                output_file.write('\n')
            
            output_file.write("```\n\n")
    
    print(f"Generated {output_path}")


if __name__ == "__main__":
    main()