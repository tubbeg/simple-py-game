import pyxel
import control as ctrl
import sprite as s




class Game():
    def __init__(self, size):
        self.a, self.b = size
        self.x, self.y = (self.a / 5,self.b / 2.9)
        print(self.x,self.y)
        self.sprite = s.PxSprite(ctrl.Action.NONE, 0,self.x,self.y,0,0,30)

    def run_game(self):
        pyxel.init(self.a, self.b,fps=60)
        pyxel.load("adv1.pyxres")
        pyxel.run(self.update, self.draw)

    def draw(self):
        pyxel.cls(1)
        #pyxel.bltm()
        self.sprite = s.draw_sprite(self.sprite)

    def update (self):
        dir = ctrl.get_action ()
        s.move_sprite (dir, self.sprite)


if __name__ == "__main__":
    size = (160,120)
    g = Game(size)
    g.run_game()