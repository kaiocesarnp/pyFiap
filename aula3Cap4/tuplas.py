usuarios={}
emails = ["xpto@xyz.com", "xkcd@phd.com"]

tupla = list(enumerate(emails)) # tupla gerada a partir do método list com uma enumeração de emails / enumerate irá retornar 1,2,3,4...
# print(tupla)

for chave in range(0,len(tupla)):
    print("Email: ", tupla[chave][1])
    usuarios[tupla[chave]]=[input("Digite o nome: "), input("Digite o nível: ")]

for chave,dado in usuarios.items(): # chave, dado é uma tupla; poderia ser assim 'for (chave,dado), mas não é necessario fazer dentro do for
    print("Usuario.:", chave[0])
    print("Email...: ",chave[1])
    print("Nome....: ", dado[0])
    print("Nível...: ", dado[1])

