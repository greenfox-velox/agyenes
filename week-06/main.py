from tkinter import *
import random
from character import Character
from skeleton import Skeleton
from boss import Boss

root = Tk()


def random_position():
    random_x = random.randint(0, 9)
    random_y = random.randint(0, 9)
    return [random_x, random_y]

field_size = 72
no_of_fields_h = 10
no_of_fields_v = 10
a = PhotoImage(file="assets/floor.png")
b = PhotoImage(file="assets/wall.png")
char = Character(random_position()[0], random_position()[1])
skeleton_1 = Skeleton(random_position()[0], random_position()[1])
skeleton_2 = Skeleton(random_position()[0], random_position()[1])
skeleton_3 = Skeleton(random_position()[0], random_position()[1])
boss = Boss(random_position()[0], random_position()[1])
canvas = Canvas(root, width='720', height='820  ', bg='white')
canvas.create_rectangle(0, 720, 800, 800, fill="white")

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

def make_dict(map_x):
    map_dict = []
    for i in range(len(map_x)):
        for j in range(len(map_x[i])):
            row = {}
            row['x'] = j
            row['y'] = i
            if map_x[i][j] == 0:
                row['type'] = 'floor'
            if map_x[i][j] == 1:
                row['type'] = 'wall'
            if map_x[i][j] == 2:
                row['type'] = 'hero'
            map_dict.append(row)
    return map_dict

def screen_drawer(x, y):
    for i in range(x):
        for j in range(y):
            if map_1[j][i] == 0:
                canvas.create_image(i * field_size, j * field_size, anchor=NW, image=a)
            elif map_1[j][i] == 1:
                canvas.create_image(i * field_size, j * field_size, anchor=NW, image=b)
    canvas.create_rectangle(0, 720, 720, 800, fill="grey")
    canvas.create_rectangle(10, 730, 710, 790, fill="white")
    canvas.create_text(360, 760, text='Hero (Level 1) HP: 8/10 | DP: 8 | SP: 6', font=('Arial', 24, 'bold'))

    char.draw(canvas)
    skeleton_1.draw(canvas)
    skeleton_2.draw(canvas)
    skeleton_3.draw(canvas)
    boss.draw(canvas)

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
