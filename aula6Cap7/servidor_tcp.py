from socket import * # importa todos os métodos da biblioteca socket

servidor = "127.0.0.1" #localhost
porta = 43210 #porta de entrada

obj_socket = socket(AF_INET, SOCK_STREAM) #AF_INET = tipo de identificação com o servidor, utilizando o IP/Dominio dele. SOCK_STREAM = feito para trabalhar com o TCP
obj_socket.bind((servidor,porta))
obj_socket.listen(2) #quantidade máxima de clientes que a aplicação vai conseguir receber uma conexão
print("Aguardando cliente....")

while True: #laço eterno
    con, cliente = obj_socket.accept() #o accept fica 'travado' esperando um cliente se conectar. Quando o cliente se conecta, ele continua executando e retorna uma tupla "con" = conexao e a identificação do "cliente"
    print("Conectado com: ", cliente)
    while True:
        msg_recebida = str(con.recv(1024))
        print("Recebemos: ", msg_recebida)
        msg_enviada = b'Olah cliente'
        con.send(msg_enviada)
        break
    con.close()

    # EXPLICAÇÃO LINHA POR LINHA:

# 1. `from socket import *`: Essa linha importa todas as funções e classes do módulo `socket`, permitindo que sejam utilizadas diretamente sem a necessidade de prefixar com o nome do módulo.

# 2. `servidor="127.0.0.1"`: Essa linha atribui o endereço IP do servidor à variável `servidor`. Nesse caso, o endereço IP é `127.0.0.1`, que se refere ao localhost.

# 3. `porta=43210`: Essa linha atribui o número da porta utilizada para a comunicação ao servidor à variável `porta`. Nesse caso, a porta é `43210`.

# 4. `obj_socket = socket(AF_INET, SOCK_STREAM)`: Essa linha cria um objeto de socket TCP/IP através da chamada da função `socket` com dois argumentos: `AF_INET` indica que será utilizado o protocolo de endereços IP, e `SOCK_STREAM` indica que será utilizado o protocolo de transporte TCP.

# 5. `obj_socket.bind((servidor,porta))`: Essa linha associa o objeto de socket a um endereço IP e número de porta específicos. No caso, é utilizado o endereço IP e porta armazenados nas variáveis `servidor` e `porta`.

# 6. `obj_socket.listen(2)`: Essa linha coloca o objeto de socket em modo de escuta para conexões de clientes. O argumento `2` indica que a fila de conexões pendentes pode conter até 2 conexões.

# 7. `print("Aguardando cliente....")`: Essa linha exibe a mensagem "Aguardando cliente...." na tela, indicando que o servidor está esperando por conexões de clientes.

# 8. `while True:`: Essa linha inicia um loop infinito, permitindo que o servidor fique sempre esperando por conexões de clientes.

# 9. `con, cliente = obj_socket.accept()`: Essa linha aguarda a conexão de um cliente e aceita a conexão quando esta ocorre. A função `accept` retorna um novo objeto de socket (`con`) e o endereço (`cliente`) do cliente conectado.

# 10. `print("Conectado com: ", cliente)`: Essa linha exibe na tela a mensagem "Conectado com:" seguida do endereço do cliente que se conectou.

# 11. `while True:`: Essa linha inicia um loop infinito para tratar as mensagens recebidas do cliente.

# 12. `msg_recebida = str(con.recv(1024))`: Essa linha recebe uma mensagem do cliente utilizando o objeto de socket `con` e armazena a mensagem na variável `msg_recebida`. A função `recv` é usada para receber dados do cliente, e o argumento `1024` define o tamanho máximo da mensagem que será recebida.

# 13. `print("Recebemos: ", msg_recebida)`: Essa linha exibe na tela a mensagem "Recebemos:" seguida do conteúdo da mensagem recebida do cliente.

# 14. `msg_enviada = b'Olah cliente'`: Essa linha atribui a mensagem de resposta que será enviada ao cliente à variável `msg_enviada`. Nesse caso, a mensagem é "Olah cliente" codificada em bytes.

# 15. `con.send(msg_enviada)`: Essa linha envia a mensagem de resposta ao cliente utilizando o objeto de socket `con