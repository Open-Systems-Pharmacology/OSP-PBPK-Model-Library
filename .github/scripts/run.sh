#!/bin/bash
# Quick start script for GitHub Projects issue management
# This script helps set up and run the GitHub Projects manager

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "GitHub Projects Issue Manager - Setup & Quick Start"
echo "===================================================="
echo ""

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: python3 is not installed"
    echo "Please install Python 3.6 or later"
    exit 1
fi

echo "✓ Python 3 is available"

# Check if pip is available
if ! command -v pip3 &> /dev/null; then
    echo "⚠️  Warning: pip3 is not installed"
    echo "You may need to install the 'requests' library manually"
else
    echo "✓ pip3 is available"
    
    # Install requirements
    echo ""
    echo "Installing required Python packages..."
    pip3 install -q -r "$SCRIPT_DIR/requirements.txt"
    echo "✓ Requirements installed"
fi

# Check for GitHub token
echo ""
if [ -z "$GITHUB_TOKEN" ]; then
    echo "⚠️  GITHUB_TOKEN environment variable is not set"
    echo ""
    echo "To use this script, you need to:"
    echo "1. Create a GitHub Personal Access Token at:"
    echo "   https://github.com/settings/tokens"
    echo ""
    echo "2. Grant the following scopes:"
    echo "   - repo (full control)"
    echo "   - project (read and write)"
    echo ""
    echo "3. Export the token:"
    echo "   export GITHUB_TOKEN=your_token_here"
    echo ""
    echo "4. Run this script again"
    echo ""
    exit 1
else
    echo "✓ GITHUB_TOKEN is set"
fi

# Show menu
echo ""
echo "What would you like to do?"
echo "1) Preview issues with 'No Status' (recommended first)"
echo "2) Move issues from 'No Status' to V12.3 project"
echo "3) Exit"
echo ""
read -p "Enter your choice (1-3): " choice

case $choice in
    1)
        echo ""
        echo "Running preview mode..."
        echo "===================================================="
        python3 "$SCRIPT_DIR/github_projects_manager.py" preview
        ;;
    2)
        echo ""
        echo "Running move mode..."
        echo "===================================================="
        python3 "$SCRIPT_DIR/github_projects_manager.py" move
        ;;
    3)
        echo "Exiting..."
        exit 0
        ;;
    *)
        echo "Invalid choice"
        exit 1
        ;;
esac
