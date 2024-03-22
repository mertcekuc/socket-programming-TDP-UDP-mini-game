import socket
import time
import random


def makeit_lost():
    lost = input("Do you want to make it lost? (y/n): ")
    if lost == 'y':
        return True
    else:
        return False


def makeit_timeout():
    timeout = input("Do you want to send message? (y/n): ")
    if timeout == 'n':
        return True
    else:
        return False


def auto_lost():
    prob = random.random()

    if prob <= 0.1:
        return True

    return False


def auto_timeout():
    prob = random.random()

    if prob <= 0.1:
        return True

    return False


def manual():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    port = 12345

    try:
        s.bind(('127.0.0.1', port))
        'Socket Created'
    except socket.error as e:
        print(str(e))

    print("Waiting for a connection")
    msg, adr = s.recvfrom(1024)
    msg = msg.decode()
    last_seq, last_ack, datalength = msg.split(',')

    print(f"RECEIVED SEQ: {last_seq}\nRECEIVED ACKr: {last_ack}\nDATALENGTH: {datalength}")
    print('=====================================================')

    datalength = int(datalength)

    turn = 0

    while True:

        seq = input('SENT SEQ:')
        ack = input('SENT ACK:')
        print('=====================================================')

        if last_seq == 'lost':
            correct_seq = int(last_ack)
            correct_ack = correct_ack

        elif msg == 'timeout':
            correct_seq = correct_seq
            correct_ack = correct_ack
        else:
            correct_seq = int(last_ack)
            correct_ack = int(last_seq) + datalength

        if int(seq) == correct_seq and int(ack) == correct_ack:
            if turn >= 1:
                if makeit_timeout():
                    s.sendto("timeout".encode(), adr)
                    turn += 1
                    print('No Message Sent')
                    print('=====================================================')

                elif makeit_lost():
                    s.sendto(f"lost,{ack}".encode(), adr)
                    print('=====================================================')
                    turn += 1
                else:
                    s.sendto(f"{seq},{ack}".encode(), adr)
                    print('=====================================================')
                    turn += 1

            else:
                s.sendto(f"{seq},{ack}".encode(), adr)
                turn += 1

        else:
            print("Incorrect")
            print(f"Correct SEQ: {correct_seq}\nCorrect ACK: {correct_ack}")
            print("\nGame Over")
            print('=====================================================')
            s.sendto(f"win".encode(), adr)
            break

        msg, adr = s.recvfrom(1024)
        msg = msg.decode()

        if msg == "win":
            print("You win the game")
            print('=====================================================')
            break
        elif msg != 'timeout':
            last_seq, last_ack = msg.split(',')
            print(f"RECEIVED SEQ: {last_seq}\nRECEIVED ACK: {last_ack}")
            print('=====================================================')

        else:
            time.sleep(5)
            print("timeout")
            print('=====================================================')


def auto():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    port = 12345

    try:
        s.bind(('127.0.0.1', port))
    except socket.error as e:
        print(str(e))

    print("Waiting for a connection")
    msg, adr = s.recvfrom(1024)
    msg = msg.decode()
    time.sleep(3)
    last_seq, last_ack, datalength = msg.split(',')
    print(f"RECEIVED SEQ: {last_seq}\nREECIVED ACK: {last_ack}\nDATALENGTH: {datalength}")
    print('=====================================================')
    datalength = int(datalength)

    turn = 0

    while True:

        if last_seq == 'lost':
            correct_seq = int(last_ack)
            correct_ack = correct_ack

        elif msg == 'timeout':
            correct_seq = correct_seq
            correct_ack = correct_ack
        else:
            correct_seq = int(last_ack)
            correct_ack = int(last_seq) + datalength

        seq = correct_seq
        ack = correct_ack

        if turn >= 1:
            if auto_timeout():
                time.sleep(3)
                s.sendto("timeout".encode(), adr)
                print('No Message Sent')
                print('=====================================================')
                turn += 1

            elif auto_lost():
                time.sleep(3)
                s.sendto(f"lost,{ack}".encode(), adr)
                print(f"SENT SEQ:{seq}\nSENT ACK:{ack}")
                print('=====================================================')
                turn += 1

            else:
                time.sleep(3)
                s.sendto(f"{seq},{ack}".encode(), adr)
                print(f"SENT SEQ:{seq}\nSENT ACK:{ack}")
                print('=====================================================')
                turn += 1

        else:
            time.sleep(3)
            s.sendto(f"{seq},{ack}".encode(), adr)
            print(f"SENT SEQ:{seq}\nSENT ACK:{ack}")
            print('=====================================================')
            turn += 1

        msg, adr = s.recvfrom(1024)
        msg = msg.decode()

        if msg == "win":
            print("You win the game")
            break
        elif msg != 'timeout':
            last_seq, last_ack = msg.split(',')
            time.sleep(3)
            print(f"RECEIVED SEQ: {last_seq}\nRECEIVED ACK: {last_ack}")
            print('=====================================================')
        else:
            time.sleep(3)
            print("timeout")
            print('=====================================================')


