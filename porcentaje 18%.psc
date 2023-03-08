Algoritmo Porcentaje
	Definir numero1 Como Real
	Definir nombre Como Caracter
	Definir porcentaj Como Real
	Escribir "Escriba su nombre porfavor"
	Leer nombre
	Escribir "Ingrese un numero mayor a 500"
	Leer numero1
	
	Si numero1>500 Entonces
		porcentaj = numero1*0.18
		Escribir nombre, "El 18% del numero ingresado es: ",porcentaj;
	SiNo
		Imprimir nombre, "El numero que ingreso ",numero1, " es menor a 500"
	Fin Si
FinAlgoritmo
