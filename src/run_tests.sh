#!/bin/bash

# Detect OS for python and venv path
OS="$(uname -s)"

if [[ "$OS" == "Linux" || "$OS" == "Darwin" ]]; then
    PYTHON_CMD=python3
    ACTIVATE_SCRIPT="../.venv/bin/activate"  # relative from src/
    MENU_PACKAGE="simple-term-menu"
else
    PYTHON_CMD=python
    ACTIVATE_SCRIPT="../.venv/Scripts/activate" # relative from src/
    MENU_PACKAGE=""
fi

# Create virtual environment if it doesn't exist
if [ ! -d "../.venv" ]; then
    echo "Creating virtual environment..."
    $PYTHON_CMD -m venv ../.venv
else
    echo "Virtual environment already exists."
fi

# Activate the virtual environment
source "$ACTIVATE_SCRIPT"

# Upgrade pip and install dependencies
$PYTHON_CMD -m pip install --upgrade pip
$PYTHON_CMD -m pip install colorama art==5.7

# Install simple-term-menu only on Linux/macOS
if [ -n "$MENU_PACKAGE" ]; then
    $PYTHON_CMD -m pip install "$MENU_PACKAGE"
fi

# Run tests with unittest discover (assuming tests are in 'tests' folder inside src/)
# -s is relative to src/ (current dir), -t points to parent (project root)
$PYTHON_CMD -m unittest discover -s tests -p "*.py" -t ..

# Note: no deactivate here — just exit the script