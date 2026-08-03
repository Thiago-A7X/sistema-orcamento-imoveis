import csv

# Classe do orçamento
class Orcamento:

    def __init__(self, imovel):
        self.imovel = imovel
        self.valor_aluguel = 0
        self.valor_contrato = 2000

        self.definir_valor()


    def definir_valor(self):

        if self.imovel == "Apartamento":
            self.valor_aluguel = 700

        elif self.imovel == "Casa":
            self.valor_aluguel = 900

        elif self.imovel == "Estúdio":
            self.valor_aluguel = 1200



    def adicionar_quartos(self, quartos):

        if quartos == "2":

            if self.imovel == "Apartamento":
                self.valor_aluguel += 200

            elif self.imovel == "Casa":
                self.valor_aluguel += 250


    def adicionar_garagem(self):

        self.valor_aluguel += 300


    def adicionar_vagas_estudio(self, vagas):

        if vagas >= 2:

            self.valor_aluguel += 250

            extras = vagas - 2

            self.valor_aluguel += extras * 60



    def aplicar_desconto(self):

        desconto = self.valor_aluguel * 0.05

        self.valor_aluguel -= desconto

        return desconto



    def calcular_parcela(self, parcelas):

        return self.valor_contrato / parcelas


# Exibe as opções de imóveis e retorna a escolha do usuário.
def escolher_imovel():

    print("===== R.M - GERAÇÃO DE ORÇAMENTO =====")
    print("1 - Apartamento")
    print("2 - Casa")
    print("3 - Estúdio")


    opcao = input("Escolha o tipo de imóvel desejado: ")


    if opcao == "1":
        return "Apartamento"

    elif opcao == "2":
        return "Casa"

    elif opcao == "3":
        return "Estúdio"

    else:

        print("Opção inválida, Tente Novamente!")

        return escolher_imovel()


# ESTRUTURA DO PROGRAMA PRINCIPAL:


# Fluxo principal de entrada dos dados e geração do orçamento.
imovel = escolher_imovel()

# Cria o orçamento inicial baseado no tipo de imóvel escolhido.
orcamento = Orcamento(imovel)



# Quartos
if imovel == "Apartamento" or imovel == "Casa":

    quartos = input("Digite a quantidade de quartos (1 ou 2): ")


    while quartos != "1" and quartos != "2":

        print("Só é possivel escolher entre 1 ou 2 quartos, Tente Novamente!")

        quartos = input("Digite a quantidade de quartos (1 ou 2): ")


    orcamento.adicionar_quartos(quartos)



# Garagem
if imovel == "Apartamento" or imovel == "Casa":

    garagem = input("Deseja vaga de garagem? (s/n): ").lower()


    while garagem != "s" and garagem != "n":

        print("Digite apenas s ou n.")

        garagem = input("Deseja vaga de garagem? (s/n): ").lower()


    if garagem == "s":

        orcamento.adicionar_garagem()



# Estúdio
if imovel == "Estúdio":

    while True:
        try:
            vagas = int(input("Quantidade de vagas desejada: "))

            if vagas >= 0 and vagas != 1:
                break

            print("Quantidade inválida. Escolha 0 vagas ou 2 vagas ou mais.")

        except ValueError:
            print("Digite apenas números.")

    orcamento.adicionar_vagas_estudio(vagas)


# Aplica desconto de 5% para apartamentos sem crianças.
if imovel == "Apartamento":

    criancas = input("Possui crianças? (s/n): ").lower()

    while criancas != "s" and criancas != "n":
        print("Resposta inválida. Digite 's' para sim ou 'n' para não.")
        criancas = input("Possui crianças? (s/n): ").lower()

    if criancas == "n":

        desconto = orcamento.aplicar_desconto()

        print(f"Desconto aplicado: R$ {desconto:.2f}")

# Solicita a quantidade de parcelas e trata entradas inválidas que não sejam números.
print("\n===== PARCELAMENTO =====")

while True:
    try:
        parcelas = int(input("Digite a quantidade de parcelas desejadas entre (1-5): "))

        if parcelas >= 1 and parcelas <= 5:
            break

        print("Número de parcelas não permitido!!\n"
              "Digite um número entre 1 e 5.")

    except ValueError:
        print("Digite apenas números.")

# Calcula o valor da parcela do contrato
valor_parcela = orcamento.calcular_parcela(parcelas)



# Exibe o resumo final do orçamento calculado.
print("\n========== ORÇAMENTO ==========")

print(f"Imóvel: {orcamento.imovel}")

print(f"Aluguel mensal: R$ {orcamento.valor_aluguel:.2f}")

print(f"Contrato: R$ {orcamento.valor_contrato:.2f}")

print(f"{parcelas}x de R$ {valor_parcela:.2f}")

print("================================")



# Gera um relatório mensal do aluguel e parcelas do contrato em CSV.
gerar = input("\nDeseja gerar CSV? (s/n): ").lower()


if gerar == "s":

    with open("orcamento.csv","w",newline="",encoding="utf-8") as arquivo:


        escritor = csv.writer(arquivo)


        escritor.writerow(["Mês", "Aluguel", "Contrato", "Total"])

        for mes in range(1, 13):

            contrato = 0

            if mes <= parcelas:
                contrato = valor_parcela

            total = orcamento.valor_aluguel + contrato

            escritor.writerow([mes,f"R$ {orcamento.valor_aluguel:.2f}",f"R$ {contrato:.2f}",f"R$ {total:.2f}"])

    print("Arquivo criado com sucesso!")