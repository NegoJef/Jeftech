#Jeftech

#-----Menu-----#
while True:
    menu = int(input("Digite a opção que deseja(de 1 a 5):"))

    if menu == 1:
        print("Cadastro de produtos")
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