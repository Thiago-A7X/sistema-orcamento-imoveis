nome = input("Digite seu nome: ")

while not nome.replace(" ", "").isalpha():
    print("Digite apenas letras.")
    nome = input("Digite seu nome: ")

idade = int(input("Digite sua idade: "))
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 6 and idade >= 18:
    print(f"Parabéns {nome}, você tem {idade} anos, é maior de idade e foi APROVADO(A)!!")
else:
    print(f"Lamento {nome}, você foi REPROVADO(A).")