from tkinter import Tk, Canvas
from grid import Grid
from human import Human
from student import Student
from hero import Hero
import random


root = Tk()
canvas = Canvas(root, width=800,height=600)
canvas.pack()
grid = Grid(canvas)
grid.display()
fs=open('students.txt', 'r', encoding='utf-8')

students=[]
for student in fs:
    s=student.split(';')
    id=int(s[0])
    name=s[1]
    var=int(s[3])
    group='ИП-21'
    gender=s[2]
    students.append({'id': id, 'full_name':name, 'variant':var, 'group':group, 'gender': gender })

fs.close()

s1 = random.choice(students)
name = s1['full_name'].split()[0]
p1 = Hero(canvas, 200, 500, s1['full_name'], s1['gender'])
p1.display()

s1 = random.choice(students)
p2=Hero(canvas, 500, 500, s1['full_name'], s1['gender'])
p2.display()

root.mainloop()