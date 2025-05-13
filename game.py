import pyxel
from enum import Enum


class Direction(Enum):
    NOWHERE = 1
    LEFT = 2
    RIGHT = 3

def is_moving_left():
    return pyxel.btn(pyxel.KEY_A)

def is_moving_right():
    return pyxel.btn(pyxel.KEY_D)

def get_direction():
    if is_moving_left():
        return Direction.LEFT
    if is_moving_right():
        return Direction.RIGHT
    return Direction.NOWHERE

sprite_pos = (0,0)

def move_sprite(dir):
    global sprite_pos
    x,y = sprite_pos
    if dir is Direction.LEFT:
        sprite_pos = (x - 1, y)
    if dir is Direction.RIGHT:
        sprite_pos = (x + 1, y)


def update():
    dir = get_direction ()
    move_sprite (dir)

def draw():
    global sprite_pos
    x,y = sprite_pos
    pyxel.cls(0)
    pyxel.blt(x, y, 0, 0, 0, 16, 16)
    #pyxel.rect(x, 0, 8, 8, 9)


def run_game ():
    pyxel.init(160, 120)
    pyxel.load("adv1.pyxres")
    pyxel.run(update, draw)


run_game()

if __name__ == "__main__":
    run_game()