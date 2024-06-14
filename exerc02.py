def impares(inicio, fim):
    for num in range(inicio, fim + 1):
        if num % 2 != 0:
            print(num)

inicio = int(input("Digite um numero: "))
fim = int(input("numero final: "))

print("Números ímpares no intervalo de", inicio, "a", fim, "são:")
impares(inicio, fim)