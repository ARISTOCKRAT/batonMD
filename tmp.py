import tkinter as tk
from tkinter import ttk

class ExampleApp(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.var1 = tk.StringVar()
        self.var2 = tk.StringVar()

        f1 = ttk.Frame(self)
        red_button = ttk.Button(f1, text="Red", command=self.make_red)
        default_button = ttk.Button(f1, text="Default", command=self.make_default)
        default_button.pack(side="left")
        red_button.pack(side="left")

        f2 = ttk.Frame(self)
        self.cb_one = ttk.Checkbutton(f2, text="Option 1", variable=self.var1,
                                      onvalue=1, offvalue=0)
        self.cb_two  = ttk.Checkbutton(f2, text="Option 2", variable=self.var2,
                                       onvalue=1, offvalue=0)
        self.cb_one.pack(side="left")
        self.cb_two.pack(side="left")

        f1.pack(side="top", fill="x")
        f2.pack(side="top", fill="x")

        style = ttk.Style()
        style.configure("Red.TCheckbutton", foreground="red")

    def make_red(self):
        self.cb_one.configure(style="Red.TCheckbutton")
        self.cb_two.configure(style="Red.TCheckbutton")

    def make_default(self):
        self.cb_one.configure(style="TCheckbutton")
        self.cb_two.configure(style="TCheckbutton")


if __name__ == "__main__":
    root = tk.Tk()
    ExampleApp(root).pack(fill="both", expand=True)
    root.mainloop()

