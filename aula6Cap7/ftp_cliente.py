# NAVEGANDO E ENVIANDO ARQUIVOS COM FTP

from ftplib import *

# ftp_ativo=False
ftp = FTP('ftp.ibiblio.org')
print(ftp.getwelcome())

usuario=input("Digite o usuario: ")
senha=input("Digite a senha: ")
ftp.login(usuario, senha)
print("Diretório atual de trabalho: ", ftp.pwd())

ftp.cwd('pub')
print("Diretório corrente: ", ftp.pwd())
ftp.quit()

# Este código estabelece uma conexão com um servidor FTP, solicita ao usuário as credenciais de login, 
    # realiza o login no servidor, exibe o diretório de trabalho atual antes e depois de alterá-lo e, em seguida, fecha a conexão FTP.


# Explicação linha à linha:

# from ftplib import *: Esta linha importa todas as classes e funções do módulo ftplib, que é usado para realizar operações FTP (File Transfer Protocol).

# ftp_ativo=False: Aqui, é criada uma variável booleana chamada ftp_ativo e é definida como False. Essa variável pode ser usada posteriormente para configurar o modo de transferência de dados do FTP, embora não seja utilizada neste código.

# ftp = FTP('ftp.ibiblio.org'): Cria um objeto FTP, estabelecendo uma conexão com o servidor FTP chamado "ftp.ibiblio.org". É possível fornecer o endereço IP ou o nome do domínio do servidor FTP.

# print(ftp.getwelcome()): Exibe uma mensagem de boas-vindas recebida do servidor FTP. A função getwelcome() retorna essa mensagem.

# usuario = input("Digite o usuario: "): Solicita ao usuário que digite o nome de usuário para fazer o login no servidor FTP. A resposta do usuário é armazenada na variável usuario.

# senha = input("Digite a senha: "): Solicita ao usuário que digite a senha para fazer o login no servidor FTP. A resposta do usuário é armazenada na variável senha.

# ftp.login(usuario, senha): Realiza o login no servidor FTP usando as credenciais fornecidas pelo usuário. O nome de usuário é passado como o primeiro argumento e a senha como o segundo argumento.

# print("Diretório atual de trabalho: ", ftp.pwd()): Exibe o diretório de trabalho atual do servidor FTP. A função pwd() retorna o diretório atual.

# ftp.cwd('pub'): Altera o diretório de trabalho para o diretório 'pub' no servidor FTP. A função cwd() é usada para alterar o diretório.

# print("Diretório corrente: ", ftp.pwd()): Exibe o diretório de trabalho atual após a alteração. Mais uma vez, a função pwd() é usada para obter o diretório atual.

# ftp.quit(): Encerra a conexão com o servidor FTP e finaliza a sessão FTP.
