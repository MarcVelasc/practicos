def sumar_tres_numeros(total):
    numeros = []
    for i in range(3):
        while True:
            try:
                numero = float(input(f"Ingrese el número {i+1}: "))
                break
            except ValueError:
                print("Error: Ingrese un número válido.")
        numeros.append(numero)
    return numeros

total = float(input("Ingrese la cantidad total: "))
numeros = sumar_tres_numeros(total)

if sum(numeros) == total:
    print("Los números ingresados son:", numeros," y cumplen con la cantidad total ingresada")
else:
    print("Error: La suma de los números no es igual a la cantidad total.")