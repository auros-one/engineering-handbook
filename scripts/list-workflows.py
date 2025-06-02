#!/usr/bin/env python3
"""
Workflow Discovery Script

Extracts metadata from workflow files to help AI agents select the appropriate workflow
based on task description, keywords, and context.
"""

import yaml
from pathlib import Path
from typing import List, Dict, Any


def extract_workflow_metadata(workflows_dir: str = "agent-guidance/workflows") -> List[Dict[str, Any]]:
    """Extract YAML frontmatter metadata from all workflow files."""
    workflows_path = Path(workflows_dir)
    workflows = []
    
    for file_path in workflows_path.glob("*.md"):
        # Skip README files
        if file_path.name.lower().startswith('readme'):
            continue
            
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Extract YAML frontmatter
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    metadata = yaml.safe_load(parts[1])
                    if metadata:
                        metadata['file'] = file_path.name
                        metadata['path'] = str(file_path)
                        workflows.append(metadata)
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            continue
    
    return workflows


def find_matching_workflows(query: str, workflows: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Find workflows that match the given query based on triggers and description."""
    query_lower = query.lower()
    matches = []
    
    for workflow in workflows:
        score = 0
        
        # Check triggers
        triggers = workflow.get('triggers', [])
        for trigger in triggers:
            if trigger.lower() in query_lower:
                score += 2
        
        # Check description
        description = workflow.get('description', '').lower()
        if any(word in description for word in query_lower.split()):
            score += 1
            
        # Check name
        name = workflow.get('name', '').lower()
        if any(word in name for word in query_lower.split()):
            score += 1
        
        if score > 0:
            workflow_match = workflow.copy()
            workflow_match['match_score'] = score
            matches.append(workflow_match)
    
    # Sort by match score
    return sorted(matches, key=lambda x: x['match_score'], reverse=True)


def format_workflow_list(workflows: List[Dict[str, Any]], include_details: bool = True) -> str:
    """Format workflows into a readable markdown list."""
    if not workflows:
        return "No workflows found.\n"
    
    output = "# Available Workflows\n\n"
    
    for wf in workflows:
        output += f"## {wf['name']} (`{wf['file']}`)\n"
        output += f"**Description:** {wf['description']}\n"
        
        if include_details and wf.get('triggers'):
            output += f"**Triggers:** {', '.join(wf['triggers'])}\n"
        
        output += "\n"
    
    return output


def format_workflow_selection(query: str, matches: List[Dict[str, Any]]) -> str:
    """Format workflow selection results for a specific query."""
    if not matches:
        return f"No workflows found matching: '{query}'\n\nAvailable workflows:\n" + \
               format_workflow_list(extract_workflow_metadata(), include_details=False)
    
    output = f"# Workflow Selection for: '{query}'\n\n"
    
    if len(matches) == 1:
        output += "## Recommended Workflow\n\n"
    else:
        output += "## Recommended Workflows (ranked by relevance)\n\n"
    
    for i, wf in enumerate(matches[:3], 1):  # Show top 3 matches
        output += f"### {i}. {wf['name']} (`{wf['file']}`)\n"
        output += f"**Description:** {wf['description']}\n"
        output += f"**Match Score:** {wf['match_score']}\n\n"
    
    return output


def main():
    """Main CLI interface."""
    import sys
    
    if len(sys.argv) < 2:
        # List all workflows
        workflows = extract_workflow_metadata()
        print(format_workflow_list(workflows))
    elif sys.argv[1] == "--query" and len(sys.argv) > 2:
        # Find workflows matching query
        query = " ".join(sys.argv[2:])
        workflows = extract_workflow_metadata()
        matches = find_matching_workflows(query, workflows)
        print(format_workflow_selection(query, matches))
    elif sys.argv[1] == "--simple":
        # Simple list without details
        workflows = extract_workflow_metadata()
        print(format_workflow_list(workflows, include_details=False))
    else:
        print("Usage:")
        print("  python list-workflows.py                    # List all workflows")
        print("  python list-workflows.py --simple           # Simple list")
        print("  python list-workflows.py --query <text>     # Find matching workflows")
        print()
        print("Examples:")
        print("  python list-workflows.py --query 'implement new feature'")
        print("  python list-workflows.py --query 'styling UI design'")
        print("  python list-workflows.py --query 'product roadmap planning'")


if __name__ == "__main__":
    main()