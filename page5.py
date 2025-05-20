import tkinter as tk

class Page5(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="lightpink")
        label = tk.Label(self, text="檔案5", font=("Arial", 24), bg="lightpink")
        label.pack(pady=100)
