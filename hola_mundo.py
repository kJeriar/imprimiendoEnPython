#imprime hola mundo
print("Hola, mundo")

# 2. Imprime "Hola, Valeria" con el nombre en una variable
nombre = "Karla"
print( "Hola", nombre ) # con una coma
#Hola&Karla
print("Hola", nombre, sep="&")
#con +
print("Hola " + nombre)
# 3. Imprimir "Hola 156!" con el número en una variable
numero = 777
print("Hola", numero, "!")
print("Hola " + str(numero) + "!")  #Solución con conversión

# 4. Imprimir "Me encanta comer tacos y arepas" con las comidas en variables
comida1 = "sopita"
comida2 = "sopaipillas"
# Con .format()
print("Me encanta comer {} y {}".format(comida1, comida2))
# Con .format()
comidas="Me encanta comer {} y {}".format(comida1, comida2)
print(comidas)
# Con f-string
print(f"Me encanta comer {comida1} y {comida2}")

#otros metodos 
#mayuscula
print(nombre.upper())
# repetirlo 3 veces 
print((f"Hola, {nombre}! ") * 3)