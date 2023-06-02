texto = "Eu amo Python!"
        #012345
print(texto.find("o")) #find = encontrar
                        # neste caso retorna a primeira ocorrência do caractere "o"

print(texto[texto.find("o")+1:].find("o")) #encontrando o proximo caractere, dividindo o texto a partir do primeiro "o", assim o resultado é o mesmo na contagem
                                                #012345012345 = contagem

# Cortando a lista em vários pedaços:
print(texto.split(" ")) #referência é o espaço entre as palavras