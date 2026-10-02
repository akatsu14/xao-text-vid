import json
import tkinter as tk
from urllib.parse import quote
import webbrowser
import os

# ================= CONFIG =================
DB_FILE = "database.json"

BASE_URL = "https://onedrive.live.com/?id=/personal/cf9f02afa8da0ec6/Documents/Personal/Videos/0.Khanh/Bio Mỹ/sample_images/"
LISTURL = "&listurl=/personal/cf9f02afa8da0ec6/Documents"
VIEWID = "&viewid=adf0c6a6-61f5-4f36-a5c9-4a79d84c7c60"

LOCAL_BASE = r"C:\Users\Manh Luong\Downloads\america"

# ================= THEME =================
BG = "#0f111a"
CARD_BG = "#1c1f2a"
BTN = "#3a3f55"
UNLOCKED = "#2ecc71"
TEXT = "white"


# ================= DB =================
def load_db():
    with open(DB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_db(data):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


# ================= LINKS =================
def make_onedrive_link(name):
    return BASE_URL + quote(name) + LISTURL + VIEWID


def make_google_search(name):
    return "https://www.google.com/search?q=" + quote(name)


# ================= LOCAL FOLDER =================
def create_local_folder(name):
    path = os.path.join(LOCAL_BASE, name)
    os.makedirs(path, exist_ok=True)
    print("📁 Created:", path)


# ================= APP =================
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("🎮 Character Explorer (Scroll Game UI)")
        self.root.geometry("600x750")
        self.root.configure(bg=BG)

        self.db = load_db()

        # ===== SEARCH =====
        self.search_var = tk.StringVar()
        tk.Entry(
            root,
            textvariable=self.search_var,
            font=("Arial", 12)
        ).pack(fill="x", padx=10, pady=10)

        self.search_var.trace("w", self.render)

        # ===== SCROLL AREA =====
        self.container = tk.Frame(root, bg=BG)
        self.container.pack(fill="both", expand=True)

        self.canvas = tk.Canvas(self.container, bg=BG, highlightthickness=0)
        self.canvas.pack(side="left", fill="both", expand=True)

        self.scrollbar = tk.Scrollbar(self.container, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.frame = tk.Frame(self.canvas, bg=BG)
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")

        self.frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        # mouse wheel scroll
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

        self.render()

    # ===== SCROLL =====
    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    # ===== ACTIONS =====
    def open_onedrive(self, name):
        for item in self.db:
            if item["name"] == name:
                item["opened"] = True

        save_db(self.db)
        # webbrowser.open(make_onedrive_link(name))
        # open local folder
        path = os.path.join(LOCAL_BASE, name)
        if os.path.exists(path):
            os.startfile(path)
        self.render()

    def open_google(self, name):
        webbrowser.open(make_google_search(name))

    def create_local(self, name):
        for item in self.db:
            if item["name"] == name:
                item["opened"] = True

        save_db(self.db)
        create_local_folder(name)
        self.render()

    # ===== UI =====
    def render(self, *args):
        for w in self.frame.winfo_children():
            w.destroy()

        keyword = self.search_var.get().lower()

        for item in self.db:
            if keyword in item["name"].lower():

                # CARD
                card = tk.Frame(
                    self.frame,
                    bg=CARD_BG,
                    highlightbackground="#222",
                    highlightthickness=1
                )
                card.pack(fill="x", padx=12, pady=8)

                color = UNLOCKED if item["opened"] else BTN

                # NAME BUTTON
                tk.Button(
                    card,
                    text=item["name"],
                    bg=color,
                    fg=TEXT,
                    font=("Arial", 12, "bold"),
                    relief="flat",
                    height=2,
                    command=lambda n=item["name"]: self.open_onedrive(n)
                ).pack(fill="x")

                # BUTTON ROW
                row = tk.Frame(card, bg=CARD_BG)
                row.pack(fill="x")

                tk.Button(
                    row,
                    text="🔎 Google",
                    bg="#444",
                    fg="white",
                    relief="flat",
                    command=lambda n=item["name"]: self.open_google(n)
                ).pack(side="left", expand=True, fill="x", padx=2, pady=5)

                tk.Button(
                    row,
                    text="☁ Open",
                    bg="#555",
                    fg="white",
                    relief="flat",
                    command=lambda n=item["name"]: self.open_onedrive(n)
                ).pack(side="left", expand=True, fill="x", padx=2, pady=5)

                tk.Button(
                    row,
                    text="📁 Folder",
                    bg="#666",
                    fg="white",
                    relief="flat",
                    command=lambda n=item["name"]: self.create_local(n)
                ).pack(side="left", expand=True, fill="x", padx=2, pady=5)


# ================= RUN =================
if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()