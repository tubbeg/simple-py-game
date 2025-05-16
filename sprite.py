import pyxel
import control as ctrl
from dataclasses import dataclass


def none_a ():
    return ctrl.Action.NONE

def jump_a ():
    return ctrl.Action.JUMP

@dataclass
class PxSprite():
    gravity = 0.01
    jump : ctrl.Action
    velocity : int
    def_frame = 0
    next_frame = []
    x : int
    y : int
    size = (16,16)
    res_x : int
    res_y : int
    update_anim_freq : int

def should_update_frame(f):
    update_at = pyxel.frame_count % f
    return (update_at == 0)

def is_jumping(spr):
    return (spr.jump is not ctrl.Action.NONE)

def set_frame(spr):
    #if should_update_frame(spr.update_anim_freq):
    for _ in range(0,30):
        spr.next_frame.append(1)
    return spr

def update_frame(spr):
    if is_jumping(spr):
        spr.jump = none_a()
        #print ("setting frame")
        return set_frame(spr)
    return spr

def draw_sprite(spr):
    x,y = spr.x,spr.y
    a,b = spr.size
    spr = update_frame (spr)
    if not spr.next_frame:
        draw_frame = spr.def_frame
    else:
        draw_frame = spr.next_frame.pop(0)
    pyxel.blt (x, y, draw_frame, spr.res_x, spr.res_y, a, b)
    return spr

def move_sprite(dir, spr):
    spr.jump = dir
    if dir is none_a():
        spr.velocity = spr.velocity + spr.gravity
        spr.y = spr.y + spr.velocity
    if dir is jump_a():
        spr.velocity = spr.velocity - 1
    