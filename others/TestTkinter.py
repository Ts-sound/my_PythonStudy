import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
#         self.hi_there = tk.Button(self)
#         self.hi_there["text"] = "Hello World\n(click me)"
#         self.hi_there["command"] = self.say_hi
#         self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")
        
        self.front = tk.Button(self, text="前", fg="blue",
                              command=self.say_hi)
        self.front.pack(side="top")
        
        self.left = tk.Button(self, text="左", fg="blue",
                              command=self.say_hi)
        self.left.pack(side="left")
        
        self.right = tk.Button(self, text="右", fg="blue",
                              command=self.say_hi)
        self.right.pack(side="right")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
