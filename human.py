from tkinter import Tk, Canvas, ARC, SE, W

class Human():
    def __init__(self, canvas, x, y, name, gen):
        self.canvas = canvas
        self.x = x
        self.y = y
        self._name = name
        self.gen = gen

        
    def display(self):
        self._drawHead()
        self._drawBody()
        self._drawLeggs()
        self._drawArms()
        self._drawName()
        self._drawEyes()
        
    def _drawLeggs(self):
        self.canvas.create_line(self.x, self.y, self.x+50, self.y-50, self.x+100, self.y, width=2)
        
    def _drawHead(self):
        self.canvas.create_oval(self.x+20, self.y-210, self.x+80, self.y-150, width=2)
        self.canvas.create_arc(self.x+30, self.y-190, self.x+70, self.y-160, start=0, extent=-180, style=ARC, outline="red", width=3)
        if self.gen=='м':
            self.canvas.create_line(self.x+50, self.y-210, self.x+50, self.y-225)
            self.canvas.create_line(self.x+50, self.y-210, self.x+25, self.y-225)
            self.canvas.create_line(self.x+50, self.y-210, self.x+75, self.y-225)
        else :
            self.canvas.create_line(self.x+25, self.y-200, self.x, self.y-150)
            self.canvas.create_line(self.x+75, self.y-200, self.x+100, self.y-150)
  
    def _drawBody(self):
        self.canvas.create_line(self.x+50, self.y-50, self.x+50, self.y-150, width=2)
        
    def _drawArms(self):
        self.canvas.create_line(self.x, self.y-100, self.x+50, self.y-150, self.x+100, self.y-100, width=2)
        
    def _drawName(self):
        self.canvas.create_text(self.x+50, self.y-250, text=self._name, font = "Verdara 14")
     
    def _drawEyes(self):
        self.canvas.create_oval(self.x+35, self.y-189, self.x+43, self.y-180, width=0, fill="blue")
        self.canvas.create_oval(self.x+65, self.y-190, self.x+57, self.y-181, width=0, fill="blue")