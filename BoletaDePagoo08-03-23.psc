Algoritmo BoletaDePago
	Definir nombre Como Caracter
	Definir cedulaDeIdentidad Como Entero
	Definir cargo Como Caracter
	Definir sueldo como entero
	Definir horasTrabajadas Como Entero
	Definir mes Como Caracter
	Definir añosDeAntiguedad Como Entero
	Definir porcentajeAntiguedad Como Entero
	Definir haberBasico, salarioMinimo Como Real
	Definir bonoAntiguedad Como Real
	Definir ingresos, egresos, liquidoPagable Como Real 
	haberBasico=sueldo
	salarioMinimo=2250 
	Escribir "Escriba su nombre y Apellido"
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
	Escribir "Escriba sus años de antiguedad"
	Leer añosDeAntiguedad
	Si añosDeAntiguedad<2 Entonces
		porcentajeAntiguedad= 0
		
	SiNo
		Si añosDeAntiguedad >=2 y añosDeAntiguedad<=4 Entonces
			porcentajeAntiguedad=0.05
		SiNo
			Si añosDeAntiguedad >=5 y añosDeAntiguedad <=7 Entonces
				porcentajeAntiguedad=0.11
			SiNo
				Si añosDeAntiguedad >=8 y añosDeAntiguedad <=10 Entonces
					porcentajeAntiguedad=0.18
				SiNo
					Si añosDeAntiguedad >=11 y añosDeAntiguedad <=14 Entonces
						porcentajeAntiguedad=0.26
					SiNo
						Si añosDeAntiguedad >=15 y añosDeAntiguedad <=19 Entonces
							porcentajeAntiguedad=0.34
						SiNo
							Si añosDeAntiguedad >=20 y añosDeAntiguedad <=24 Entonces
								porcentajeAntiguedad=0.42
							SiNo
								Si añosDeAntiguedad >=25 Entonces
									porcentajeAntiguedad=0.50
								SiNo
									
								Fin Si
							Fin Si
						Fin Si
						
					Fin Si
				Fin Si
			Fin Si
		Fin Si
		
	Fin Si
	bonoAntiguedad=salarioMinimo*3*porcentajeAntiguedad
	ingresos=haberBasico+bonoAntiguedad
	Imprimir "tu ingreso es ,",ingresos "y tu bono de antiguedad es,",porcentajeAntiguedad, ""
	
FinAlgoritmo