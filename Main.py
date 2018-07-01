from tkinter import *
import time

class Application(Frame):
    def say_hi(self):
        print("hi there, everyone!")

    def keydown(self, e):
        print('press', e.char)
        if e.char == 'd':
            self.canvas.move(self.img, 50, 0)
        elif e.char == 'a':
            self.canvas.move(self.img, -50, 0)        

    def createWidgets(self):
        self.canvas = Canvas(self, width=640, height=480, bg='green')
        self.canvas.pack()
        self.canvas.create_line(0, 0, 200, 100)
        rect = self.canvas.create_rectangle(0, 0, 50, 50, fill='red')
        self.canvas.move(rect, 20, 20)
        format = "gif -index " + str(2)
        self.gif = PhotoImage(file = 'C:\\Users\\David\\Pictures\\basketball.gif', format=format)
        self.img = self.canvas.create_image(20, 20, image=self.gif, anchor=NW)

        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
root.title("my game")
root.geometry("800x600")
app = Application(master=root)
app.bind("<KeyPress>", app.keydown)
app.focus_set()
app.mainloop()
root.destroy()