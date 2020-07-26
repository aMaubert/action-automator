import sys

from pynput.mouse import Listener


class MouseListener:

    def __init__(self, output_file: str):
        self.file = None
        try:
            self.file = open(output_file, mode='w', encoding='utf-8')
        except ValueError:
            print('error : text.txt doesn\' exists .', file=sys.stderr)
        self.listener = Listener(on_move=self.on_move,
                                 on_click=self.on_click)

    def on_move(self, x, y):
        self.file.write(f'mouse move: ({x},{y})\n')

    def on_click(self, x, y, button, pressed):
        if pressed:
            self.file.write(f'mouse pressed {button}: ({x},{y})\n')
        else:
            self.file.write(f'mouse released {button}: ({x},{y})\n')

    def start(self):
        self.listener.start()
        self.listener.join()

    def stop(self):
        self.listener.stop()
        self.file.close()



