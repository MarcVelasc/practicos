numero = int(input("Ingrese un número para calcular su factorial: "))

factorial = 1

for i in range(1, numero + 1):
    factorial = factorial * i

print("El factorial de", numero, "es", factorial)