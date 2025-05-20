import tkinter as tk

class Page4(tk.Frame):
    def __init__(self, parent, on_click):
        super().__init__(parent, bg="lightyellow")
        label = tk.Label(self, text="檔案4", font=("Arial", 24), bg="lightyellow")
        label.pack(pady=100)
        self.bind("<Button-1>", on_click)
