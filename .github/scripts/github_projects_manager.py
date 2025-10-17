#!/usr/bin/env python3
"""
Script to manage GitHub Projects - preview and move issues between columns/projects.

This script requires a GitHub Personal Access Token with the following scopes:
- repo
- project (read:project and write:project)

Usage:
  # Preview issues with "No Status"
  python3 github_projects_manager.py preview
  
  # Move issues from "No Status" to project V12.3
  python3 github_projects_manager.py move

Set the GITHUB_TOKEN environment variable before running:
  export GITHUB_TOKEN=your_token_here
"""

import os
import json
import sys
import requests
from typing import List, Dict, Any, Optional

class GitHubProjectsManager:
    def __init__(self, token: str, org: str, repo: str):
        self.token = token
        self.org = org
        self.repo = repo
        self.api_url = "https://api.github.com/graphql"
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
    
    def execute_query(self, query: str, variables: Dict[str, Any] = None) -> Dict[str, Any]:
        """Execute a GraphQL query."""
        payload = {"query": query}
        if variables:
            payload["variables"] = variables
        
        response = requests.post(self.api_url, json=payload, headers=self.headers)
        
        if response.status_code != 200:
            print(f"Error: HTTP {response.status_code}")
            print(response.text)
            sys.exit(1)
        
        result = response.json()
        
        if "errors" in result:
            print("GraphQL Errors:")
            for error in result["errors"]:
                print(f"  - {error.get('message', 'Unknown error')}")
            sys.exit(1)
        
        return result
    
    def get_organization_projects(self) -> List[Dict[str, Any]]:
        """Get all projects for an organization using GraphQL."""
        query = """
        query($org: String!) {
          organization(login: $org) {
            projectsV2(first: 100) {
              nodes {
                id
                title
                number
                url
                shortDescription
              }
            }
          }
        }
        """
        
        variables = {"org": self.org}
        result = self.execute_query(query, variables)
        
        return result.get('data', {}).get('organization', {}).get('projectsV2', {}).get('nodes', [])
    
    def get_project_fields(self, project_id: str) -> List[Dict[str, Any]]:
        """Get all fields in a project."""
        query = """
        query($projectId: ID!) {
          node(id: $projectId) {
            ... on ProjectV2 {
              fields(first: 20) {
                nodes {
                  ... on ProjectV2Field {
                    id
                    name
                  }
                  ... on ProjectV2SingleSelectField {
                    id
                    name
                    options {
                      id
                      name
                    }
                  }
                }
              }
            }
          }
        }
        """
        
        variables = {"projectId": project_id}
        result = self.execute_query(query, variables)
        
        return result.get('data', {}).get('node', {}).get('fields', {}).get('nodes', [])
    
    def get_project_items(self, project_id: str) -> List[Dict[str, Any]]:
        """Get all items in a project including their status field values."""
        query = """
        query($projectId: ID!, $cursor: String) {
          node(id: $projectId) {
            ... on ProjectV2 {
              items(first: 100, after: $cursor) {
                pageInfo {
                  hasNextPage
                  endCursor
                }
                nodes {
                  id
                  content {
                    ... on Issue {
                      number
                      title
                      url
                      state
                    }
                  }
                  fieldValues(first: 10) {
                    nodes {
                      ... on ProjectV2ItemFieldSingleSelectValue {
                        name
                        field {
                          ... on ProjectV2SingleSelectField {
                            name
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
        """
        
        all_items = []
        cursor = None
        
        while True:
            variables = {'projectId': project_id}
            if cursor:
                variables['cursor'] = cursor
                
            result = self.execute_query(query, variables)
            
            project_data = result.get('data', {}).get('node', {})
            items_data = project_data.get('items', {})
            nodes = items_data.get('nodes', [])
            all_items.extend(nodes)
            
            page_info = items_data.get('pageInfo', {})
            if not page_info.get('hasNextPage', False):
                break
            cursor = page_info.get('endCursor')
        
        return all_items
    
    def add_item_to_project(self, project_id: str, content_id: str) -> str:
        """Add an issue to a project."""
        mutation = """
        mutation($projectId: ID!, $contentId: ID!) {
          addProjectV2ItemById(input: {projectId: $projectId, contentId: $contentId}) {
            item {
              id
            }
          }
        }
        """
        
        variables = {
            "projectId": project_id,
            "contentId": content_id
        }
        
        result = self.execute_query(mutation, variables)
        return result.get('data', {}).get('addProjectV2ItemById', {}).get('item', {}).get('id')
    
    def update_item_field(self, project_id: str, item_id: str, field_id: str, option_id: str):
        """Update a field value for a project item."""
        mutation = """
        mutation($projectId: ID!, $itemId: ID!, $fieldId: ID!, $value: ProjectV2FieldValue!) {
          updateProjectV2ItemFieldValue(
            input: {
              projectId: $projectId
              itemId: $itemId
              fieldId: $fieldId
              value: $value
            }
          ) {
            projectV2Item {
              id
            }
          }
        }
        """
        
        variables = {
            "projectId": project_id,
            "itemId": item_id,
            "fieldId": field_id,
            "value": {
                "singleSelectOptionId": option_id
            }
        }
        
        self.execute_query(mutation, variables)
    
    def get_issue_id(self, issue_number: int) -> str:
        """Get the global ID of an issue."""
        query = """
        query($owner: String!, $repo: String!, $issueNumber: Int!) {
          repository(owner: $owner, name: $repo) {
            issue(number: $issueNumber) {
              id
            }
          }
        }
        """
        
        variables = {
            "owner": self.org,
            "repo": self.repo,
            "issueNumber": issue_number
        }
        
        result = self.execute_query(query, variables)
        return result.get('data', {}).get('repository', {}).get('issue', {}).get('id')
    
    def preview_issues_to_move(self):
        """Preview which issues would be moved from 'No Status' to project V12.3."""
        print(f"Fetching projects for organization: {self.org}")
        projects = self.get_organization_projects()
        
        print(f"\nFound {len(projects)} projects:")
        for project in projects:
            desc = f" - {project.get('shortDescription', '')}" if project.get('shortDescription') else ""
            print(f"  - {project['title']} (#{project['number']}){desc}")
        
        # Find V12.3 project
        v12_3_project = None
        for project in projects:
            if 'V12.3' in project['title'] or project['title'] == 'V12.3':
                v12_3_project = project
                break
        
        if not v12_3_project:
            print("\n❌ Could not find project 'V12.3'")
            print("Available projects:")
            for project in projects:
                print(f"  - {project['title']}")
            return None
        
        print(f"\n✓ Found target project: {v12_3_project['title']}")
        print(f"  URL: {v12_3_project['url']}")
        
        # Search for issues with "No Status"
        print("\n" + "="*60)
        print("Searching for issues with 'No Status' across all projects...")
        print("="*60)
        
        issues_with_no_status = []
        
        for project in projects:
            print(f"\nChecking project: {project['title']}")
            items = self.get_project_items(project['id'])
            print(f"  Found {len(items)} items in project")
            
            for item in items:
                content = item.get('content', {})
                if not content:
                    continue
                    
                # Check if this item has "No Status" status
                field_values = item.get('fieldValues', {}).get('nodes', [])
                for field_value in field_values:
                    field = field_value.get('field', {})
                    field_name = field.get('name', '')
                    value_name = field_value.get('name', '')
                    
                    if field_name == 'Status' and value_name == 'No Status':
                        issues_with_no_status.append({
                            'project': project['title'],
                            'project_id': project['id'],
                            'item_id': item['id'],
                            'issue_number': content.get('number'),
                            'issue_title': content.get('title'),
                            'issue_url': content.get('url'),
                            'issue_state': content.get('state')
                        })
                        break
        
        if not issues_with_no_status:
            print("\n✓ No issues found with 'No Status' status")
            return None
        
        print("\n" + "="*60)
        print(f"PREVIEW: Found {len(issues_with_no_status)} issue(s) with 'No Status'")
        print("="*60)
        
        for issue in issues_with_no_status:
            print(f"\nIssue #{issue['issue_number']}: {issue['issue_title']}")
            print(f"  Current Project: {issue['project']}")
            print(f"  State: {issue['issue_state']}")
            print(f"  URL: {issue['issue_url']}")
        
        print("\n" + "="*60)
        print(f"These issues would be moved to project: {v12_3_project['title']}")
        print("="*60)
        
        return {
            'target_project': v12_3_project,
            'issues': issues_with_no_status
        }
    
    def move_issues_to_project(self, preview_data: Dict[str, Any]):
        """Move issues from 'No Status' to project V12.3."""
        if not preview_data:
            print("No issues to move")
            return
        
        target_project = preview_data['target_project']
        issues = preview_data['issues']
        
        print(f"\n{'='*60}")
        print(f"Moving {len(issues)} issues to project: {target_project['title']}")
        print(f"{'='*60}\n")
        
        # Get fields for the target project
        fields = self.get_project_fields(target_project['id'])
        status_field = None
        
        for field in fields:
            if field.get('name') == 'Status':
                status_field = field
                break
        
        if not status_field:
            print("❌ Could not find 'Status' field in target project")
            return
        
        moved_count = 0
        failed_count = 0
        
        for issue in issues:
            issue_num = issue['issue_number']
            issue_title = issue['issue_title']
            
            try:
                print(f"Processing Issue #{issue_num}: {issue_title}")
                
                # Get the issue's global ID
                issue_id = self.get_issue_id(issue_num)
                
                # Add the issue to the target project
                item_id = self.add_item_to_project(target_project['id'], issue_id)
                
                print(f"  ✓ Added to project {target_project['title']}")
                moved_count += 1
                
            except Exception as e:
                print(f"  ❌ Failed: {e}")
                failed_count += 1
        
        print(f"\n{'='*60}")
        print(f"Summary:")
        print(f"  Successfully moved: {moved_count}")
        print(f"  Failed: {failed_count}")
        print(f"{'='*60}")


