#Jeftech
#Função pra criar novo produto
def cadastrar_produto(estoque):
    nome_produto = input("Digite o nome do produto: ")
    quantidade = int(0)
    valor = float(0.0)
    lucro_bruto = float(0.0)
    lucro_liquido = float(0.0)

    estoque[nome_produto] = {"Quantidade": quantidade, "Valor": valor, "Lucro_bruto": lucro_bruto, "Lucro_liquido": lucro_liquido}
    print(f"Produto {nome_produto} cadastrado com sucesso!")
    return estoque

def comprar_produto(estoque):
    nome_produto = input("Digite o nome do produto que deseja comprar: ")

    if nome_produto in estoque:
        quantidade1 = int(input("Digite a quantidade que deseja comprar: "))
        valor1 = float(input("Digite o valor do produto: "))

        estoque[nome_produto]["Quantidade"] += quantidade1
        estoque[nome_produto]["Valor"] += valor1
        print(f"Nova compra realizada com sucesso!")

def venda_produto(estoque):
    nome_produto = input("Digite o nome do produto que deseja vender: ")

    if nome_produto in estoque:
        quantidade2 = int(input("Digite a quantidade que deseja vender: "))
        if quantidade2 <= estoque[nome_produto]["Quantidade"]:
            valor2 = float(input("Digite o valor da venda: "))

            estoque[nome_produto]["Quantidade"] -= quantidade2
            estoque[nome_produto]["Lucro_bruto"] += valor2
            print(f"Nova venda realizada com sucesso!")

            estoque[nome_produto]["Lucro_liquido"] = estoque[nome_produto]["Lucro_bruto"] - estoque[nome_produto]["Valor"]
        else:
            print("Quantide em estoque menor do que a que deseja vender.")



def mostrar_estoque(estoque):
    print("\nEstoque atual:")
    for produto, dados in estoque.items():
        print(f"Produto: {produto}\n Quantidade: {dados['Quantidade']}\n Valor: R$ {dados['Valor']:.2f}\n Lucro_Bruto: R$ {dados['Lucro_bruto']:.2f}\n Lucro_Liquido: R$ {dados['Lucro_liquido']:.2f}")
    print()

estoque = {}

while True:
    print("Menu:")
    print("1. Cadastrar produto")
    print("2. Comprar produto")
    print("3. Mostrar estoque")
    print("4. Vender produto")
    print("5. Sair")

    menu = int(input("Digite a opção que deseja (de 1 a 5): "))

    if menu == 1:
        while True:
            cad = int(input("Deseja cadastrar um produto? \n1-> Sim\n2-> Não\n: "))
            if cad == 1:
                cadastrar_produto(estoque)
            elif cad == 2:
                break
            else:
                print("Digite um valor válido.\n **********************************")
    elif menu == 2:
        comprar_produto(estoque)
    elif menu == 3:
        mostrar_estoque(estoque)
    elif menu == 4:
        venda_produto(estoque)
    elif menu == 5:
        break
    else:
        print("Digite um valor válido.")
