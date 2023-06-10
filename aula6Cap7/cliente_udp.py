# APLICAÇÃO CLIENTE COM UDP
# Faz ligação com o arquivo "servido_udp.py"
# Rodar primeiro o servidor_tcp.py e depois este arquivo.
# Funcionou atraves do debug. Procurando outras formas...

from socket import *

servidor="127.0.0.1"
porta=43210

obj_socket = socket(AF_INET, SOCK_DGRAM)
obj_socket.connect((servidor, porta))
saida=""

while saida!="X":
    msg = input("Sua mensagem: ")
    obj_socket.sendto(msg.encode(), (servidor,porta))
    dados, origem = obj_socket.recvfrom(65535)
    print("Resposta do Servidor: ", dados.decode())
    saida=input("Digite <X> para sair: ").upper()
obj_socket.close()

# Explicação linha à linha:

# from socket import *: Esta linha importa todas as classes e funções do módulo socket, que é usado para criar aplicativos de rede.

# servidor = "127.0.0.1": Aqui, definimos o endereço IP do servidor como "127.0.0.1", que é o endereço IP local (localhost).

# porta = 43210: Define a porta em que o servidor está escutando as conexões.

# obj_socket = socket(AF_INET, SOCK_DGRAM): Cria um objeto de socket utilizando a classe socket importada anteriormente. O argumento AF_INET especifica o uso do protocolo de endereçamento IPv4, e SOCK_DGRAM indica que será usado o protocolo UDP (User Datagram Protocol).

# obj_socket.connect((servidor, porta)): Estabelece a conexão do socket com o endereço IP do servidor e a porta especificados.

# saida = "": Inicializa uma variável chamada saida com uma string vazia.

# while saida != "X":: Inicia um loop que continuará até que a variável saida seja igual a "X".

# msg = input("Sua mensagem: "): Solicita ao usuário que digite uma mensagem para enviar ao servidor.

# obj_socket.sendto(msg.encode(), (servidor, porta)): Envia a mensagem digitada pelo usuário para o servidor. A mensagem é convertida em bytes usando o método encode().

# dados, origem = obj_socket.recvfrom(65535): Aguarda a chegada de dados do servidor. A função recvfrom() recebe os dados e o endereço de origem da mensagem.

# print("Resposta do Servidor: ", dados.decode()): Exibe no console a resposta recebida do servidor, convertendo-a de bytes para uma representação de string usando o método decode().

# saida = input("Digite <X> para sair: ").upper(): Solicita ao usuário que digite "X" para sair do programa. A resposta é convertida para letras maiúsculas usando o método upper().

# obj_socket.close(): Encerra a conexão do socket.

# Esse código implementa um cliente UDP que se conecta a um servidor, permite ao usuário enviar mensagens 
    # para o servidor e exibe a resposta recebida. O loop continua até que o usuário digite "X" para sair.