def main():
    # Repository information
    ORG = 'Open-Systems-Pharmacology'
    REPO = 'OSP-PBPK-Model-Library'
    
    # Get GitHub token
    token = os.environ.get('GITHUB_TOKEN')
    if not token:
        print("Error: GITHUB_TOKEN environment variable is not set")
        print("\nTo run this script:")
        print("1. Create a GitHub Personal Access Token with 'repo' and 'project' scopes")
        print("2. Set the environment variable: export GITHUB_TOKEN=your_token_here")
        print("3. Run the script again")
        sys.exit(1)
    
    # Create manager
    manager = GitHubProjectsManager(token, ORG, REPO)
    
    # Determine mode
    mode = sys.argv[1] if len(sys.argv) > 1 else "preview"
    
    if mode == "preview":
        print("GitHub Projects Manager - Preview Mode")
        print("="*60)
        manager.preview_issues_to_move()
    elif mode == "move":
        print("GitHub Projects Manager - Move Mode")
        print("="*60)
        
        # First do a preview
        preview_data = manager.preview_issues_to_move()
        
        if preview_data:
            print("\n" + "="*60)
            response = input("Do you want to proceed with moving these issues? (yes/no): ")
            if response.lower() in ['yes', 'y']:
                manager.move_issues_to_project(preview_data)
            else:
                print("Operation cancelled")
    else:
        print(f"Unknown mode: {mode}")
        print("Usage: python3 github_projects_manager.py [preview|move]")
        sys.exit(1)


if __name__ == '__main__':
    main()
