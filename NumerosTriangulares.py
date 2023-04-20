def generar_secuencia_triangulares(hasta):
    secuencia = []
    for n in range(1, hasta+1):
        numero_triangular = n * (n + 1) // 2
        secuencia.append(numero_triangular)
    return secuencia

hasta = 6
secuencia_triangulares = generar_secuencia_triangulares(hasta)
print("La secuencia de números triangulares hasta", hasta, "es:")
print(secuencia_triangulares)