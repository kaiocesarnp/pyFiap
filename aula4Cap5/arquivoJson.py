import json

# LENDO O ARQUIVO:

# with open("aula4Cap5/bd.json", "r") as arq_json: #abrindo o arquivo
#     dicionario = json.load(arq_json) # utilizando o módulo 'json' / carregando(load) o arquivo em "dicionario"
#     for chave,dados in dicionario.items():
#         print(chave + " | " + str(dados))

 
#GRAVANDO/SALVANDO O ARQUIVO:

dicionario = {
"CHAVES":["CHAVES DO 8", "14/04/2017", "RECEP_01"],
"QUICO":["QUICO FLORES", "24/04/2017", "RAIOX_01"],
"FLORINDA":["DONA FLORINDA", "18/04/2017", "RECEP_03"]
}

# o dump precisa de duas informações: o objeto que será escrito(no caso o dicionario), e o nome do arquivo("bd1.json")
with open("aula4Cap5/bd1.json", "w") as json_file:
    json.dump(dicionario, json_file)
