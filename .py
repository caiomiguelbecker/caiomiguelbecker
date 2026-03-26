print ("hello word")

codar = input( "Vamos codar?")

lopping = True
while lopping:
    if codar.lower() == "sim":
        print("Ótimo! Vamos começar a codar!")
        lopping = False
    else:
        print("Vamos tentar novamente. Digite 'sim' para começar a codar.")
        codar = input( "Vamos codar?")

nome = input("qual seu nome?")

idade = input("Qual sua idade?")

print(f"ola, {nome}! Boa noite")

print(f"então, {nome} vamos codar,")

print ("Comece escolhendo seu username e senha para login")

username = input("Digite seu username: ")   

senha = input("Digite sua senha: ") 

print(f"Parabéns, {nome}! Você criou seu login com sucesso. Seu username é '{username}' e sua senha é '{senha}'. Agora você pode acessar sua conta e começar a codar!")

print("agora vamos logar com seu username e senha")

username_login = input("Digite seu username para login: ") 
senha_login = input("Digite sua senha para login: ") 


lopping = True
while lopping:
    if username_login == username and senha_login == senha:
        print(f"Bem-vindo de volta, {nome}! Você fez login com sucesso.")
        lopping = False
    else:
        print("Username ou senha incorretos. Tente novamente.")
        username_login = input("Digite seu username para login: ") 
        senha_login = input("Digite sua senha para login: ")

