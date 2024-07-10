#Jeftech
#Função pra criar novo produto
def cadastrar_produto(estoque):
    nome_produto = input("Digite o nome do produto: ")
    quantidade = int(0)
    valor = float(0.0)

    estoque[nome_produto] = {"Quantidade": quantidade, "Valor": valor}
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

def mostrar_estoque(estoque):
    print("\nEstoque atual:")
    for produto, dados in estoque.items():
        print(f"Produto: {produto}, Quantidade: {dados['Quantidade']}, Valor: R$ {dados['Valor']:.2f}")
    print()

estoque = {}

while True:
    print("Menu:")
    print("1. Cadastrar produto")
    print("2. Comprar produto")
    print("3. Mostrar estoque")
    print("4. Prejuízo/Despesas")
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
        print("Prejuízo/Despesas")
    elif menu == 5:
        break
    else:
        print("Digite um valor válido.")
