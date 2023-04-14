Funcion fibunnaci<- numFibunnaci(numero)
	resultado=0
	cantidad=0
	anterior=1
	cont=0
	Para i<-1 Hasta numero Con Paso 1 Hacer
		
		resultado=cantidad + anterior
		anterior= cantidad
		cantidad= resultado
		si numero=resultado Entonces
			cont= cont+1
		FinSi
	Fin Para
	si cont=1 Entonces
		imprimir "es fibonnaci"
	sino 
		Imprimir "no es fibonnaci"
	FinSi

Fin Funcion
Funcion ParImpar<-numParImpar(numero)
	Si numero mod 2=0  Entonces
		Escribir "El numero es par"
	SiNo
		Escribir "El numero es impar"
	Fin Si
	
Fin Funcion

Funcion Primo<-numPrimo(numero)
	cont <- 0
	Para i<-1 Hasta numero Con Paso 1 Hacer
		si numero mod i=0 Entonces
			cont=cont+1
		FinSi
	Fin Para
	Si cont = 2 Entonces
		Escribir "Si es numero primo"
	SiNo
		Escribir "No es numero primo"
	Fin Si
	
Fin Funcion

Algoritmo PrimoImparFibunnaci
	Definir resultado, numero,anterior, cantidad Como Entero
	Escribir "Ingrese un numero"
	Leer numero
	Imprimir numParImpar(numero)
	Imprimir numPrimo(numero)
	Imprimir numFibunnaci(numero)
FinAlgoritmo
