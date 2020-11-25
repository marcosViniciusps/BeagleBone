import socket
import time
import Adafruit_BBIO.UART as UART   #Configura e inicializa o canal UART
import serial
####################SERIAL##################################
#Habilita a comunicacao serial pela UART1 (pinos 24-TX e 26-RX para BBG)
UART.setup("UART1")
ser = serial.Serial(port = "/dev/ttyO1", baudrate=9600)
ser.close()
ser.open()
if ser.isOpen():
        print("Serial aberta!")
        ser.write("BBG!")   #Envia para arduino
####################SERVIDOR##################################
HOST = ''              # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     #Cria o mecanismo de Socket para receber a conecao
orig = (HOST, PORT)
texto = 'ACK'   #Mensagem que sera enviada para BBG
msg = 0     #Recebera a mensagem da BBG
while True:
        try:
            tcp.bind(orig)
            print('Aguardando comunicacao...')
        except:
            print('Tentando conectar!')
            time.sleep(1)
        else:
            break
tcp.listen(1)   #Define o limite de conexoes
while True:
    con, cliente = tcp.accept()     #Deixa o Servidor na escuta aguardando as conexoes
    print('Conectado por', cliente)     #Printa o ip do cliente conectado
    while True:
        try:
            msg = con.recv(1024)    #Aguarda um dado enviado pela rede de ate 1024 Bytes
            con.send(texto.encode('utf-8'))     #Codifica a variavel testo e a envia para o cliente
        except:
            print('Perda de comunicacao')
            time.sleep(2)
            break
        else:
            if msg == 'Break':
                print('Finalizando conexao do cliente'.format(cliente))
                print('Aguardando nova conexao...')
                con.close()
                break
            else:
                print('({}) enviou: {}'.format(cliente[0], msg))
                ser.write(msg)
                time.sleep(2)

