<div align="center">
<h1>C2fetch</h1>

A lightweight, real-time CPU temperature monitor with customizable ASCII art. Powered by [psutil](https://pypi.org/project/psutil/) and [rich](https://github.com/Textualize/rich).

  <img src="https://raw.githubusercontent.com/quietpulse/c2fetch/refs/heads/main/Pasted_image.png" alt="C2fetch Screenshot" width="600">
</div>

## Features
- Real-time CPU temperature monitoring
- Customizable ASCII art banner
- Color-coded temperature display based on thresholds
- Cross-platform compatibility (primarily tested on Linux)

## Requirements
- Python 3.6 or higher
- Python packages: `rich` and `psutil` (install via `pip install rich psutil`)
- Unix-like operating system (e.g., Linux)

## Installation

### Automated Installation (Arch Linux)
1. Clone the repository:
   ```
   git clone https://github.com/quietpulse/c2fetch.git
   cd c2fetch
   ```
2. Make the setup script executable and run it:
   ```
   chmod +x setup.sh
   ./setup.sh
   ```
   - This installs dependencies and sets up the tool.
   - To uninstall: `./setup.sh --uninstall`

### Manual Installation (Ubuntu, Fedora, etc.)
1. Clone the repository:
   ```
   git clone https://github.com/quietpulse/c2fetch.git
   cd c2fetch
   ```
2. Install system dependencies:
   - **Debian/Ubuntu**:
     ```
     sudo apt update && sudo apt install -y python3-pip
     ```
   - **Fedora**:
     ```
     sudo dnf install -y python3-pip
     ```
   - **Arch Linux (alternative)**:
     ```
     sudo pacman -Sy python-pip
     ```
3. Install Python packages:
   ```
   pip3 install --user rich psutil
   ```
4. Create an alias for easy access (add to `~/.bashrc` or your shell configuration):
   ```
   echo "alias c2fetch='python3 $(pwd)/main.py'" >> ~/.bashrc
   source ~/.bashrc
   ```

## Usage
Run the tool with optional color customization:
```
c2fetch [--color COLOR]
```
- `--color COLOR`: Sets the color of the ASCII art banner (default: `magenta`). Available colors include `cyan`, `green`, etc.

Example:
```
c2fetch --color cyan
```

## Customization
- **Temperature Thresholds**: Modify the `temp_style()` function in `main.py` to adjust color thresholds for temperature displays.
- **ASCII Art**: Update the banner in the `create_ascii_art()` function in `main.py` to customize the visual output.

## Contributing
Contributions are welcome! To get started:
1. Fork the repository.
2. Create a feature branch:
   ```
   git checkout -b feat/your-feature
   ```
3. Commit your changes:
   ```
   git commit -am "Add your feature"
   ```
4. Push to the branch:
   ```
   git push origin feat/your-feature
   ```
5. Open a Pull Request on GitHub.

Please ensure your code follows the project's style and includes relevant tests or documentation updates.

## License
MIT License. See [LICENSE](LICENSE) for details.

---

Designed and Crafted with ❤️ & ✨ by ~ Me
