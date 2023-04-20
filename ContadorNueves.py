def contar_nueves(numero):
    contador = 0
    numero = str(numero)
    for digito in numero:
        if digito == '9':
            contador += 1
    return contador

numero = int(input("Ingresa un número: "))
cantidad_de_nueves = contar_nueves(numero)
print("La cantidad de nueves en el número ingresado es:", cantidad_de_nueves)