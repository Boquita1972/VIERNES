"""#pedirle un dato al usuario

nombre= input("amigo como te llamas: ")

#mostrar el dato, concateno con la cadena f

print (f'el nombre es: {nombre}')"""

"""-------------------------------------------------------"""

#pedir que ingrese un numero, en este caso toma el numero como texto

"""numero= input("amigo tirate un numero: ")

resultado= numero *2 

print (resultado)"""

"""-------------------------------------------------------"""
#con la funcion int convierte el numero texto a numero entero y lo multiplico x 2

"""numero= input("amigo tirate un numero: ")

resultado= int(numero) *2 

print ("el resultado es:", resultado)"""


"""-------------------------------------------------------"""
#con la funcion float convierte el numero texto a numero flotante y lo multiplico x 2

"""numero= input("amigo tirate un numero: ")

resultado= float(numero) *2 

print ("el resultado es:", resultado)"""

"""-------------------------------------------------------"""
#con la funcion int delante de float hace que el resultado sea un entero
# si no por mas que sea un entero me lo muestra como flotante 9.0 

numero= input("amigo tirate un numero: ")

resultado= int(float(numero) *2) 

print ("el resultado es:", resultado)
