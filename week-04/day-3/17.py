# create a 300x300 canvas.
# make it look like a nigth sky:
# - The background should be black
# - The stars can be small squares
# - The stars should have random positions on the canvas
# - The stars should have random color (some shade of grey)

from tkinter import *
import random

root = Tk()

canvas = Canvas(root, width='500', height='500', bg='white')
canvas.pack()

size = 20

for i in range(23):
    canvas.create_line(0 + i * size, 400, 200 + i * size/2, 100 + i * size/2)

for i in range(23):
    canvas.create_line(0 + i * size, 400, 200 + i * size/2, 100 + i * size/2)

for i in range(23):
    canvas.create_line(0 + i * size, 400, 200 + i * size/2, 100 + i * size/2)

canvas.pack()

root.mainloop()
