import pyxel
import control as ctrl
import sprite as s


spr = s.PxSprite(0,0,0,0,0)


def update():
    global spr
    dir = ctrl.get_direction ()
    spr = s.move_sprite (dir, spr)

def draw():
    global spr
    pyxel.cls(0)
    spr = s.draw_sprite(spr)
    #pyxel.rect(x, 0, 8, 8, 9)

def run_game ():
    pyxel.init(160, 120)
    pyxel.load("adv1.pyxres")
    pyxel.run(update,draw)


if __name__ == "__main__":
    run_game()