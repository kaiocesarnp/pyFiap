# APLICAÇÃO CLIENTE COM TCP
# Faz ligação com o arquivo "servido_tcp.py"
# Rodar primeiro o servidor_tcp.py e depois este arquivo.
# Funcionou atraves do debug. Procurando outras formas...

from socket import *

servidor="127.0.0.1"
porta=43210

msg = bytes(input("Digite algo: "), 'utf-8')
obj_socket=socket(AF_INET, SOCK_STREAM)
obj_socket.connect((servidor,porta))
obj_socket.send(msg)
resposta=obj_socket.recv(1024)

print("Recebemos: ", resposta)

obj_socket.close()