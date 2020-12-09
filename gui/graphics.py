import tkinter as tk


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.menu = tk.Button(self)
        self.menu["text"] = "Hello World\n(click me)"
        self.menu["command"] = self.say_hi
        self.menu.pack(side="left")

        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("Hello!")

if __name__ == "__main__":
    try:
        window = tk.Tk()
        app = App(master=window)
        app.mainloop()
    except Exception as e:
        print(e)