# encoding: utf-8
# o modulo socket e a base para toda a comunicacao Python em rede
from socket import *
from datetime import datetime
# o nome ou IP do servidor. Se nome, uma consulta DNS sera realizada. Porta do servidor.
serverName = 'localhost'
serverPort = 12000
# cria um socket cliente. o primeiro parametro indica que o endereco e o IPv4. o segundo indica que e UDP
# se a porta nao e especificada, o SO escolhe uma aleatoria
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)
# input() espera uma entrada do teclado para formar a msg
# '''receba uma mensagem do teclado para a mensagem (message) a ser enviada
message = 'Hello'
# envia a msg. .encode() transforma a string em bytes. as informacoes de ip de origem e porta tambem
# estao contidas na mensagem
# #clientSocket.sendto(message.encode(),(serverName, serverPort))
# recebe a msg. modifiedMessage guarda a msg e serverAddress guarda o ip e porta do servidor (nao e necessario)
# buffer de 2048
pings_numbers = 1

for pings_numbers in range(1, 11):
    time_envio = datetime.now()
    clientSocket.sendto(message.encode(), (serverName, serverPort))

    try:
        time_recebido = datetime.now()
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
        RTT = time_recebido - time_envio
        print("Ping ", pings_numbers, "hora: ", time_envio.hour, ":",
              time_envio.minute, ":", time_envio.second, " RTT: ", RTT, "segundos")
    except timeout:
        print("Solicitação expirada")
        continue
    pings_numbers += 1
# try:
    # modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
# imprime a msg recebida do servidor
# m = modifiedMessage.decode()

# print(m)
# fecha o socket
clientSocket.close()
