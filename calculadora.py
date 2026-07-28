def somar():
    print("SOMAR")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = (num1 + num2)
    print(f"O resultado da sua soma é de: {resultado}")


def subtrair():
    print("SUBTRAIR")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = (num1 - num2)
    print(f"O resultado da sua subtração é de: {resultado}")


def dividir():
    print("DIVIDIR")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = (num1 / num2)
    print(f"O resultado da sua divisão é de: {resultado}")


def multiplicar():
    print("MULTIPLICAR")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = (num1 * num2)
    print(f"O resultado da sua multiplicação é de: {resultado}")

print("##### CALCULADORA DA LALA ######")

print("1 - somar")
print("2 - subtrair")
print("3 - dividir")
print("4 - multiplicar")

opcao = int(input("Digite a opção desejada: "))

if opcao == 1:
    somar()