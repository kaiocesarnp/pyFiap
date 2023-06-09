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