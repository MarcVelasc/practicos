Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> numero = int(input("Ingrese un número para calcular su factorial: "))

factorial = 1

for i in range(1, numero + 1):
    factorial = factorial * i

print("El factorial de", numero, "es", factorial)