import sys

from pynput.keyboard import Listener, Key

from ActionCoder import ActionCoder
from keyboard.KeyboardEvent import KeyboardEvent


def get_vk(key):
    """
    Get the virtual key code from a key.
    These are used so case/shift modifications are ignored.
    """
    return key.vk if hasattr(key, 'vk') else key.value.vk


class KeyboardListener:
    def __init__(self, output_file: str, action_coder: ActionCoder):
        self.file = None
        try:
            self.file = open(output_file, mode='w', encoding='utf-8')
        except ValueError:
            print('error : keyboard.txt doesn\' exists .', file=sys.stderr)
        self.action_coder = action_coder
        self.listener = Listener(on_press=self.on_press,
                                 on_release=self.on_release)

    def on_press(self, key):
        if key == Key.esc:
            # Stop listener
            return False
        """ When a key is pressed """
        vk = get_vk(key)  # Get the key's vk
        try:
            self.file.write(self.action_coder.encode(value=vk, event=KeyboardEvent.Press))
        except AttributeError:
            print('special key {0} pressed'.format(key))

    def on_release(self, key):
        if key == Key.esc:
            # Stop listener
            return False
        vk = get_vk(key)  # Get the key's vk
        self.file.write(self.action_coder.encode(value=vk, event=KeyboardEvent.Release))

    def start(self):
        self.listener.start()
        self.listener.join()

    def stop(self):
        self.listener.stop()
        self.file.close()
