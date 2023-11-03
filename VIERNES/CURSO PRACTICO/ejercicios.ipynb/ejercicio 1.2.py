frase= input ("contate algo amigo y calculo el tiempo que tardaste:")
separo_palabras=frase.split(" ")
cantidad_palabras=len(separo_palabras)
tiempo= cantidad_palabras/2
tiempo_dalto=(cantidad_palabras/2)*30/100

print("dijiste:",cantidad_palabras,"palabras Y tardaste en decirlas:",tiempo, "segundos")
print("dalto tarda en decirlas:",(tiempo-tiempo_dalto),"segundos")
if tiempo > 10:
    print ("capo hablas una banda")