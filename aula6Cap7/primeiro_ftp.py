# INTRODUÇÃO AO FTP

from ftplib import *

# ftp_ativo=False

ftp = FTP('ftp.ibiblio.org')

print(ftp.getwelcome())

ftp.quit()

# Ao dar print e aparecer '220 ProFTPD Server', significa que foi conectado com sucesso ao servidor e pode começar 
        # a transferência de arquivos. Principalmente em relação ao 220, que é o status

# Esse código estabelece uma conexão com um servidor FTP usando o módulo ftplib, exibe uma 
        # mensagem de boas-vindas recebida do servidor e, em seguida, fecha a conexão FTP.


# Explicação linha à linha:

# from ftplib import *: Esta linha importa todas as classes e funções do módulo ftplib, que é usado para realizar operações FTP (File Transfer Protocol).

# ftp_ativo=False: Aqui, é criada uma variável booleana chamada ftp_ativo e é definida como False. Essa variável será usada posteriormente para configurar o modo de transferência de dados do FTP.

# ftp = FTP('ftp.ibiblio.org'): Cria um objeto FTP, estabelecendo uma conexão com o servidor FTP chamado "ftp.ibiblio.org". É possível fornecer o endereço IP ou o nome do domínio do servidor FTP.

# print(ftp.getwelcome()): Exibe uma mensagem de boas-vindas recebida do servidor FTP. A função getwelcome() retorna essa mensagem.

# ftp.quit(): Encerra a conexão com o servidor FTP e finaliza a sessão FTP.

