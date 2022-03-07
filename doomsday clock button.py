import random
import pyglet
import time
from pyglet.window import key, Window
from pyglet.gl import *
import winsound

game_window = Window(1280, 720, "Морской бой") 
pyglet.gl.glClearColor(0.5,0.5,0.5,1)
batch = pyglet.graphics.Batch()
layer_00 = pyglet.graphics.OrderedGroup(0)
layer_01 = pyglet.graphics.OrderedGroup(1)
start = False
class Text_info(pyglet.text.Label):
    def __init__(self, text_descr="", text_value = "", x = 0, y = 0):
        self.text_descr = text_descr
        super(Text_info, self).__init__(text = self.text_descr + ": " + text_value,
                                                        font_name = 'Times New Roman',
                                                        font_size = 24,
                                                        
                                                        x = x,
                                                        y = y,
                                                        anchor_x = 'left',
                                                        anchor_y = 'baseline',
                                                        batch = batch)
                                                        
    def update(self, text_value_new = ""):
        self.text = self.text_descr + ": " + text_value_new

class Main_game:
    def __init__(self):
        self.__clicks_made = 0
        self._info_ship = Text_info(text_descr = "Кликов", x = 400, y = 300)

    @property
    def clicks_made(self):
        return self.__clicks_made

    @clicks_made.setter
    def clicks_made(self, value):
        self.__clicks_made = value
        self._info_ship.update(str(self.__clicks_made))        
mg = Main_game()

class button(pyglet.sprite.Sprite):
    def __init__(self, img_file = "images/button2.png", x = 300, y = game_window.height - 140, batch = batch):
        img = pyglet.image.load(img_file)
        img.anchor_x = img.width // 2
        img.anchor_y = img.height // 2                        
        super(button, self).__init__(img, x = x, y = y, batch = batch) 

    def on_press(self, img_file = "images/button_pressed.png", x = 300, y = game_window.height - 159, batch = batch):
        global pressed
        img = pyglet.image.load(img_file)
        img.anchor_x = img.width // 2
        img.anchor_y = img.height // 2                         
        super(button, self).__init__(img, x = x, y = y, batch = batch) 
        self.visible = True
        pressed = True

    def reset(self, img_file = "images/button2.png", x = 300, y = game_window.height - 140, batch = batch):
        global pressed, bt
        img = pyglet.image.load(img_file)
        img.anchor_x = img.width // 2
        img.anchor_y = img.height // 2                        
        bt = button()
        pressed = False


class arrow(pyglet.sprite.Sprite):
    def __init__(self, img_file = "images/arrow.png", x = game_window.width - 250, y = game_window.height - 300, batch = batch):
        img = pyglet.image.load(img_file)
        img.anchor_x = img.width // 2
        img.anchor_y = 14                        
        super(arrow, self).__init__(img, x = x, y = y, batch = batch, group = layer_01)
        self.rotation = 30 
        pyglet.clock.schedule_interval(self.move_arrow, 1 / 5)

    def move_arrow(self, dt):
        if self.rotation > 300:
            self.rotation -= 2.4
        elif self.rotation > 250:
            self.rotation -= 1.5
        elif self.rotation > 180:
            self.rotation -= 0.5
        
class hour_hand(pyglet.sprite.Sprite):
    def __init__(self, img_file = "images/hour_hand.png", x = game_window.width - 250, y = game_window.height - 300, batch = batch):
        img = pyglet.image.load(img_file)
        img.anchor_x = img.width // 2
        img.anchor_y = 14                        
        super(hour_hand, self).__init__(img, x = x, y = y, batch = batch, group = layer_01)
        self.rotation = 315 
        pyglet.clock.schedule_interval(self.move_arrow, 1 / 5)
    
    def move_arrow(self, dt):
        self.rotation = 315 + ar.rotation / 12



class clock(pyglet.sprite.Sprite):
    def __init__(self, img_file = "images/clock.png", x = game_window.width - 250, y = game_window.height - 300, batch = batch):
        img = pyglet.image.load(img_file)
        img.anchor_x = img.width // 2
        img.anchor_y = img.height // 2                  
        super(clock, self).__init__(img, x = x, y = y, batch = batch, group = layer_00) 

cl = clock()
ar = arrow()
hr = hour_hand()
bt = button()

@game_window.event
def on_mouse_press(x, y, button, modifiers):
    global press_time, start
    if bt.x + bt.width // 2 > x > bt.x - bt.width // 2 and \
       bt.y + bt.height // 2 > y > bt.y - bt.height // 2 and button == pyglet.window.mouse.LEFT:
        winsound.PlaySound('button_click', winsound.SND_ASYNC | winsound.SND_FILENAME)
        mg.clicks_made += 1
        ar.rotation += -ar.rotation % 360 / 13     
        bt.visible = False
        press_time = time.time() + 0.5
        bt.on_press()
        start = True

@game_window.event 
def on_draw():
    game_window.clear()    
    batch.draw() 


@game_window.event    
def depress(dt):
    if start and time.time() > press_time and pressed:
        bt.visible = False
        bt.reset()

pyglet.clock.schedule_interval(depress, 1 / 80)
pyglet.app.run()