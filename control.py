import pyxel
from enum import Enum

class Action(Enum):
    NONE = 1
    JUMP = 2

def is_jump():
    click = pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT)
    space = pyxel.btnr(pyxel.KEY_SPACE)
    return (click or space)

def get_action():
    dir = Action.NONE
    if is_jump():
        dir = Action.JUMP
    return dir

def is_exit():
    q = pyxel.btn(pyxel.KEY_Q)
    esc = pyxel.btn(pyxel.KEY_ESCAPE)
    return (q or esc)