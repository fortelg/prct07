#!/usr/bin/python
#!encoding: UTF-8
import modulo 

#Programa principal
#Ojo, para hacer uso de la funcion sys, debemos incluirla al principio del programa

tupla = (10,20, 30, 40)
#tupla = (10,100,1000,10000,100000,1000000,10000000,100000000,1000000000,10000000000)
#tupla = (10,100,1000,10000,100000,1000000,10000000, 100000000,1000000000) #Error de memoria
#tupla = (1e1,1e2,1e3,1e4,1e5,1e6,1e7,1e8)

lista = []
for i in tupla:
	valor_pi = modulo.calcular_pi (i)
	lista.append (valor_pi)
pi35 = []
for i in tupla:
	pi35.append (modulo.PI35DT)
dif35 = []
for i in range (len (tupla)):
	dif35.append (abs(pi35[i] - lista[i]))
print "i\tPI35DT\t\tlista i\t\tPI35DT - lista i"
for i in range (len (tupla)):
	print "%d\t%1.10f\t%1.10f\t%1.10f" % (i+1, pi35[i], lista[i], dif35[i])

#Esto sería para saber Mas.....
print "Pasando la salida a una matriz...."
print "i\tPI35DT\t\tlista i\t\tPI35DT - lista i", #
matriz = []
for i in range (len (tupla)):
	matriz.append ([i+1, pi35[i], lista[i], dif35[i]])
for i in range (len (tupla)):
	print
	print matriz[i][0], #
	for j in range (1,4):
		print "\t%1.10f" % matriz[i][j], #
