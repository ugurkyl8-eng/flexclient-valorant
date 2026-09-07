import tkinter as tk
from tkinter import messagebox

BG = "#0b1020"
PANEL = "#121a2f"
PANEL_2 = "#192440"
TEXT = "#f4f7ff"
MUTED = "#9aa8c7"
ACCENT = "#7c5cff"
ACCENT_HOVER = "#9278ff"
SUCCESS = "#42d392"

MIXES = [
    ("Mix 1", "Standart mix menüsü", "Temel seçenekleri hızlıca görüntüle."),
    ("Mix 2", "Rekabetçi mix menüsü", "Daha yoğun bir çalışma düzeni için hazır görünüm."),
    ("Mix 3", "Özel mix menüsü", "Kendi kullanım akışını planlayabileceğin alan."),
]


class FlexClient(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("FlexClient · Valorant Mix Menüsü")
        self.geometry("980x620")
        self.minsize(820, 520)
        self.configure(bg=BG)
        self.selected_mix = tk.StringVar(value="Henüz mix seçilmedi")
        self.content = None
        self._build_shell()
        self.show_home()

    def _build_shell(self):
        sidebar = tk.Frame(self, bg=PANEL, width=220)
        sidebar.pack(side="left", fill="y")
        sidebar.pack_propagate(False)

        logo = tk.Frame(sidebar, bg=PANEL)
        logo.pack(fill="x", padx=22, pady=(28, 34))
        tk.Label(logo, text="FLEXCLIENT", bg=PANEL, fg=TEXT,
                 font=("Segoe UI", 17, "bold")).pack(anchor="w")
        tk.Label(logo, text="MIX MENÜSÜ", bg=PANEL, fg=ACCENT,
                 font=("Segoe UI", 9, "bold")).pack(anchor="w", pady=(3, 0))

        self.nav_buttons = []
        for label, command in [
            ("⌂  Ana Menü", self.show_home),
            ("✦  Mixler", self.show_mixes),
            ("⚙  Ayarlar", self.show_settings),
        ]:
            button = tk.Button(
                sidebar, text=label, command=command, anchor="w",
                bg=PANEL, fg=MUTED, activebackground=PANEL_2,
                activeforeground=TEXT, relief="flat", bd=0,
                font=("Segoe UI", 11), padx=22, pady=13, cursor="hand2"
            )
            button.pack(fill="x", padx=10, pady=2)
            self.nav_buttons.append(button)

        footer = tk.Frame(sidebar, bg=PANEL)
        footer.pack(side="bottom", fill="x", padx=22, pady=22)
        tk.Label(footer, text="v1.0.0", bg=PANEL, fg=MUTED,
                 font=("Segoe UI", 9)).pack(anchor="w")
        tk.Label(footer, text="Güvenli yerel menü", bg=PANEL, fg=SUCCESS,
                 font=("Segoe UI", 9)).pack(anchor="w", pady=(4, 0))

        self.content = tk.Frame(self, bg=BG)
        self.content.pack(side="right", fill="both", expand=True)

    def _clear_content(self):
        for widget in self.content.winfo_children():
            widget.destroy()

    def _header(self, eyebrow, title, subtitle):
        header = tk.Frame(self.content, bg=BG)
        header.pack(fill="x", padx=42, pady=(36, 22))
        tk.Label(header, text=eyebrow.upper(), bg=BG, fg=ACCENT,
                 font=("Segoe UI", 9, "bold")).pack(anchor="w")
        tk.Label(header, text=title, bg=BG, fg=TEXT,
                 font=("Segoe UI", 26, "bold")).pack(anchor="w", pady=(7, 4))
        tk.Label(header, text=subtitle, bg=BG, fg=MUTED,
                 font=("Segoe UI", 11)).pack(anchor="w")

    def _card(self, parent, title, description, button_text=None, command=None):
        card = tk.Frame(parent, bg=PANEL_2)
        card.pack(fill="x", pady=7)
        body = tk.Frame(card, bg=PANEL_2)
        body.pack(fill="x", padx=20, pady=18)
        text = tk.Frame(body, bg=PANEL_2)
        text.pack(side="left", fill="x", expand=True)
        tk.Label(text, text=title, bg=PANEL_2, fg=TEXT,
                 font=("Segoe UI", 13, "bold")).pack(anchor="w")
        tk.Label(text, text=description, bg=PANEL_2, fg=MUTED,
                 font=("Segoe UI", 10)).pack(anchor="w", pady=(5, 0))
        if button_text and command:
            tk.Button(body, text=button_text, command=command,
                      bg=ACCENT, fg="white", activebackground=ACCENT_HOVER,
                      activeforeground="white", relief="flat", bd=0,
                      font=("Segoe UI", 10, "bold"), padx=16, pady=9,
                      cursor="hand2").pack(side="right")

    def show_home(self):
        self._clear_content()
        self._header("Hoş geldin", "FlexClient Mix Menüsü", "Mix seçeneklerini tek ekrandan yönet.")
        wrap = tk.Frame(self.content, bg=BG)
        wrap.pack(fill="both", expand=True, padx=42)
        self._card(wrap, "Mixler", "Hazır mix seçeneklerini görüntüle ve seç.",
                   "Mixleri aç", self.show_mixes)
        self._card(wrap, "Seçili mix", self.selected_mix.get(),
                   "Değiştir", self.show_mixes)
        note = tk.Frame(wrap, bg="#101a2b")
        note.pack(fill="x", pady=(24, 0))
        tk.Label(note, text="Bilgi", bg="#101a2b", fg=SUCCESS,
                 font=("Segoe UI", 10, "bold")).pack(anchor="w", padx=18, pady=(15, 4))
        tk.Label(note, text="Bu uygulama yerel bir menü arayüzüdür; oyun dosyalarına veya oyun sürecine müdahale etmez.",
                 bg="#101a2b", fg=MUTED, wraplength=680, justify="left",
                 font=("Segoe UI", 10)).pack(anchor="w", padx=18, pady=(0, 15))

    def show_mixes(self):
        self._clear_content()
        self._header("Menü", "Mixler", "Kullanmak istediğin mix görünümünü seç.")
        wrap = tk.Frame(self.content, bg=BG)
        wrap.pack(fill="both", expand=True, padx=42)
        for name, title, description in MIXES:
            self._card(wrap, f"{name} · {title}", description, "Seç",
                       lambda selected=name: self.select_mix(selected))

    def select_mix(self, name):
        self.selected_mix.set(f"{name} seçildi")
        messagebox.showinfo("Mix seçildi", f"{name} aktif menü olarak seçildi.")
        self.show_home()

    def show_settings(self):
        self._clear_content()
        self._header("Uygulama", "Ayarlar", "FlexClient görünüm bilgileri.")
        wrap = tk.Frame(self.content, bg=BG)
        wrap.pack(fill="both", expand=True, padx=42)
        self._card(wrap, "Tema", "Koyu tema aktif.")
        self._card(wrap, "Sürüm", "FlexClient v1.0.0")
        self._card(wrap, "Durum", "Hazır", "Ana menü", self.show_home)


if __name__ == "__main__":
    FlexClient().mainloop()
