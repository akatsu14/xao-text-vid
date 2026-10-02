import os
import tkinter as tk
from tkinter import ttk, font
import webbrowser

ID_FOLDER = "id_folder"
OPENED = set()

# Color palette
BG = "#0f0f13"
BG2 = "#1a1a24"
BG3 = "#22222f"
ACCENT = "#6c63ff"
ACCENT2 = "#ff6584"
TEXT = "#e8e8f0"
TEXT_DIM = "#6b6b8a"
GREEN = "#4ade80"
BORDER = "#2e2e42"

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Downsub Opener")
        self.root.geometry("680x560")
        self.root.configure(bg=BG)
        self.root.resizable(True, True)

        self._setup_styles()
        self._build_ui()
        self.load_files()

    def _setup_styles(self):
        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "Custom.TCombobox",
            fieldbackground=BG3,
            background=BG3,
            foreground=TEXT,
            arrowcolor=ACCENT,
            bordercolor=BORDER,
            lightcolor=BORDER,
            darkcolor=BORDER,
            selectbackground=ACCENT,
            selectforeground=TEXT,
            padding=(10, 8),
            font=("Consolas", 11),
        )
        style.map(
            "Custom.TCombobox",
            fieldbackground=[("readonly", BG3)],
            background=[("readonly", BG3)],
            bordercolor=[("focus", ACCENT), ("!focus", BORDER)],
        )

        style.configure(
            "TScrollbar",
            background=BG2,
            troughcolor=BG,
            bordercolor=BORDER,
            arrowcolor=TEXT_DIM,
            width=8,
        )
        style.map("TScrollbar", background=[("active", BG3)])

    def _build_ui(self):
        # ── Header ──────────────────────────────────────────────
        header = tk.Frame(self.root, bg=BG, pady=0)
        header.pack(fill="x", padx=0, pady=0)

        # Top accent bar
        accent_bar = tk.Frame(header, bg=ACCENT, height=3)
        accent_bar.pack(fill="x")

        title_frame = tk.Frame(header, bg=BG, padx=28, pady=18)
        title_frame.pack(fill="x")

        tk.Label(
            title_frame,
            text="⬇  DOWNSUB",
            font=("Consolas", 20, "bold"),
            fg=TEXT,
            bg=BG,
        ).pack(side="left")

        tk.Label(
            title_frame,
            text="OPENER",
            font=("Consolas", 20, "bold"),
            fg=ACCENT,
            bg=BG,
        ).pack(side="left", padx=(4, 0))

        self.counter_label = tk.Label(
            title_frame,
            text="0 opened",
            font=("Consolas", 10),
            fg=TEXT_DIM,
            bg=BG,
        )
        self.counter_label.pack(side="right")

        # Divider
        tk.Frame(self.root, bg=BORDER, height=1).pack(fill="x")

        # ── File selector ────────────────────────────────────────
        selector_frame = tk.Frame(self.root, bg=BG2, padx=28, pady=16)
        selector_frame.pack(fill="x")

        tk.Label(
            selector_frame,
            text="ID LIST FILE",
            font=("Consolas", 9, "bold"),
            fg=TEXT_DIM,
            bg=BG2,
        ).pack(anchor="w", pady=(0, 6))

        combo_row = tk.Frame(selector_frame, bg=BG2)
        combo_row.pack(fill="x")

        self.combo = ttk.Combobox(combo_row, state="readonly", style="Custom.TCombobox")
        self.combo.pack(side="left", fill="x", expand=True)
        self.combo.bind("<<ComboboxSelected>>", self.load_ids)

        # Reload button
        self.reload_btn = tk.Button(
            combo_row,
            text="⟳",
            font=("Consolas", 14),
            bg=BG3,
            fg=ACCENT,
            activebackground=ACCENT,
            activeforeground=TEXT,
            relief="flat",
            bd=0,
            cursor="hand2",
            padx=12,
            pady=4,
            command=self.load_files,
        )
        self.reload_btn.pack(side="left", padx=(8, 0))

        # Divider
        tk.Frame(self.root, bg=BORDER, height=1).pack(fill="x")

        # ── Stats bar ───────────────────────────────────────────
        self.stats_frame = tk.Frame(self.root, bg=BG, padx=28, pady=10)
        self.stats_frame.pack(fill="x")

        self.total_label = tk.Label(
            self.stats_frame,
            text="—  IDs",
            font=("Consolas", 10),
            fg=TEXT_DIM,
            bg=BG,
        )
        self.total_label.pack(side="left")

        self.progress_label = tk.Label(
            self.stats_frame,
            text="",
            font=("Consolas", 10),
            fg=GREEN,
            bg=BG,
        )
        self.progress_label.pack(side="right")

        # ── Listbox area ─────────────────────────────────────────
        list_outer = tk.Frame(self.root, bg=BG, padx=20, pady=0)
        list_outer.pack(fill="both", expand=True, pady=(0, 12))

        # Inner border frame
        list_border = tk.Frame(list_outer, bg=BORDER, bd=0)
        list_border.pack(fill="both", expand=True)

        list_inner = tk.Frame(list_border, bg=BG2, bd=1)
        list_inner.pack(fill="both", expand=True, padx=1, pady=1)

        self.listbox = tk.Listbox(
            list_inner,
            font=("Consolas", 12),
            bg=BG2,
            fg=TEXT,
            selectbackground=ACCENT,
            selectforeground=TEXT,
            activestyle="none",
            relief="flat",
            bd=0,
            highlightthickness=0,
            cursor="hand2",
        )
        scrollbar = ttk.Scrollbar(list_inner, orient="vertical", command=self.listbox.yview)
        self.listbox.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        self.listbox.pack(side="left", fill="both", expand=True, padx=2, pady=2)

        self.listbox.bind("<<ListboxSelect>>", self.open_id)
        self.listbox.bind("<Enter>", lambda e: self.listbox.configure(bg="#1e1e2e"))
        self.listbox.bind("<Leave>", lambda e: self.listbox.configure(bg=BG2))

        # ── Footer ───────────────────────────────────────────────
        footer = tk.Frame(self.root, bg=BG, padx=28, pady=10)
        footer.pack(fill="x")

        tk.Label(
            footer,
            text="● Click an ID to open in Downsub",
            font=("Consolas", 9),
            fg=TEXT_DIM,
            bg=BG,
        ).pack(side="left")

        tk.Label(
            footer,
            text="Green = already opened",
            font=("Consolas", 9),
            fg=GREEN,
            bg=BG,
        ).pack(side="right")

    # ── Logic ────────────────────────────────────────────────────

    def load_files(self):
        if not os.path.exists(ID_FOLDER):
            os.makedirs(ID_FOLDER)
        files = [f for f in os.listdir(ID_FOLDER) if f.endswith(".txt")]
        self.combo["values"] = files
        if files:
            self.combo.current(0)
            self.load_ids()

    def load_ids(self, event=None):
        self.listbox.delete(0, tk.END)
        filename = self.combo.get()
        if not filename:
            return
        path = os.path.join(ID_FOLDER, filename)

        with open(path, "r") as f:
            ids = [line.strip() for line in f if line.strip()]

        for vid in ids:
            self.listbox.insert(tk.END, f"  {vid}")
            if vid in OPENED:
                self.listbox.itemconfig(tk.END, fg=GREEN)
            else:
                self.listbox.itemconfig(tk.END, fg=TEXT)

        total = len(ids)
        opened = sum(1 for v in ids if v in OPENED)
        self.total_label.config(text=f"{total}  IDs")
        self.progress_label.config(text=f"✓ {opened} / {total} opened")

    def open_id(self, event):
        selection = self.listbox.curselection()
        if not selection:
            return

        index = selection[0]
        raw = self.listbox.get(index).strip()
        video_id = raw

        youtube_url = f"https://www.youtube.com/watch?v={video_id}"
        downsub_url = f"https://downsub.com/?url={youtube_url}"

        webbrowser.open(downsub_url)

        OPENED.add(video_id)
        self.listbox.itemconfig(index, fg=GREEN)

        # Update counter
        total = self.listbox.size()
        opened = len(OPENED)
        self.counter_label.config(text=f"{opened} opened")
        self.progress_label.config(text=f"✓ {opened} / {total} opened")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()