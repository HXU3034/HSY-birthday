import tkinter as tk
from tkinter import PhotoImage

class Page1(tk.Frame):
    def __init__(self, parent, on_image_click):
        super().__init__(parent, bg="white")

        label = tk.Label(self, text="檔案1", font=("Arial", 24), bg="white")
        label.pack(pady=10)

        self.img1 = PhotoImage(file="img1.png")
        self.img2 = PhotoImage(file="img2.png")
        self.img3 = PhotoImage(file="img3.png")

        for img in [self.img1, self.img2, self.img3]:
            lbl = tk.Label(self, image=img, bg="white", cursor="hand2")
            lbl.image = img  # 防止圖片被回收
            lbl.pack(pady=5)
            lbl.bind("<Button-1>", on_image_click)
