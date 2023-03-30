import math
import random
numeroAlAzar = random.randint(1,2)
def FuncionSumatoria(num1, num2, num3):
    return num1 + num2 + num3

def numeroMayor(num1,num2,num3):
  if  (num1>num2 and num1>num3):
    numeroMayor=num1
  else:
    if (num3>num1 and num3>num2):
      numeroMayor=num2
    else:
      numeroMayor=num3
  return numeroMayor

def FuncionFormula (numeroElegidoAlAzar,numeroAleatorio12,numeroTexto,longitudNumero ):
    if longitudNumero==2:
        primerNumeroTexto=(numeroTexto[0])
        primerNumero=int(primerNumeroTexto)
        ultimoNumeroTexto=(numeroTexto[-1])
        ultimoNumero=int(ultimoNumeroTexto)
        potenciaPrimera=(primerNumero**2)
        piUltimo=(ultimoNumero*math.pi)
        return (potenciaPrimera+piUltimo)
    else:
        if longitudNumero==3:
            primerNumeroTexto=(numeroTexto[0])
            primerNumero=int(primerNumeroTexto)
            ultimoNumeroTexto=(numeroTexto[-1])
            ultimoNumero=int(ultimoNumeroTexto)
            numeroCentralTexto=(numeroTexto[1])
            numeroCentral=int(numeroCentralTexto)
            potenciaPrimera=(primerNumero**2)
            piUltimo=(ultimoNumero*math.pi)
            return (potenciaPrimera+piUltimo+numeroCentral)
        else:
            if longitudNumero>3:
                primerNumeroTexto=(numeroTexto[0])
                primerNumero=int(primerNumeroTexto)
                ultimoNumeroTexto=(numeroTexto[-1])
                ultimoNumero=int(ultimoNumeroTexto)
                potenciaPrimera=(primerNumero**2)
                piUltimo=(ultimoNumero*math.pi)
                B=1
                nCentroFinal=1
                while B<=(longitudNumero-2):
                    nCentralTexto=(numeroTexto[B])
                    nCentroNumeral=int(nCentralTexto)
                    nCentroFinal=(nCentroFinal*nCentroNumeral)
                    B=B+1
                return potenciaPrimera+piUltimo+nCentroFinal
            else:
                return numeroElegidoAlAzar

def FuncionAleatorio (suma,numeroMayor):
  numeroAleatorio = random.randint(1,2)
    if numeroAleatorio==1:
        return suma
    else:
        return numeroMayor
  
# Funcion Raiz Cuadrada
def funcionRaizCuadrada (numeroElegidoAlAzar,numeroAleatorio,numeroTexto,longitudNumero ):
  funcionRaizCuadrada = math.sqrt(numeroElegidoAlAzar,numeroAleatorio,numeroTexto,longitudNumero )

# Funcion Seno
numerofinal=FuncionFormula(numeroElegidoAlAzar,numeroAlAzar,numeroTexto,longitudNumero )
def senode (numerofinal):
    return math.sin(numerofinal)