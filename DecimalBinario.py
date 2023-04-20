def decimalBinario(decimal):
    binario = ''
    while decimal > 0:
        residuo = decimal % 2
        binario = str(residuo) + binario
        decimal = decimal // 2
    return binario

numero_decimal = int(input("Ingresa un número decimal: "))
numero_binario = decimalBinario(numero_decimal)
print("El número binario equivalente es:", numero_binario)