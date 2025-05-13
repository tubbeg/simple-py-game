import pyxel


x = 0

def calc_pos (a):
    return (a + 1) % pyxel.width

def update():
    global x
    x = calc_pos(x)

def draw():
    pyxel.cls(0)
    pyxel.rect(x, 0, 8, 8, 9)


def run_game ():
    pyxel.init(160, 120)
    pyxel.run(update, draw)


run_game()