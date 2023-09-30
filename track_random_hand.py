from pico2d import *
open_canvas()  

backGround = load_image('TUK_GROUND_FULL.png')
hand = load_image('hand_arrow.png')

class Player:
    def __init__(self):
        self.sprite = load_image('animation_sheet.png')
        self.pos = [get_canvas_width() // 2, get_canvas_height() // 2]
    def draw(self):
        x, y = 0, 1
        self.sprite.clip_draw(0, 0, 100, 100, self.pos[x], self.pos[y])
clear_canvas()
backGround.draw(400,400)
player = Player()
player.draw()
hand.draw(400,400)
update_canvas()
delay(1)

close_canvas()