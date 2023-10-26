preco = 0
while True:
    print('''CÓDIGO  PRODUTO         PREÇO (R$)
H       Hamburger       5,50
C       Cheeseburger    6,80
M       Misto Quente    4,50
A       Americano       7,00
Q       Queijo Prato    4,00
X       PARA TOTAL DA CONTA''')

    opcao = input("").strip().upper()[0]

    if opcao == 'H':
        preco += 5.50
    if opcao == 'C':
        preco += 6.80
    if opcao == 'M':
        preco += 4.50
    if opcao == 'A':
        preco += 7.00
    if opcao == 'Q':
        preco += 4.00
    if opcao == 'X': break
    if opcao != 'H' and opcao != 'C' and opcao != 'M' and opcao != 'A' and opcao != 'Q' and opcao != 'X':
        print("Opção inválida.")

print(f'{preco:.2f}')

