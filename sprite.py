import pyxel
import control as ctrl





def draw_sprite(frame,pos):
    x,y = pos
    new_frame = frame + 1
    new_frame = new_frame % 2
    pyxel.blt(x, y, new_frame, 0, 0, 16, 16)
    return (new_frame)



def move_sprite(dir, pos):
    x,y = pos
    if dir is ctrl.Direction.LEFT:
        return (x - 1, y)
    if dir is ctrl.Direction.RIGHT:
        return (x + 1, y)
    return pos