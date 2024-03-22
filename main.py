import server
import client

def main():
    side = (input('1-Server[s]\n2-Client[c]\nSelect side: '))
    print('\n')
    mode = (input('1-Auto[a]\n2-Manual[m]\nSelect mode: '))
    print('=====================================================')
    if side == '1' or side == 's':
        if mode == '1' or mode == 'a':
            print('Server is running in auto mode...')
            server.auto()
        elif mode == '2' or mode == 'm':
            print('Server is running in manual mode...')
            server.manual()
    elif side == '2' or side == 'c':
        if mode == '1' or mode == 'a':
            print('Client is running in auto mode...')
            client.auto()
        elif mode == '2' or mode == 'm':
            print('Client is running in manual mode...')
            client.manual()

if __name__ == '__main__':
    main()