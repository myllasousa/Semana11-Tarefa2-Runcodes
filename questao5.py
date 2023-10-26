while True:
    nota = float(input(""))
    if nota >= 10.1 or nota < 0:
        print("Nota inválida.")
    if 8.5 <= nota <= 10.0:
        print("A")
    if 8.4 >= nota >= 7.0:
        print("B")
    if 6.9 >= nota >= 5.0:
        print("C")
    if 4.9 >= nota >= 4.0:
        print("D")
    if 3.9 >= nota >= 0:
        print("E")
    if 0 <= nota <= 10: break
