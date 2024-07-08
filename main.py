#Jeftech
#Função pra criar novo produto
class produto:
    def __init__(self,nome,valor,):
        self.nome = nome
        self.valor = valor
    def __repr__(self):
        return f"{self.nome}, Valor={self.valor}"
    
def cadastrar_produto(nome,valor,):
    return produto(nome,valor)







#-----Menu-----#
while True:
    menu = int(input("Digite a opção que deseja(de 1 a 5):"))

    if menu == 1:
        print("Cadastro de produtos")
        nome1 = str(input("Digite o nome do produto:"))
        valor1 = float(input("Digite o valor do produto:"))
        produto1 = cadastrar_produto(nome1,valor1)
        print(produto1)
    elif menu == 2:
        print("Compra de produtos")
    elif menu == 3:
        print("Venda de produtos")
    elif menu == 4:
        print("Prejuizo/Despesas")
    elif menu == 5:
        break
    else:
        print("Digite um valor válido")