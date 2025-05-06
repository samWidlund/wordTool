#!/bin/bash

SCRIPT_DIR="$(dirname "$0")"
VENV_PYTHON="$SCRIPT_DIR/venv/bin/python"
SCRIPT_FILE="$SCRIPT_DIR/script.py"

gnome-terminal -- bash -c "$VENV_PYTHON $SCRIPT_FILE; echo; read -p 'press [Enter] to close'"