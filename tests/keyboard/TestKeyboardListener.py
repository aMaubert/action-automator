from keyboard.KeyboardActionCoder import KeyboardActionCoder
from keyboard.KeyboardListener import KeyboardListener

if __name__ == '__main__':
    keyboard_listener = KeyboardListener( output_file='../../keyboard.txt',
                                          action_coder=KeyboardActionCoder())
    keyboard_listener.start()
    keyboard_listener.stop()
