#!/usr/bin/python
# -*- coding: utf-8 -*-

fd = open('/etc/passwd', 'r')

lineas = fd.readlines()
fd.close()
dict = {} 
for linea in lineas:
    elementos = linea.split(":")
   #print elementos[0], elementos[-1][:-1]   no nos pide que las imprimamos
    dict[elementos[0]] = elementos[-1][:-1] 

print "La shell de root es:", dict['root']
try:  
    print"La shell de imaginario es:", dict['imaginario']
except (KeyError):
	print "no existe la shell de imaginario"


