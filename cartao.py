renda = float(input("Digite sua renda mensal: "))
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if renda >= 2500.00 and idade >=18:
    print(f"Parabéns {nome}, sua renda é de {renda}, e seu cartão foi aprovado!!")

else: 
    print(f"Olá {nome}, sua renda é de {renda}, e seu cartão não foi aprovado por não atender um de nossos requisitos")