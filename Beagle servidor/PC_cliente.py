import socket
import time
HOST = '172.20.0.178'     # Endereco IP do Servidor
PORT = 5000              # Porta que o Servidor esta
msg = ' '
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    try:
        dest = (HOST, PORT)
        tcp.connect(dest)
    except:
        print('\033[1;30m Tentando conecxão com {}...\033[0;0m'.format(HOST))
        time.sleep(2)
    else:
        print('-'*30)
        print('\033[1;32m \t\tConectado!\033[0;0m')
        print('-'*30)
        print('\t\033[1;34m Para sair digite "Break"\033[0;0m')
        print('-' * 30)
        while msg != 'Break':
            print('Digite sua mensagem: ')
            msg = input()
            try:
                tcp.send(msg.encode('utf-8'))   # Envia para o ervidor a mensagem digitada pelo cliente
                data = tcp.recv(1024).decode()  # Lê mensagem enviada pelo servidor
                print('O servidor enviou: {}'.format(data))
            except:
                print('-' * 30)
                print('\t \033[1;31m Falha na comunicação!\033[0;0m')
                print('-' * 30)
                break
        if msg == 'Break':
            print('\033[1;30m Comunicação com {} encerrada!\033[0;0m'.format(HOST))
            tcp.close()
            break
