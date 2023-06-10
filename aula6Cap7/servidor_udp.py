# APLICAÇÃO SERVIDORA COM UDP
from socket import *

servidor="127.0.0.1"
porta=43210

obj_socket = socket(AF_INET, SOCK_DGRAM)
obj_socket.bind((servidor,porta))
print("Servidor pronto....")

while True:
    dados, origem = obj_socket.recvfrom(65535)
    print("Origem..........: ", origem)
    print("Dados recebidos.: ", dados.decode())
    resposta=input("Digite a resposta: ")
    obj_socket.sendto(resposta.encode(), origem)

obj_socket.close()

# Explicação linha à linha:

# from socket import *: Esta linha importa todas as classes e funções do módulo socket, que é usado para criar aplicativos de rede.

# servidor = "127.0.0.1": Aqui, é definido o endereço IP do servidor como "127.0.0.1", que é o endereço IP local (localhost).

# porta = 43210: Define a porta em que o servidor irá escutar as conexões.

# obj_socket = socket(AF_INET, SOCK_DGRAM): Cria um objeto de socket utilizando a classe socket importada anteriormente. O argumento AF_INET especifica o uso do protocolo de endereçamento IPv4, e SOCK_DGRAM indica que será usado o protocolo UDP (User Datagram Protocol).

# obj_socket.bind((servidor, porta)): Associa o objeto de socket ao endereço IP do servidor e à porta definida anteriormente. Dessa forma, o servidor ficará escutando as conexões nesse endereço e porta específicos.

# print("Servidor pronto...."): Exibe a mensagem "Servidor pronto..." no console.

# while True:: Inicia um loop infinito para que o servidor fique sempre aguardando por novas conexões.

# dados, origem = obj_socket.recvfrom(65535): Aguarda a chegada de dados vindos de um cliente. A função recvfrom() recebe os dados e o endereço de origem da mensagem.

# print("Origem..........: ", origem): Exibe no console o endereço de origem da mensagem recebida.

# print("Dados recebidos.: ", dados.decode()): Exibe no console os dados recebidos, convertendo-os de bytes para uma representação de string utilizando o método decode().
 
# resposta = input("Digite a resposta: "): Solicita ao usuário que digite uma resposta para enviar ao cliente.

# obj_socket.sendto(resposta.encode(), origem): Envia a resposta digitada pelo usuário de volta para o cliente, utilizando o método sendto(). A resposta é convertida para bytes utilizando o método encode().

# obj_socket.close(): Encerra a conexão do socket.

# Esse código implementa um servidor UDP simples que aguarda a chegada de mensagens de clientes, 
        # exibe as informações da mensagem recebida, solicita uma resposta do usuário 
            # e envia essa resposta de volta para o cliente. 
        # O servidor continua aguardando por novas mensagens em um loop infinito até que seja interrompido.