#from PySide2.QtWidgets import *

EVENT_UI_CLOSING = "UI_CLOSING"

class Event:
    event_data = None
    program = None

    def __init__(self, program, *args):
        self.program = program
        self.event_data = list(args)




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

    def addCallbackStoreage(self, event_type:Event):
        self.event_and_callbacks

    def registerEvent(self, callback, event_type: Event = Event): # 나중에 처리가될 수 있는 이벤트를 등록시킴
        
        # print(str(self.event_and_callbacks.items()))



        self.event_and_callbacks[event_type].appand(callback)

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