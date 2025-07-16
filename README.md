<div align="center">

# **C2fetch**

**Lightweight real‑time CPU temperature monitor 🌡️** with customizable ASCII art, powered by [psutil](https://pypi.org/project/psutil/) and [rich](https://github.com/Textualize/rich).

<Img src="https://raw.githubusercontent.com/quietpulse/c2fetch/refs/heads/main/Pasted_image.png"/> 

</div>

---

## 🧩 Requirements

- **Python** 3.6+
- **rich** & **psutil** (`pip install rich psutil`)
- Unix‑like OS (Linux)

---

## 🚀 Quick Start

| Method          | Command                                  | Notes                             |
| --------------- | ---------------------------------------- | --------------------------------- |
| **Arch (Auto)** | `chmod +x setup.sh && ./setup.sh`        | Installer tested on Arch only     |
| **Ubuntu/DNF**  | `./main.py` *(see manual install below)* | Requires manual deps installation |
| **Manual**      | `python3 main.py [--color COLOR]`        | No setup script                   |

---

### 🔧 Automated (Arch Linux)

```bash
chmod +x setup.sh
./setup.sh        # Installs c2fetch + dependencies
./setup.sh --uninstall
````

### 🛠️ Manual (Ubuntu, Fedora, etc.)

1. **Clone repo**

   ```bash
   git clone https://github.com/kagiyanagi/c2fetch.git && cd c2fetch
   ```

2. **Install dependencies**

   * **Debian/Ubuntu:**

     ```bash
     sudo apt update && sudo apt install -y python3-pip
     ```
   * **Fedora:**

     ```bash
     sudo dnf install -y python3-pip
     ```
   * **Arch (alternative):**

     ```bash
     sudo pacman -Sy python-pip
     ```
   * **Install Python packages:**

     ```bash
     pip3 install --user rich psutil
     ```

3. **Alias (optional)**

   ```bash
   echo "alias c2fetch='python3 $(pwd)/main.py'" >> ~/.bashrc && source ~/.bashrc
   ```

4. **Run**

   ```bash
   c2fetch --color cyan
   ```

---

## 🎨 Usage & Options

```bash
c2fetch [--color COLOR]
```

* **`--color COLOR`**: ASCII art banner color (default: `magenta`)

---

## 🛠️ Customization

* **Thresholds**: Edit `temp_style()` in `main.py`.
* **ASCII art**: Replace banner in `create_ascii_art()`.

---

## 🤝 Contributing

1. Fork & clone this repository.
2. Create a feature branch:

   ```bash
   git checkout -b feat/YourIdea
   ```

3. Commit your changes & push:
   ```bash
    git commit -am "Add feature"
    git push origin feat/YourIdea
   ```

4. Open a **Pull Request** on GitHub.

---

##### Designed and Crafted with ❤️ & ✨ by ~ @kagiyanagi

