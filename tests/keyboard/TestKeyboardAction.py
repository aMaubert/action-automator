from keyboard.KeyboardActionCoder import KeyboardActionCoder

if __name__ == '__main__':
    keyboard_action_coder = KeyboardActionCoder()
    with open('../../keyboard.txt', 'r') as file:
        for line in file.readlines():
            keyboard_action = keyboard_action_coder.decode(command=line)
            keyboard_action.execute()