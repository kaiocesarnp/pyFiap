texto = "Leia e Han Solo"
    # 012345678901234 = posições do caracteres. Por exemplo, o primeiro espaço é o 4 pq a contagem começa no 0(zero)
    
print(texto[0:4])
print(texto[0:4:2]) #percorrer a cada dois caracteres. explicação: Posição inicial > quantidade de informação a percorrer > passo
print(texto[7:]) #a partir dos dois pontos sem determinar outro numero após eles, a contagem vai até o final

# 543210987654321 - = contagem regressiva, ao contrário, utilizando o sinal de menos
print(texto[-8:])

# Invertendo a string por inteiro
print(texto[::-1])

