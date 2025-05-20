import tkinter as tk

class Page2(tk.Frame):
    def __init__(self, parent, on_click):
        super().__init__(parent, bg="lightblue")
        label = tk.Label(self, text="檔案2", font=("Arial", 24), bg="lightblue")
        label.pack(pady=100)
        self.bind("<Button-1>", on_click)
