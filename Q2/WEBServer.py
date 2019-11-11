# import socket module
from socket import *
import sys  # para terminar o programa

serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepara o socket servidor
serverPort = 12000
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

while True:
    # Estabelece a conexão
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024)
        print(message)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        ht = 'HTTP/1.x 200 OK'
        # Envia um linha de cabeçalho HTTP para o socket
        connectionSocket.send(ht.encode('UTF-8'))
        # Envia o conteúdo do arquivo solicitado ao cliente
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode('UTF-8'))
        connectionSocket.close()
        print('File Recieved')

    except IOError:
        # Envia uma mensagem de resposta “File not Found”
        msgR = '404 Not Found'
        connectionSocket.send(msgR.encode('UTF-8'))
        print(msgR)
        # Fecha o socket cliente
        connectionSocket.close()

serverSocket.close()
sys.exit()  # Termina o programa depois de enviar os dados
