from Terranimation.event.event import *


class UiEvent(Event):
    gui = None

    def __init__(self, args, widget, event_code:str):
        super.__init__(self, args)
        self.gui = widget
        self.name = event_code

class ButtonPressedEvent(UiEvent):
    pressed_button = None

    def __init__(self, args, widget, button_type):
        super.__init__(self, args, widget)
        self.pressed_button = button_type

class TopBarButtonPressedEvent(ButtonPressedEvent):
    EXIT_BUTTON = 0

    def __init__(self, args, widget, button_type):
        super.__init__(self, args, widget, button_type)
        if button_type not in {0, 1, 2}:
            print("Warning: Unpopular button from the top bar")

    def close(self):
        self.gui.close()