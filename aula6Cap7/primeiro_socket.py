import socket

resp = "S"
while(resp=="S"):
    url = input("Digite uma url: ")
    ip = socket.gethostbyname(url)
    print("O IP referente à url informada é: ", ip)
    resp = input("Digite <s> para continuar: ").upper()

# EXPLICAÇÃO LINHA À LINHA:

# import socket: Essa linha importa o módulo socket, que fornece funcionalidades para a comunicação em rede.

# resp = "S": Essa linha atribui a string "S" à variável resp, que será usada para controlar a repetição do loop.

# while(resp=="S"):: Essa linha inicia um loop while que continuará executando enquanto o valor da variável resp for igual a "S".

# url = input("Digite uma url: "): Essa linha solicita ao usuário que digite uma URL e armazena o valor inserido na variável url.

# ip = socket.gethostbyname(url): Essa linha utiliza a função gethostbyname do módulo socket 
            # para obter o endereço IP correspondente à URL fornecida pelo usuário. O IP é armazenado na variável ip.

# print("O IP referente à url informada é: ", ip): Essa linha exibe na tela a mensagem 
            # "O IP referente à URL informada é: " seguida do valor da variável ip, ou seja, o endereço IP correspondente à URL fornecida.

# resp = input("Digite <s> para continuar: ").upper(): Essa linha solicita ao usuário que digite 
            # "s" para continuar ou qualquer outra tecla para sair. A função input é utilizada para obter a entrada do usuário, e o método .upper() é aplicado para converter a entrada para letras maiúsculas. O valor inserido pelo usuário é atribuído à variável resp, atualizando assim a condição de saída do loop.