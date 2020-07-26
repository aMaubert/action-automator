from pynput.keyboard import Controller

from Action import Action
from keyboard.KeyboardEvent import KeyboardEvent


class KeyboardAction(Action):

    def __init__(self, key, event: KeyboardEvent):
        self.key = key
        self.event = event
        self.controller = Controller()

    def execute(self):
        if self.event == KeyboardEvent.Press:
            self.controller.press(key=self.key)
        else:
            self.controller.release(key=self.key)

    def __str__(self):
        return f'KeyboardAction( key={self.key}, event={self.event.value})'