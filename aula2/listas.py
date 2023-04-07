inventario=[]
resposta="S"
while resposta=="S":
  inventario.append(input("Equipamento: ")) #append = inserido na lista 'inventario'
  inventario.append(float(input("Valor: ")))
  inventario.append(int(input("Número Serial: ")))
  inventario.append(input("Departamento: "))
  resposta=input("Digite \"S\" para continuar: ").upper()  #upper = letra maiuscula, \"\" barras com aspas = aspas aparecem no print

for elemento in inventario:
  print(elemento)

