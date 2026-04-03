import sys


CODIGO_ENCERRAMENTO = 'exit'

def main() -> None:
    try:
        while True:
            user_input = str(input("> "))
            if user_input == CODIGO_ENCERRAMENTO:
                sys.exit(0)
            
            print(f'[user]: {user_input}')
            print(f'[machine]: What else would you like to talk about?')
    except KeyboardInterrupt:
        print('[machine]: Encerrando conversa...')

if __name__ == '__main__':
    main()