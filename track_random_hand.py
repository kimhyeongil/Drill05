from pico2d import *
open_canvas()  
sprite = load_image('animation_sheet.png')
backGround = load_image('TUK_GROUND_FULL.png')
hand = load_image('hand_arrow.png')

clear_canvas()
backGround.draw(400,400)
sprite.draw(400,400)
hand.draw(400,400)
update_canvas()
delay(1)

close_canvas()