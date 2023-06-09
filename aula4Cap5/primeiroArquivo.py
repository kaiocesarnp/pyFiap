# Criar arquivos:

# arquivo = open("aula4Cap5/primeiro_arquivo.txt", "w")
# arquivo.write("Meu primeiro arquivo!")
# arquivo.close()


# Melhorando o código, adicionando texto
# with open("aula4Cap5/primeiro_arquivo.txt", "a") as arquivo:
#     arquivo.write("\nHakuna Matata")
#     arquivo.write("\nMuito lindo viver")
#     arquivo.write("\nCe vai entender")
#     arquivo.write("\nHakuna Matata")

# Ler arquivo:
with open("aula4Cap5/primeiro_arquivo.txt", "r") as arquivo:
    conteudo = arquivo.read() #lê o arquivo completo
    conteudo = arquivo.readline() #só lê a primeira linha
    print(conteudo)

#Lê linha à linha, dando espaço entre elas
with open("aula4Cap5/primeiro_arquivo.txt", "r") as arquivo:
    for linha in arquivo.readlines():
        print(linha)





# Sempre que quiser adicionar informações em um arquivo já existente, utilize o "a"

# r = read, ler
# w = write, escrita
# a = append, ler e escrever
# x = exclusivo, ninguem pode manipular enquanto voce está com o arq. aberto

# with = com a abertura deste arqvuivo
#("\n") = pular linha