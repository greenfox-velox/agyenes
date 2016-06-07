from tkinter import *
import random
from character import Character

root = Tk()

map_1 = [[1,0,0,1,0,1,0,0,0,0],
        [0,0,0,1,0,1,0,1,1,0],
        [0,1,1,1,0,1,0,1,1,0],
        [0,0,0,0,0,1,0,0,0,0],
        [1,1,1,1,0,1,1,1,1,0],
        [0,1,0,1,0,0,0,0,1,0],
        [0,1,0,1,0,0,0,0,1,0],
        [0,0,0,0,0,1,1,0,1,0],
        [0,1,1,1,0,0,0,0,1,0],
        [0,0,0,1,0,1,1,0,1,0],
        [0,1,0,1,0,1,0,0,0,0]]

#dictionary-t 3 adattal (x, y, fal v. floor)

field_size = 72
no_of_fields_h = 10
no_of_fields_v = 10
a = PhotoImage(file="assets/floor.png")
b = PhotoImage(file="assets/wall.png")
c = PhotoImage(file="assets/hero-down.png")
char = Character(0,0)
canvas = Canvas(root, width='720', height='720  ', bg='white')

def screen_drawer(x, y):
    for i in range(x):
        for j in range(y):
            if map_1[j][i] == 0:
                canvas.create_image(i * field_size, j * field_size, anchor=NW, image=a)
            elif map_1[j][i] == 1:
                canvas.create_image(i * field_size, j * field_size, anchor=NW, image=b)
    char.draw(canvas)

def move_down(event):
    char.move_down()
    screen_drawer(no_of_fields_h, no_of_fields_v)

def move_up(event):
    char.move_up()
    screen_drawer(no_of_fields_h, no_of_fields_v)

def move_left(event):
    char.move_left()
    screen_drawer(no_of_fields_h, no_of_fields_v)

def move_right(event):
    char.move_right()
    screen_drawer(no_of_fields_h, no_of_fields_v)

root.bind("<Up>", move_up)
root.bind("<Down>", move_down)
root.bind("<Right>", move_right)
root.bind("<Left>", move_left)

screen_drawer(no_of_fields_h, no_of_fields_v)

canvas.pack()

root.mainloop()
