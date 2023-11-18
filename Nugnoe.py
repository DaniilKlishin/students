from tkinter import Tk, Canvas


root = Tk()
canvas = Canvas(root,Width=800,height=600)
canvas.pack()
canvas.create_line(0, 0, 100, 100, 200)
root.mainLoop()