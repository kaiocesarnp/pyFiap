# Criar arquivos:

# arquivo = open("aula4Cap5/primeiro_arquivo.txt", "w")
# arquivo.write("Meu primeiro arquivo!")
# arquivo.close()


# Melhorando o código, adicionando texto
with open("aula4Cap5/primeiro_arquivo.txt", "a") as arquivo:
    arquivo.write("\nHakuna Matata")



# Sempre que quiser adicionar informações em um arquivo já existente, utilize o "a"

# r = read, ler
# w = write, escrita
# a = append, ler e escrever
# x = exclusivo, ninguem pode manipular enquanto voce está com o arq. aberto

# with = com a abertura deste arqvuivo
#("\n") = pular linha