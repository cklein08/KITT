#!/bin/bash

# KITT Setup Script
# Adds the `kitt` terminal command so you can launch KITT from anywhere

set -e

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

print_color() { printf "${1}${2}${NC}\n"; }
print_header() {
    echo ""
    print_color "$CYAN" "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    print_color "$CYAN" "KITT - Knight Rider Intelligent Technology Team"
    print_color "$CYAN" "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
}

# Get KITT directory (where this script lives, parent of .kitt)
KITT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

print_header
echo "This script adds the 'kitt' command to your shell."
echo "After setup, type 'kitt' from any directory to launch KITT."
echo ""

# Detect shell and config file
if [ -n "$ZSH_VERSION" ] || [ "$SHELL" = "/bin/zsh" ] || [ "$SHELL" = "/usr/bin/zsh" ]; then
    SHELL_RC="$HOME/.zshrc"
elif [ -n "$BASH_VERSION" ] || [ "$SHELL" = "/bin/bash" ] || [ "$SHELL" = "/usr/bin/bash" ]; then
    SHELL_RC="$HOME/.bashrc"
    [ ! -f "$SHELL_RC" ] && SHELL_RC="$HOME/.profile"
else
    SHELL_RC="$HOME/.profile"
fi

# Check if kitt function already exists
if grep -q "kitt()" "$SHELL_RC" 2>/dev/null; then
    print_color "$YELLOW" "The 'kitt' command already exists in $SHELL_RC"
    echo "To update it, remove the existing 'kitt()' function and run this script again."
    exit 0
fi

# Ask for KITT workspace path (default: current KITT dir)
echo "Where is your KITT workspace?"
echo "  (Press Enter to use: $KITT_DIR)"
read -r USER_PATH
WORKSPACE_PATH="${USER_PATH:-$KITT_DIR}"
WORKSPACE_PATH="${WORKSPACE_PATH/#\~/$HOME}"

# Append kitt function
KITT_FUNC='
# KITT - Knight Rider Intelligent Technology Team
kitt() {
    cd "'"$WORKSPACE_PATH"'" && claude
}
'

echo "" >> "$SHELL_RC"
echo "$KITT_FUNC" >> "$SHELL_RC"

print_color "$GREEN" "Done! The 'kitt' command has been added to $SHELL_RC"
echo ""
echo "To use it:"
echo "  1. Open a new terminal (or run: source $SHELL_RC)"
echo "  2. Type: kitt"
echo ""
echo "KITT will open in your workspace at: $WORKSPACE_PATH"
echo ""
