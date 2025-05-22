#!/usr/bin/env bash
APP="c2fetch"
BIN="/usr/local/bin/$APP"
LIB="/usr/local/lib/$APP"
PY="$(cd "$(dirname "$0")" && pwd)/main.py"
RCS=(~/.bashrc ~/.zshrc ~/.profile)

uninstall() {
  echo "Uninstalling $APP..."
  sudo rm -f "$BIN" && sudo rm -rf "$LIB"
  command -v pip3 &>/dev/null && sudo pip3 uninstall -y rich psutil 2>/dev/null
  for rc in "${RCS[@]}"; do [ -f "$rc" ] && sed -i.bak "/alias $APP=/d" "$rc"; done
  echo "$APP removed."; exit
}

install() {
  [ -f "$PY" ] || { echo "main.py not found."; exit 1; }
  echo "Installing $APP..."
  sudo mkdir -p "$LIB" && sudo cp "$PY" "$LIB/main.py" && sudo chmod +x "$LIB/main.py"
  if ! sudo pip3 install rich psutil 2>/dev/null; then
    command -v pacman &>/dev/null && sudo pacman -S --noconfirm python-rich python-psutil || \
    echo "Try pipx or a virtualenv."
  fi
  echo -e "#!/usr/bin/env bash\npython3 \"$LIB/main.py\" \"\$@\"" | sudo tee "$BIN" >/dev/null
  sudo chmod +x "$BIN"
  for rc in "${RCS[@]}"; do grep -q "alias $APP=" "$rc" 2>/dev/null || echo "alias $APP='$BIN'" >> "$rc"; done
  echo "Done. Run '$APP' in new shell."
}

[[ "$1" == "--uninstall" ]] && uninstall || install
