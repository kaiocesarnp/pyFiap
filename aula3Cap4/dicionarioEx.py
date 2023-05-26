usuarios={}
usuarios={
    "Chaves":["Chaves Silva","17/06/2017","Recep_01"],
    "Quico":["Enrico Flores","03/06/2017","Raiox_02"]
    }
print(usuarios)

# Adicionando novo usuário sem subscrever os antigos:
usuarios["Florinda"]=["Florinda Flores", "26/11/2017", "Recep_01"]
print(usuarios)

print("####----####")

# Verificar ultimo login do usuário:
print(usuarios.get("Quico"))

