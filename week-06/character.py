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

class Character(object):

    def __init__(self, hero_x, hero_y):
        self.hero_x = hero_x
        self.hero_y = hero_y
        self.hero_image = PhotoImage(file="assets/hero-down.png")

    def draw(self, canvas):
        if map_1[self.hero_y][self.hero_x] == 0:
            canvas.create_image(self.hero_x * 72, self.hero_y * 72, anchor=NW, image=self.hero_image)
        else:
            self.hero_x = random.randint(0, 9)
            self.hero_y = random.randint(0, 9)
            self.draw(canvas)

    def move_up(self):
        if self.hero_y > 0 and map_1[self.hero_y - 1][self.hero_x] == 0:
            self.hero_y = self.hero_y - 1
            self.hero_image = PhotoImage(file="assets/hero-up.png")
        else:
            self.hero_y = self.hero_y
            self.hero_image = PhotoImage(file="assets/hero-up.png")

    def move_down(self):
        if self.hero_y < 9 and map_1[self.hero_y + 1][self.hero_x] == 0:
            self.hero_y = self.hero_y + 1
            self.hero_image = PhotoImage(file="assets/hero-down.png")
        else:
            self.hero_y = self.hero_y
            self.hero_image = PhotoImage(file="assets/hero-down.png")

    def move_right(self):
        if self.hero_x < 9 and map_1[self.hero_y][self.hero_x + 1] == 0:
            self.hero_x = self.hero_x + 1
            self.hero_image = PhotoImage(file="assets/hero-right.png")
        else:
            self.hero_x = self.hero_x
            self.hero_image = PhotoImage(file="assets/hero-right.png")

    def move_left(self):
        if self.hero_x > 0 and map_1[self.hero_y][self.hero_x - 1] == 0:
            self.hero_x = self.hero_x - 1
            self.hero_image = PhotoImage(file="assets/hero-left.png")
        else:
            self.hero_x = self.hero_x
            self.hero_image = PhotoImage(file="assets/hero-left.png")
