from pico2d import *
open_canvas()  

backGround = load_image('TUK_GROUND_FULL.png')
hand = load_image('hand_arrow.png')

class Player:
    def __init__(self):
        print("class Player construct")
clear_canvas()
backGround.draw(400,400)
player = Player()
hand.draw(400,400)
update_canvas()
delay(1)

close_canvas()