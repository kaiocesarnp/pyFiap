import getpass 

# print("Usuário.......: ", getpass.getuser()) #Usuário da máquina

# print(getpass.getpass("Digite sua senha:..."))

usuario = getpass.getuser()
senha = getpass.getpass("Digite sua senha:...")

if usuario == 'Particular' and senha == 'hello_python':
    print('Bem-vinda Tasha')
else:
    print('Você não tem acesso')


