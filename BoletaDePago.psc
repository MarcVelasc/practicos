Algoritmo BoletaDePago
	Definir nombre Como Caracter
	Definir cedulaDeIdentidad Como Entero
	Definir cargo Como Caracter
	Definir sueldo como entero
	Definir horasTrabajadas Como Entero
	Definir mes Como Caracter
	Definir a�osDeAntiguedad Como Entero
	Definir porcentajeAntiguedad Como Entero
	Escribir "Escriba su nombre"
	Leer nombre
	Escribir "Escriba su numero de C.I"
	Leer cedulaDeIdentidad
	Escribir "Escriba su cargo"
	Leer cargo 
	Escribir "Escriba su sueldo"
	Leer sueldo
	Escribir "Escriba sus horas trabajadas"
	Leer horasTrabajadas
	Escribir " Escriba el mes"
	Leer mes
	Escribir "Escriba sus a�os de anitiguedad"
	Leer a�osDeAntiguedad
	Si a�osDeAntiguedad>=4 Entonces
		porcentajeAntiguedad= sueldo*(6750*0.011)
		Imprimir "tu sueldo es ,",sueldo "y tu bono de antiguedad es,",porcentajeAntiguedad
	SiNo
		
	Fin Si

	
FinAlgoritmo
