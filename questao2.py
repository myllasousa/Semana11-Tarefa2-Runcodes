quantidade = 0
numeros = 0
maior = None
menor = None
while True:
    idade = int(input(""))
    if idade == 0: break
    if idade > 0:
        numeros += idade
        quantidade += 1
    if idade > 0:
        if maior is None or idade > maior:
            maior = idade
        if menor is None or idade < menor:
            menor = idade
media = numeros / quantidade
print(quantidade)
print(f'{media:.2f}')
print(menor)
print(maior)

