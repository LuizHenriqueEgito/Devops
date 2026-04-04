from pathlib import Path

FILE_PATH = Path('/data/messages.txt')

def write_msg():
    msg = input('Digite a mensagem: ')
    FILE_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(FILE_PATH, 'a') as file:
        file.write(msg + '\n')

def show_msg():
    if not FILE_PATH.exists():
        print('<vazio>')
        return None

    with open(FILE_PATH, 'r') as file:
        msgs = file.readlines()
    for line, msg in enumerate(msgs, 1):
        print(f'[{line}] > {msg.strip()}')

def main():
    while True:
        print('\n')
        print('*' * 30)
        print('1. Write message')
        print('2. Show messages')
        print('3. Exit')
        print('*' * 30)
        print('\n')
        option = int(input("User choice: "))

        match option:
            case 1:
                write_msg()
            case 2:
                show_msg()
            case 3:
                break
            case _:
                print('Invalid Option')

if __name__ == '__main__':
    main()
        