from pynput.keyboard import Key, KeyCode

from ActionCoder import ActionCoder
from keyboard.KeyboardAction import KeyboardAction
from keyboard.KeyboardEvent import KeyboardEvent


class KeyboardActionCoder(ActionCoder):

    def encode(self, value: Key, event: KeyboardEvent):
        return f'keyboard {event.value}: {value}\n'

    def decode(self, command: str):
        command = command.replace('keyboard ', '').replace('\n', '')
        split = command.split(': ')
        virtual_key = int(split[1])
        return KeyboardAction(key=KeyCode.from_vk(vk=virtual_key), event=KeyboardEvent(split[0]))
