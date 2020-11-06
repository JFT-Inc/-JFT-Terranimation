#from PySide2.QtWidgets import *

class Event:
    event_data = None
    program = None

    def __init__(self, program, *args):
        self.program = program
        self.event_data = list(args)

EVENT_UI_CLOSING = "UI_CLOSING"

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

class AbstractEventHandler:
    def handle(self, eventobject):
        pass

ec = locals()

class EventSquenceHandler:
    def __init__(self):
        self.EVENT_CLASS_LIST:list = list(filter(lambda p: type(p) == type, ec.values()))
        self.EVENT_CLASS_LIST.pop(len(self.EVENT_CLASS_LIST) - 1)
        self.EVENT_CLASS_LIST.pop(len(self.EVENT_CLASS_LIST) - 2)
        self.event_and_callbacks: dict(Event, list) = {} #

        for the_class in self.EVENT_CLASS_LIST:
            self.event_and_callbacks[the_class] = []
        self.event_handlers = []
        self.simple_event = []

    def registerEvent(self, callback, event_type = Event):
        #print(str(self.event_and_callbacks.items()))
        pass
        #self.event_and_callbacks[event_type].appand(callback)

    def registerEventHandler(self, eventHandler):
        self.event_handlers.append(eventHandler)

    def event_execution(self, event_object):
        for event_handler in self.event_handlers:
            event_handler.handle(event_object)

        for key_event_type in self.event_and_callbacks.keys():
            if isinstance(event_object, key_event_type):
                self.event_and_callbacks[key_event_type](event_object)

    def happen(self, event_object):
        self.event_execution(self, event_object)