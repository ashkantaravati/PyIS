def mock_func():
    """Does something. """
    print(f'mock function')


COMMANDS = {
    ".index":mock_func,
    ".find":mock_func,
    ".create":mock_func,
    ".delete":mock_func,
    ".update":mock_func,
    ".quit":lambda: exit(0)

}
def available_commands():
    return list(COMMANDS)

def show_greetings():
    print("mock greetings")
    print("available mock commands:")
    for command in available_commands():
        print(f"{command:<15}{COMMANDS[command].__doc__}")

def main():
    show_greetings()
    while True:
        cmd = input('cmd> ')
        if cmd in available_commands():
            action = COMMANDS[cmd]
            action()
            print()
        else:
            print('Wrong command')







if __name__ == '__main__':
    main()
