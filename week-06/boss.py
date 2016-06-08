from tkinter import *
import random

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

def random_position():
    random_x = random.randint(1, 10)
    random_y = random.randint(1, 10)
    return [random_x, random_y]

class Boss(object):

    def __init__(self, boss_x, boss_y):
        self.boss_x = boss_x
        self.boss_y = boss_y
        self.boss_image = PhotoImage(file="assets/boss.png")

    def draw(self, canvas):
        if map_1[self.boss_y][self.boss_x] == 0:
            canvas.create_image(self.boss_x * 72, self.boss_y * 72, anchor=NW, image=self.boss_image)
        else:
            self.boss_x = random.randint(0, 9)
            self.boss_y = random.randint(0, 9)
            self.draw(canvas)
