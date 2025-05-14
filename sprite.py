import pyxel
import control as ctrl
from dataclasses import dataclass

@dataclass
class PxSprite():
    state : ctrl.Direction
    frame : int
    x : int
    y : int
    size = (16,16)
    res_x : int
    res_y : int
    update_anim_freq : int

def should_update_frame(f):
    update_at = pyxel.frame_count % f
    return (update_at == 0)

def is_walking(spr):
    return (spr.state is not ctrl.Direction.NOWHERE)

def update_frame(spr):
    if is_walking(spr):
        if should_update_frame(spr.update_anim_freq):
            new_frame = spr.frame + 1
            new_frame = new_frame % 2
            spr.frame = new_frame
            return spr
        else:
            return spr
    else:
        spr.frame = 0
        return spr

def draw_sprite(spr):
    x,y = spr.x,spr.y
    a,b = spr.size
    spr = update_frame (spr)

    pyxel.blt (x, y, spr.frame, spr.res_x, spr.res_y, a, b)
    return spr

def move_sprite(dir, spr):
    spr.state = dir
    if dir is ctrl.Direction.LEFT:
        spr.x = spr.x - 1
    if dir is ctrl.Direction.RIGHT:
        spr.x = spr.x + 1
    if dir is ctrl.Direction.UP:
        spr.y = spr.y - 1
    if dir is ctrl.Direction.DOWN:
        spr.y = spr.y + 1
    if dir is ctrl.Direction.UPLEFT:
        spr.y = spr.y - 1
        spr.x = spr.x - 1
    if dir is ctrl.Direction.DOWNLEFT:
        spr.y = spr.y + 1
        spr.x = spr.x - 1
    if dir is ctrl.Direction.UPRIGHT:
        spr.y = spr.y - 1
        spr.x = spr.x + 1
    if dir is ctrl.Direction.DOWNRIGHT:
        spr.y = spr.y + 1
        spr.x = spr.x + 1