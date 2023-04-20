def decimal_a_romano(decimal):
    romanos = {
        1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X',
        40: 'XL', 50: 'L', 90: 'XC', 100: 'C',
        400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
    }
    resultado = ''
    for valor, simbolo in sorted(romanos.items(), reverse=True):
        while decimal >= valor:
            resultado += simbolo
            decimal -= valor
    return resultado

def romano_a_decimal(romano):
    romanos = {
        'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10,
        'XL': 40, 'L': 50, 'XC': 90, 'C': 100,
        'CD': 400, 'D': 500, 'CM': 900, 'M': 1000
    }
    resultado = 0
    i = 0
    while i < len(romano):
        if i + 1 < len(romano) and romano[i:i+2] in romanos:
            resultado += romanos[romano[i:i+2]]
            i += 2
        else:
            resultado += romanos[romano[i]]
            i += 1
    return resultado

while True:
    print("1. Convertir decimal a romano")
    print("2. Convertir romano a decimal")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == '1':
        decimal = int(input("Ingrese el número decimal: "))
        romano = decimal_a_romano(decimal)
        print(f"El número romano equivalente es: {romano}")
    elif opcion == '2':
        romano = input("Ingrese el número romano: ")
        decimal = romano_a_decimal(romano)
        print(f"El número decimal equivalente es: {decimal}")
    elif opcion == '3':
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")