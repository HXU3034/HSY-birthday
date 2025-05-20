import tkinter as tk
from page1 import Page1
from page2 import Page2
from page3 import Page3
from page4 import Page4
from page5 import Page5

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("模組化頁面切換")
        self.click_count = 0

        # 建立頁面實例（傳入根容器與回呼）
        self.page1 = Page1(root, self.on_image_click)
        self.page2 = Page2(root, lambda e: self.show_page(self.page1))
        self.page3 = Page3(root, lambda e: self.show_page(self.page1))
        self.page4 = Page4(root, lambda e: self.show_page(self.page5))
        self.page5 = Page5(root)

        self.show_page(self.page1)

    def show_page(self, page):
        for p in [self.page1, self.page2, self.page3, self.page4, self.page5]:
            p.pack_forget()
        page.pack(fill="both", expand=True)

    def on_image_click(self, event):
        self.click_count += 1
        print(f"點擊次數：{self.click_count}")

        if self.click_count == 1:
            self.show_page(self.page2)
        elif self.click_count == 2:
            self.show_page(self.page3)
        elif self.click_count == 3:
            self.show_page(self.page4)
        else:
            self.click_count = 0
            self.show_page(self.page1)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
