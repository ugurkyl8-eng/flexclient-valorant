import ctypes
import sys
import tkinter as tk

WINDOW_WIDTH = 112
WINDOW_HEIGHT = 112
MENU_WIDTH = 350
MENU_HEIGHT = 230
PURPLE = "#7657ff"
PURPLE_DARK = "#33256f"
PINK = "#ff00ff"
BG = "#0b1020"
PANEL = "#121a2f"
PANEL_2 = "#192440"
TEXT = "#f4f7ff"
MUTED = "#9aa8c7"
GREEN = "#42d392"

MIXES = [
    ("Aim Warmup", "Nişan ısınma preset'i"),
    ("Crosshair Focus", "Crosshair sabitleme preset'i"),
    ("Utility Review", "Yetenek ve lineup kontrolü"),
]


def foreground_is_valorant(overlay_hwnd=None):
    """Check only the foreground window title; no game memory or files are read."""
    if sys.platform != "win32":
        return True
    user32 = ctypes.windll.user32
    hwnd = user32.GetForegroundWindow()
    if overlay_hwnd and hwnd == overlay_hwnd:
        return True
    if not hwnd:
        return False
    title = ctypes.create_unicode_buffer(512)
    user32.GetWindowTextW(hwnd, title, 512)
    return "valorant" in title.value.lower()


class ProfileOverlay:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("FlexClient Profile")
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        self.root.configure(bg=PINK)
        try:
            self.root.wm_attributes("-transparentcolor", PINK)
        except tk.TclError:
            pass

        self.menu_open = False
        self.selected_mix = "Mix 1"
        self.status = "Hazır"
        self.canvas = tk.Canvas(
            self.root,
            width=WINDOW_WIDTH,
            height=WINDOW_HEIGHT,
            bg=PINK,
            highlightthickness=0,
            bd=0,
        )
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self._on_left_click)
        self.root.bind("<Button-3>", lambda _event: self.root.destroy())
        self.root.bind("<Escape>", lambda _event: self.root.destroy())
        self.root.after(250, self._watch_valorant)
        self._render()

    def _draw_avatar(self):
        c = self.canvas
        c.create_oval(5, 5, 87, 87, fill=PURPLE_DARK, outline="")
        c.create_oval(9, 9, 83, 83, fill=PURPLE, outline="")
        c.create_oval(32, 22, 60, 50, fill="#ffd7b0", outline="")
        c.create_arc(30, 18, 62, 48, start=180, extent=180, fill="#20253d", outline="#20253d")
        c.create_oval(40, 33, 44, 37, fill="#20253d", outline="")
        c.create_oval(50, 33, 54, 37, fill="#20253d", outline="")
        c.create_arc(41, 35, 53, 45, start=200, extent=140, style="arc", outline="#7a3e42", width=2)
        c.create_arc(25, 43, 67, 84, start=180, extent=180, fill="#26a6a1", outline="#26a6a1")
        c.create_oval(70, 70, 91, 91, fill="#0b1020", outline="")
        c.create_oval(74, 74, 87, 87, fill=GREEN, outline="")
        c.create_text(56, 101, text="FLEX", fill="white", font=("Segoe UI", 7, "bold"))

    def _render(self):
        width = MENU_WIDTH if self.menu_open else WINDOW_WIDTH
        height = MENU_HEIGHT if self.menu_open else WINDOW_HEIGHT
        self.root.geometry(f"{width}x{height}+14+14")
        self.canvas.configure(width=width, height=height)
        self.canvas.delete("all")
        self._draw_avatar()

        if not self.menu_open:
            return

        c = self.canvas
        c.create_rectangle(104, 7, MENU_WIDTH - 7, MENU_HEIGHT - 7,
                           fill=PANEL, outline=PURPLE_DARK, width=2)
        c.create_text(124, 27, text="FLEXCLIENT", anchor="w", fill=TEXT,
                      font=("Segoe UI", 13, "bold"))
        c.create_text(124, 46, text="Meşru antrenman preset'leri", anchor="w", fill=PURPLE,
                      font=("Segoe UI", 9, "bold"))

        for index, (name, subtitle) in enumerate(MIXES):
            top = 60 + index * 39
            active = name == self.selected_mix
            c.create_rectangle(118, top, MENU_WIDTH - 20, top + 31,
                               fill=PANEL_2 if active else PANEL,
                               outline=PURPLE if active else PANEL)
            c.create_text(130, top + 10, text=name, anchor="w", fill=TEXT,
                          font=("Segoe UI", 10, "bold"))
            c.create_text(130, top + 23, text=subtitle, anchor="w", fill=MUTED,
                          font=("Segoe UI", 8))

        c.create_text(124, 203, text=f"Durum: {self.status}", anchor="w",
                      fill=GREEN, font=("Segoe UI", 9, "bold"))
        c.create_text(MENU_WIDTH - 20, 203, text="Avatar'a tıkla: kapat",
                      anchor="e", fill=MUTED, font=("Segoe UI", 8))

    def _on_left_click(self, event):
        if event.x <= 100 and event.y <= 110:
            self.menu_open = not self.menu_open
            self._render()
            return

        if self.menu_open and event.x >= 118:
            for index, (name, _subtitle) in enumerate(MIXES):
                top = 60 + index * 39
                if top <= event.y <= top + 31:
                    self.selected_mix = name
                    self.status = f"{name} aktif"
                    self._render()
                    return

    def _watch_valorant(self):
        overlay_hwnd = self.root.winfo_id()
        if foreground_is_valorant(overlay_hwnd):
            self.root.deiconify()
            self.root.attributes("-topmost", True)
        else:
            self.menu_open = False
            self.root.withdraw()
        self.root.after(500, self._watch_valorant)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    ProfileOverlay().run()
