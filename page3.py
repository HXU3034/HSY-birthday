import tkinter as tk

class Page3(tk.Frame):
    def __init__(self, parent, on_click):
        super().__init__(parent, bg="lightgreen")
        label = tk.Label(self, text="檔案3", font=("Arial", 24), bg="lightgreen")
        label.pack(pady=100)
        self.bind("<Button-1>", on_click)
