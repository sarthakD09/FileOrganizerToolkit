import tkinter as tk
import tkinter.ttk as ttk
import threading
from tkinter import filedialog
from main import organize_directory
import time

# ---------- THEME ----------
BG = "#1e1e1e"
FG = "#ffffff"
ACCENT = "#4CAF50"
SECONDARY = "#2d2d2d"
ERROR = "#ff4d4d"
INFO = "#00bfff"

# ---------- APP CLASS ----------
class FileOrganizerApp:

    def __init__(self, root):
        self.root = root
        self.selected_path = None

        self.setup_ui()

    # ---------- UI ----------
    def setup_ui(self):
        self.root.title("File Organizer Toolkit v1.0 by Novion")
        self.root.geometry("550x550")
        self.root.configure(bg=BG)

        tk.Label(
            self.root,
            text="File Organizer Toolkit",
            font=("Arial", 16, "bold"),
            bg=BG,
            fg=FG
        ).pack(pady=10)

        self.top_frame = tk.Frame(self.root, bg=BG)
        self.top_frame.pack(pady=5)

        self.status_label = tk.Label(
            self.top_frame,
            text="Waiting for action...",
            bg=BG,
            fg=FG
        )
        self.status_label.pack(pady=5)

        self.folder_label = tk.Label(
            self.top_frame,
            text="No folder selected",
            bg=BG,
            fg="#aaaaaa"
        )
        self.folder_label.pack(pady=5)

        self.create_controls()
        self.create_logs()

    # ---------- CONTROLS ----------
    def create_controls(self):
        tk.Button(
            self.top_frame,
            text="Browse Folder",
            command=self.choose_folder,
            bg=ACCENT,
            fg="black",
            relief="flat",
            padx=10,
            pady=5
        ).pack(pady=5)

        self.checkbox_value = tk.BooleanVar(value=True)

        tk.Checkbutton(
            self.top_frame,
            text="Dry Run (No changes will be made)",
            variable=self.checkbox_value,
            bg=BG,
            fg=FG,
            selectcolor=SECONDARY
        ).pack(pady=5)

        button_frame = tk.Frame(self.root, bg=BG)
        button_frame.pack(pady=10)

        self.organize_btn = tk.Button(
            button_frame,
            text="Organize",
            width=12,
            command=self.run_organizer,
            bg=ACCENT,
            fg="black",
            relief="flat"
        )
        self.organize_btn.pack(side=tk.LEFT, padx=5)

        tk.Button(
            button_frame,
            text="Clear Logs",
            width=12,
            command=self.clear_logs,
            bg=SECONDARY,
            fg="black",
            relief="flat"
        ).pack(side=tk.LEFT, padx=5)

        self.progress = ttk.Progressbar(
            self.root,
            orient="horizontal",
            mode="indeterminate"
        )

    # ---------- LOG UI ----------
    def create_logs(self):
        tk.Label(
            self.root,
            text="Logs",
            font=("Arial", 10, "bold"),
            bg=BG,
            fg=FG
        ).pack()

        frame = tk.Frame(self.root, bg=SECONDARY)
        frame.pack(fill="both", expand=True, padx=10, pady=10)

        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.log_text = tk.Text(
            frame,
            wrap="word",
            bg="#121212",
            fg=FG,
            insertbackground="white",
            yscrollcommand=scrollbar.set
        )
        self.log_text.pack(side=tk.LEFT, fill="both", expand=True)

        scrollbar.config(command=self.log_text.yview)

        # Log colors
        self.log_text.tag_config("info", foreground="#ffffff")
        self.log_text.tag_config("success", foreground=ACCENT)
        self.log_text.tag_config("error", foreground=ERROR)

    # ---------- ACTIONS ----------
    def choose_folder(self):
        path = filedialog.askdirectory()
        if path:
            self.set_folder(path, "Folder selected")

    def run_organizer(self):
        if not self.selected_path:
            self.set_status("Please select a folder first!", ERROR)
            return

        threading.Thread(target=self.worker, daemon=True).start()

    def worker(self):
        self.ui_update(self.start_progress)

        success, msg = organize_directory(
            self.selected_path,
            self.checkbox_value.get(),
            logger=lambda m: self.log(m, "info")
        )

        self.ui_update(self.stop_progress)

        if success:
            self.set_status(msg, ACCENT)
            self.log(msg, "success")
        else:
            self.set_status(msg, ERROR)
            self.log(msg, "error")

    # ---------- HELPERS ----------
    def set_folder(self, path, message):
        self.selected_path = path
        self.folder_label.config(text=path, fg=ACCENT)
        self.set_status(message, ACCENT)

    def set_status(self, message, color):
        self.ui_update(lambda: self.status_label.config(text=message, fg=color))

    def log(self, message, level="info"):
        timestamp = time.strftime("%H:%M:%S")
        self.ui_update(lambda: self._append_log(f"[{timestamp}] {message}", level))

    def _append_log(self, message, level):
        self.log_text.insert(tk.END, message + "\n", level)
        self.log_text.see(tk.END)

    def clear_logs(self):
        self.log_text.delete(1.0, tk.END)

    def start_progress(self):
        self.progress.pack(fill="x", padx=20, pady=10)
        self.progress.start()
        self.organize_btn.config(state="disabled")
        self.set_status("Organizing...", INFO)

    def stop_progress(self):
        self.progress.stop()
        self.progress.pack_forget()
        self.organize_btn.config(state="normal")

    def ui_update(self, func):
        self.root.after(0, func)


# ---------- RUN ----------
if __name__ == "__main__":
    root = tk.Tk()
    app = FileOrganizerApp(root)
    root.mainloop()