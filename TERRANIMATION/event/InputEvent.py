
from Terranimation.event.event import *

DEVICE_MOUSE        = 0b0001
DEVICE_KEYBOARD     = 0b0010

class InputEvent(Event):
    def __init__(self, current_widget, input_device):
        super.__init__(self, None, current_widget)

        self.device = input_device

class MouseClickEvent(InputEvent):
    def __init__(self, x, y, button, current_widget):
        super.__init__(self, current_widget, DEVICE_MOUSE)

        self.posX = x
        self.posY = y
        self.button = button

class MouseDragging(MouseClickEvent):
    def __init__(self, x, y, button, current_widget):
        super.__init__(self, x, y, button, current_widget)


