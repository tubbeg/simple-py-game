import pyxel
from enum import Enum

class Direction(Enum):
    NOWHERE = 1
    LEFT = 2
    RIGHT = 3
    DOWN = 4
    UP = 5
    DOWNLEFT = 6
    DOWNRIGHT = 7
    UPLEFT = 8
    UPRIGHT = 9

def is_moving_left():
    return pyxel.btn(pyxel.KEY_A)

def is_moving_right():
    return pyxel.btn(pyxel.KEY_D)

def is_moving_up():
    return pyxel.btn(pyxel.KEY_W)

def is_moving_down():
    return pyxel.btn(pyxel.KEY_S)

def get_direction():
    dir = Direction.NOWHERE
    if is_moving_left():
        dir = Direction.LEFT
    if is_moving_right():
        dir = Direction.RIGHT
    if is_moving_up():
        if dir is Direction.LEFT:
            dir = Direction.UPLEFT
        elif dir is Direction.RIGHT:
            dir = Direction.UPRIGHT
        else:
            dir = Direction.UP
    if is_moving_down():
        if dir is Direction.LEFT:
            dir = Direction.DOWNLEFT
        elif dir is Direction.RIGHT:
            dir = Direction.DOWNRIGHT
        else:
            dir = Direction.DOWN
    return dir


def is_exit():
    q = pyxel.btn(pyxel.KEY_Q)
    esc = pyxel.btn(pyxel.KEY_ESCAPE)
    return (q or esc)