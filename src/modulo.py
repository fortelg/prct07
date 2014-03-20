#!/usr/bin/python
#!encoding: UTF-8
import sys
import math 

PI35DT = 3.14159265358979311599796346854418516

#Utilizacion de una funcion calcular_xi para obtener los xi
def calcular_xi (n, i):
	xi = (i - 1.0/2.0) / n
	return xi

#Utilizacion de una funcion calcular_fxi para obtener los f(xi)
def calcular_fxi (xi):
	fxi = 4.0 / (1.0 + xi*xi)
	return fxi

#Utilizacion de una funcion arccot para calcular la arcotangente
def arccot(x, unity):
	sum = xpower = unity // x
	n = 3
	sign = -1
	while 1:
		xpower = xpower // (x*x)
		term = xpower // n
		if not term:
			break
		sum += sign * term
		sign = -sign
		n += 2
	return sum

#Esta funcion es para calcular los 35 decimales, a su vez llama a la funcion arccot
def decimales_pi(digits):
	unity = 10**(digits + 10)
	decimal_pi = 4 * (4*arccot(5, unity) - arccot(239, unity))
	return (float(decimal_pi // 10**10) / 10**digits)

def calcular_pi (n):
	VALOR_PI = 3.14159265358979311599796346854418516
	ini = 0
	intervalo = 1.0 / float (n);
	sumatorio = 0.0
	for i in range(n):
		xi = calcular_xi(n, i+1)
		fxi = calcular_fxi (xi)
		ini += intervalo
		sumatorio += fxi
	valor_pi = sumatorio / n;
	return (valor_pi)

#Programa principal
#Ojo, para hacer uso de la funcion sys, debemos incluirla al principio del programa


if (__name__ == "__main__"):
	argumentos = sys.argv[1:]
	if (len(argumentos) == 2):
		aproximaciones = int (argumentos[0])
		n = int (argumentos[1])
	else:
		print "Introduzca el numero de aproximaciones:"
		aproximaciones = int (raw_input ());
		print "Introduzca el numero de intervalos (n > 0):"
		n = int (raw_input ());
	if (n > 0):
		intervalo = n
		lista = []
		for i in range (aproximaciones):
			valor_pi = calcular_pi (intervalo)
			intervalo += n
			lista.append (valor_pi)
		pi35 = []
		for i in range (aproximaciones):
			pi35.append (PI35DT)
		dif35 = []
		for i in range (aproximaciones):
			dif35.append (abs(pi35[i] - lista[i]))
		print "i\tPI35DT\tlista i\tPI35DT - lista i"
		for i in range (aproximaciones):
			print "%d\t%1.10f\t%1.10f\t%1.10f" % (i+1, pi35[i], lista[i], dif35[i])
	else:
		print "El valor de los intervalos debe ser mayor que 0"


