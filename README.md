📂 File Organizer Toolkit

A cross-platform desktop application that automatically organizes files into categories like images, documents, videos, and more.

Built with Python + Tkinter, featuring a clean GUI, dry-run safety mode, and real-time logs.

---

🚀 Features

- 📁 Automatically organizes files by type
- 🖥️ Simple and clean GUI
- 🔍 Dry-run mode (preview before making changes)
- 📊 Real-time logs and status updates
- ⚡ Fast and lightweight
- 🌍 Cross-platform (Mac & Windows)

---

🧠 How It Works

The tool scans a selected directory and classifies files into categories such as:

- Photos → `.jpg`, `.png`, `.heic`, etc.
- Documents → `.pdf`, `.docx`, `.txt`, etc.
- Videos → `.mp4`, `.mkv`, etc.
- Audio → `.mp3`, `.wav`, etc.
- Archives → `.zip`, `.rar`, etc.
- Others → everything else

It then moves them into corresponding folders.

---

📦 Installation

🔧 Option 1: Run from Source

```bash
git clone https://github.com/yourusername/FileOrganizerToolkit.git
cd FileOrganizerToolkit

python3 -m venv venv
source venv/bin/activate   # Mac/Linux

pip install -r requirements.txt
python -m ui.app
```
💻 Option 2: Download Prebuilt App

Go to the Releases
 - section and download:

🍎 Mac → .app / .dmg
🪟 Windows → .exe


⚙️ Usage
-Click Browse Folder
-Select the directory you want to organize
-(Optional) Enable Dry Run
-Click Organize

⚠️ Safety Features
- Dry-run mode prevents accidental file moves
- Skips hidden files
- Avoids overwriting files (auto-renames duplicates)


🛠️ Tech Stack
- Python 3
- Tkinter (GUI)
- shutil & os (file operations)
- PyInstaller (packaging)
- GitHub Actions (CI/CD)

🔄 Future Improvements
- Undo feature
- File preview before organizing
- Custom rules (user-defined categories)
- Dark/light theme toggle
- Drag & drop support (optional)


🤝 Contributing

Feel free to fork the repo and submit pull requests!










