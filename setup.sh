#!/usr/bin/env bash

# setup.sh: Installer/uninstaller for c2fetch CPU Temp Monitor
# Works on most Linux distributions with Python3 and pip/pacman/pipx

APP_NAME="c2fetch"
INSTALL_DIR="/usr/local/lib/$APP_NAME"
BIN_SCRIPT="/usr/local/bin/$APP_NAME"
RC_FILES=("~/.bashrc" "~/.zshrc" "~/.profile")

# Determine the directory of this script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PY_SCRIPT="${SCRIPT_DIR}/main.py"

# Remove lines matching pattern from shell rc files
remove_rc_lines() {
  local pattern="$1"
  for rc in "${RC_FILES[@]}"; do
    rc_file=$(eval echo "$rc")
    if [ -f "$rc_file" ]; then
      sed -i.bak "/$pattern/d" "$rc_file"
    fi
  done
}

uninstall() {
  echo "Uninstalling $APP_NAME..."
  sudo rm -f "$BIN_SCRIPT"
  sudo rm -rf "$INSTALL_DIR"
  if command -v pip3 &>/dev/null; then
    sudo pip3 uninstall -y rich psutil 2>/dev/null || true
  fi
  remove_rc_lines "alias $APP_NAME="
  echo "$APP_NAME has been uninstalled."
  exit 0
}

install() {
  echo "Installing $APP_NAME..."

  # Check for Python script
  if [ ! -f "$PY_SCRIPT" ]; then
    echo "Error: $PY_SCRIPT not found. Please place main.py in the same directory as setup.sh." 1>&2
    exit 1
  fi

  sudo mkdir -p "$INSTALL_DIR"
  sudo cp "$PY_SCRIPT" "$INSTALL_DIR/"
  sudo chmod +x "$INSTALL_DIR/$(basename "$PY_SCRIPT")"

  echo "Installing dependencies (rich, psutil)..."
  if command -v pip3 &>/dev/null; then
    sudo pip3 install rich psutil || pypkg_fail=true
  else
    pypkg_fail=true
  fi

  # Fallback for Arch Linux (pacman) or pipx
  if [ "$pypkg_fail" = true ]; then
    if command -v pacman &>/dev/null; then
      echo "Detected pacman. Installing via pacman..."
      sudo pacman -S --noconfirm python-rich python-psutil
    else
      echo "pip install failed. Consider using pipx: 'pipx install $APP_NAME' or create a venv." 1>&2
    fi
  fi

  echo "Creating executable at $BIN_SCRIPT"
  sudo tee "$BIN_SCRIPT" > /dev/null << EOF
#!/usr/bin/env bash
python3 "$INSTALL_DIR/$(basename "$PY_SCRIPT")" "\$@"
EOF
  sudo chmod +x "$BIN_SCRIPT"

  for rc in "${RC_FILES[@]}"; do
    rc_file=$(eval echo "$rc")
    if [ -f "$rc_file" ] && ! grep -q "alias $APP_NAME=" "$rc_file"; then
      echo "alias $APP_NAME='$BIN_SCRIPT'" >> "$rc_file"
      echo "Added alias to $rc_file"
    fi
  done

  echo "Installation complete. Open a new shell and run '$APP_NAME'."
}

case "$1" in
  --uninstall)
    uninstall
    ;;
  --install)
    install
    ;;
  *)
    install
    ;;
esac
