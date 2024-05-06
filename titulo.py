# -*- coding: utf-8 -*-
"""
Created on Mon May  6 15:06:35 2024

@author: Dell
"""
import camelcase

nombre = "josé moisés villanueva parrera"

print(nombre.upper())
print(nombre.title())

#Creamos un objeto llamado cam
cam = camelcase.CamelCase()
print("Con camelcase....")

# imprimimos el nombre en formato título
# utilizamos camelcase
print(cam.hump(nombre))


