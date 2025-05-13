import pyxel
import control as ctrl
import sprite as s

sprite_pos = (0,0)
sprite_frame = 0

def update():
    global sprite_pos
    dir = ctrl.get_direction ()
    sprite_pos = s.move_sprite (dir, sprite_pos)

def draw():
    global sprite_frame
    pyxel.cls(0)
    sprite_frame = s.draw_sprite(sprite_frame, sprite_pos)
    #pyxel.rect(x, 0, 8, 8, 9)

def run_game ():
    pyxel.init(160, 120)
    pyxel.load("adv1.pyxres")
    pyxel.run(update,draw)


run_game()

if __name__ == "__main__":
    run_game()