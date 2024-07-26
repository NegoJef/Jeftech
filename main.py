#Jeftech
import json
import os

def carregar_estoque():
    # Verifica se o arquivo 'estoque.json' existe
    if os.path.exists('estoque.json'):
        # Carrega o estoque do arquivo JSON
        with open('estoque.json', 'r') as json_file:
            return json.load(json_file)
    else:
        # Retorna um estoque vazio se o arquivo não existir
        return {}
    
#Função pra criar novo produto
def cadastrar_produto(estoque):

    # Salva o estoque em um arquivo JSON
    with open('estoque.json', 'w') as json_file:
        json.dump(estoque, json_file)

    nome_produto = input("Digite o nome do produto: ")
    quantidade = int(0)
    valor = float(0.0)
    lucro_bruto = float(0.0)
    lucro_liquido = float(0.0)

    estoque[nome_produto] = {"Quantidade": quantidade, "Valor": valor, "Lucro_bruto": lucro_bruto, "Lucro_liquido": lucro_liquido}
    print(f"Produto {nome_produto} cadastrado com sucesso!")
    return estoque

#Função para comprar um produto
def comprar_produto(estoque):

    # Salva o estoque em um arquivo JSON
    with open('estoque.json', 'w') as json_file:
        json.dump(estoque, json_file)

    nome_produto = input("Digite o nome do produto que deseja comprar: ")

    if nome_produto in estoque:
        quantidade1 = int(input("Digite a quantidade que deseja comprar: "))
        valor1 = float(input("Digite o valor do produto: "))

        estoque[nome_produto]["Quantidade"] += quantidade1
        estoque[nome_produto]["Valor"] += valor1
        print(f"Nova compra realizada com sucesso!")
#Função pra vender um produto
def venda_produto(estoque):
    # Salva o estoque em um arquivo JSON
    with open('estoque.json', 'w') as json_file:
        json.dump(estoque, json_file)
    
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


#Função pra mostrar o estoque atual
def mostrar_estoque(estoque):

    # Salva o estoque em um arquivo JSON
    with open('estoque.json', 'w') as json_file:
        json.dump(estoque, json_file)

    # Carrega o estoque do arquivo JSON
    with open('estoque.json', 'r') as json_file:
        produto_carregado = json.load(json_file)
        for produto, dados in produto_carregado.items():
            print(f"Produto: {produto}")
            print(f" Quantidade: {dados['Quantidade']}")
            print(f" Valor: R$ {dados['Valor']:.2f}")
            print(f" Lucro_Bruto: R$ {dados['Lucro_bruto']:.2f}")
            print(f" Lucro_Liquido: R$ {dados['Lucro_liquido']:.2f}")
            print()


estoque = carregar_estoque()

#Salvar a string JSON em um arquivo


while True:
    print("Menu:")
    print("1. Cadastrar produto | 2. Comprar produto | 3. Vender produto | 4. Mostrar Estoque | 5. Sair")
    
    
   
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
        venda_produto(estoque)
        
    elif menu == 4:
        mostrar_estoque(estoque)
    elif menu == 5:
        with open('estoque.json', 'w') as json_file:
            json.dump(estoque, json_file)
        break
    else:
        print("Digite um valor válido.")
