import ctypes
import sys
import tkinter as tk


WINDOW_WIDTH = 112
WINDOW_HEIGHT = 112
PURPLE = "#7657ff"
PURPLE_DARK = "#33256f"
PINK = "#ff00ff"


def valorant_is_foreground():
    """Return True when the foreground window title contains VALORANT."""
    if sys.platform != "win32":
        return True
    user32 = ctypes.windll.user32
    hwnd = user32.GetForegroundWindow()
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

        screen_width = self.root.winfo_screenwidth()
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+14+14")

        self.canvas = tk.Canvas(
            self.root,
            width=WINDOW_WIDTH,
            height=WINDOW_HEIGHT,
            bg=PINK,
            highlightthickness=0,
            bd=0,
        )
        self.canvas.pack()
        self._draw_avatar()
        self.root.bind("<Button-1>", self._start_drag)
        self.root.bind("<B1-Motion>", self._drag)
        self.root.bind("<Button-3>", lambda _event: self.root.destroy())
        self.root.bind("<Escape>", lambda _event: self.root.destroy())
        self.root.after(250, self._watch_valorant)

    def _draw_avatar(self):
        c = self.canvas
        # Outer profile badge
        c.create_oval(5, 5, 87, 87, fill=PURPLE_DARK, outline="")
        c.create_oval(9, 9, 83, 83, fill=PURPLE, outline="")
        # Simple profile illustration
        c.create_oval(32, 22, 60, 50, fill="#ffd7b0", outline="")
        c.create_arc(30, 18, 62, 48, start=180, extent=180, fill="#20253d", outline="#20253d")
        c.create_oval(40, 33, 44, 37, fill="#20253d", outline="")
        c.create_oval(50, 33, 54, 37, fill="#20253d", outline="")
        c.create_arc(41, 35, 53, 45, start=200, extent=140, style="arc", outline="#7a3e42", width=2)
        c.create_arc(25, 43, 67, 84, start=180, extent=180, fill="#26a6a1", outline="#26a6a1")
        # Online indicator
        c.create_oval(70, 70, 91, 91, fill="#0b1020", outline="")
        c.create_oval(74, 74, 87, 87, fill="#42d392", outline="")
        c.create_text(56, 99, text="FLEX", fill="white", font=("Segoe UI", 7, "bold"))

    def _watch_valorant(self):
        if valorant_is_foreground():
            self.root.deiconify()
            self.root.attributes("-topmost", True)
        else:
            self.root.withdraw()
        self.root.after(500, self._watch_valorant)

    def _start_drag(self, event):
        self._drag_x = event.x
        self._drag_y = event.y

    def _drag(self, event):
        x = self.root.winfo_x() + event.x - self._drag_x
        y = self.root.winfo_y() + event.y - self._drag_y
        self.root.geometry(f"+{x}+{y}")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    ProfileOverlay().run()
