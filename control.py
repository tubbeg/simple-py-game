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


def is_exit():
    q = pyxel.btn(pyxel.KEY_Q)
    esc = pyxel.btn(pyxel.KEY_ESCAPE)
    return (q or esc)