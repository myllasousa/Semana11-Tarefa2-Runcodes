while True:
    print('''OPÇÕES:
1 - SAUDAÇÃO
2 - BRONCA
3 - FELICITAÇÃO
0 - FIM''')
    opcao = int(input(""))

    if opcao == 1:
        print("1 - Olá. Como vai?")
    if opcao == 2:
        print("2 - Vamos estudar mais.")
    if opcao == 3:
        print("3 - Meus Parabéns!")
    if opcao >= 4:
        print("Opção inválida.")
    if opcao == 0: break

print("0 - Fim de serviço.")


