from mouse.MouseListener import MouseListener

if __name__ == '__main__':
    mouse_listener = MouseListener(output_file='../../mouse.txt')
    mouse_listener.start()
    mouse_listener.stop()