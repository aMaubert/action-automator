from pyautogui import press, write, moveTo, leftClick, drag, size, position


def launch_paint():
    press('winleft')
    write('paint')
    press('enter')

    moveTo(70, 30)

    leftClick()
    moveTo(330, 68)

    leftClick()

    moveTo(50, 100)

    distance = 200
    while distance > 0:
        drag(distance, 0, duration=0.5)  # move right
        distance -= 5
        drag(0, distance, duration=0.5)  # move down
        drag(-distance, 0, duration=0.5)  # move left
        distance -= 5
        drag(0, -distance, duration=0.5)  # move up


if __name__ == '__main__':
    launch_paint()
    print(size())