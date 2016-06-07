from tkinter import *

class Character(object):

    def __init__(self, hero_x, hero_y):
        self.hero_x = hero_x
        self.hero_y = hero_y
        self.hero_image = PhotoImage(file="assets/hero-down.png")

    def draw(self, canvas):
        canvas.create_image(self.hero_x * 72, self.hero_y * 72, anchor=NW, image=self.hero_image)

    def move_up(self):
        self.hero_y = self.hero_y - 1
        self.hero_image = PhotoImage(file="assets/hero-up.png")

    def move_down(self):
        self.hero_y = self.hero_y + 1
        self.hero_image = PhotoImage(file="assets/hero-down.png")

    def move_right(self):
        self.hero_x = self.hero_x + 1
        self.hero_image = PhotoImage(file="assets/hero-right.png")

    def move_left(self):
        self.hero_x = self.hero_x - 1
        self.hero_image = PhotoImage(file="assets/hero-left.png")
