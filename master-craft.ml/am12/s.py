import tkinter as tk
from tkinter import messagebox

class MoshinHesab:
    def __init__(self, root):
        self.root = root
        self.root.title("ماشین حساب")
        self.root.geometry("320x420")
        self.root.resizable(False, False)
        self.root.configure(bg="#2c3e50")

        self.expression = ""
        self.create_widgets()
        self.bind_keys()  # فعال‌سازی پشتیبانی از کیبورد

    def create_widgets(self):
        # فریم نمایشگر
        self.display = tk.Entry(
            self.root, font=("Arial", 20), bd=10, relief="sunken",
            justify="right", bg="#ecf0f1"
        )
        self.display.grid(row=0, column=0, columnspan=4, ipady=10, pady=10, padx=10, sticky="nsew")

        # دکمه‌ها
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("C", 5, 0), ("Exit", 5, 3)
        ]

        for (text, row, col) in buttons:
            color = "#3498db" if text not in ["=", "C", "Exit"] else (
                "#2ecc71" if text == "=" else ("#e74c3c" if text == "C" else "#9b59b6")
            )
            tk.Button(
                self.root, text=text, font=("Arial", 14, "bold"),
                bg=color, fg="white", width=6, height=2,
                relief="raised", command=lambda t=text: self.on_click(t)
            ).grid(row=row, column=col, padx=5, pady=5)

        # تنظیم اندازه ردیف‌ها و ستون‌ها
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)

    def bind_keys(self):
        """اتصال دکمه‌های کیبورد به عملکرد ماشین حساب"""
        self.root.bind("<Key>", self.key_press)
        self.root.bind("<Return>", lambda e: self.on_click("="))   # وقتی Enter زده شد
        self.root.bind("<KP_Enter>", lambda e: self.on_click("="))  # وقتی Enter عددی (NumPad) زده شد

    def key_press(self, event):
        key = event.keysym

        if key in "0123456789":
            self.on_click(key)
        elif key in ["plus", "KP_Add"]:
            self.on_click("+")
        elif key in ["minus", "KP_Subtract"]:
            self.on_click("-")
        elif key in ["asterisk", "KP_Multiply"]:
            self.on_click("*")
        elif key in ["slash", "KP_Divide"]:
            self.on_click("/")
        elif key == "period":
            self.on_click(".")
        elif key in ["BackSpace"]:
            self.expression = self.expression[:-1]
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)
        elif key == "Escape":
            self.on_click("C")

    def on_click(self, char):
        if char == "C":
            self.expression = ""
            self.display.delete(0, tk.END)
        elif char == "=":
            try:
                result = str(eval(self.expression))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
                self.expression = result
            except ZeroDivisionError:
                messagebox.showerror("خطا", "تقسیم بر صفر مجاز نیست!")
                self.clear_display()
            except Exception:
                messagebox.showerror("خطا", "ورودی نامعتبر است!")
                self.clear_display()
        elif char == "Exit":
            self.root.destroy()
        else:
            self.expression += str(char)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)

    def clear_display(self):
        self.expression = ""
        self.display.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = MoshinHesab(root)
    root.mainloop()



