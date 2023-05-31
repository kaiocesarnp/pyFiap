def perguntar():
    return input("\nO que deseja realizar?" +
            "\n<I> - Para Inserir um usuário"+
            "\n<P> - Para Pesquisar um usuário"+
            "\n<E> - Para Excluir um usuário"+
            "\n<L> - Para Listar um usuário: ").upper()

def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(),
                                                    input("Digite a última data de acesso: "),
                                                    input("Qual a última estação acessada: ").upper()]
    salvar(dicionario)

# Salvar o dicionário num arquivo:
def salvar(dicionario):
    with open("aula3Cap4/bd.txt", "a") as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(chave + ":" + str(valor))

