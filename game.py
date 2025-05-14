import pyxel
import control as ctrl
import sprite as s

spr_loc = (0,0)

def update(sprite):
    dir = ctrl.get_direction ()
    s.move_sprite (dir, sprite)

def draw(sprite):
    pyxel.cls(1)
    sprite = s.draw_sprite(sprite)

def run_game ():
    spr = s.PxSprite(ctrl.Direction.NOWHERE, 0,0,0,0,0,30)
    fdraw = lambda: draw (spr)
    fupdate = lambda: update(spr)
    pyxel.init(160, 120,fps=60)
    pyxel.load("adv1.pyxres")
    pyxel.run(fupdate,fdraw)

if __name__ == "__main__":
    run_game()