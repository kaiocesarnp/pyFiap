basedados = [] #lista vazia. Com a basedados fora do with, é possível manipula-la
                # fora dele. Caso contrario(se ela estivesse dentro do with), só seria possivel manipula-la dentro dele

# abrir "iris.data":
with open("aula4Cap5/iris.data", "r") as arquivo: # "r" = leitura. Chamado de "arquivo"
    for registro in arquivo.readlines():
        # adicionar o "registro" dentro da base de dados:
        basedados.append(registro.split(",")) #assim fica como uma lista, e não como uma linha, uma unica string

print(basedados)