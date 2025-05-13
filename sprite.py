import pyxel
import control as ctrl
from dataclasses import dataclass



@dataclass
class PxSprite():
    frame : int
    x : int
    y : int
    size = (16,16)
    res_x : int
    res_y : int

def draw_sprite(spr):
    x,y = spr.x,spr.y
    new_frame = spr.frame + 1
    new_frame = new_frame % 2
    a,b = spr.size
    pyxel.blt(x, y, new_frame, spr.res_x, spr.res_y, a, b)
    spr.frame = new_frame
    return spr


def move_sprite(dir, spr):
    if dir is ctrl.Direction.LEFT:
        spr.x = spr.x - 1
        return spr
    if dir is ctrl.Direction.RIGHT:
        spr.x = spr.x + 1
        return spr
    return spr