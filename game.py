import pyxel



def update():
    pass

def draw():
    pyxel.cls(0)
    pyxel.blt(0, 0, 0, 0, 0, 16, 16)
    #pyxel.rect(x, 0, 8, 8, 9)


def run_game ():
    pyxel.init(160, 120)
    pyxel.load("adv1.pyxres")
    pyxel.run(update, draw)


run_game()