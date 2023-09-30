from pico2d import *
import random
class Player:
    def __init__(self):
        self.sprite = load_image('animation_sheet.png')
        self.pos = [get_canvas_width() // 2, get_canvas_height() // 2]
        self.nFrame, self.frame = 8, 0
    
    def draw(self):
        x, y = 0, 1
        self.sprite.clip_draw(self.frame * 100, 0, 100, 100, self.pos[x], self.pos[y])
        self.frame = (self.frame + 1) % self.nFrame


class Hand:
    def __init__(self):
        self.img = load_image('hand_arrow.png')
        self.set_random_pos()
    
    def set_random_pos(self):
        self.pos = [random.randint(0 + self.img.w, get_canvas_width() - self.img.w), random.randint(0 + self.img.h, get_canvas_height() - self.img.h)]
        
    def draw(self):
        x, y = 0, 1
        self.img.draw(self.pos[x], self.pos[y])


class GameManager:
    def __init__(self):
        open_canvas(1024,720)
        self.backGround = load_image('TUK_GROUND_FULL.png')
        self.hand = Hand()
        self.w, self.h = 1024, 720
        self.player = Player()
        resize_canvas(self.w, self.h)
    
    def render(self):
        clear_canvas()
        self.backGround.draw(self.w // 2, self.h // 2)
        self.player.draw()
        self.hand.draw()
        update_canvas()
        delay(0.1)


GM = GameManager()

while True:
    GM.render()
delay(1)

close_canvas()