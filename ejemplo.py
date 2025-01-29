"""
    Ejemplo de estructura de condicional
    múltiple
"""

# Declaración de variables

# Variable para almacenar la calificación cualitativa
resultado = ""   # variable de tipo cadena 

# Variable para almacenar la calificación del estudiante
# Solicitar al usuario que ingrese la calificación
calificacion = input("Ingrese la calificación del estudiante: ")
# Para asignar el valor a calificación, se pide el valor por teclado
# a través de input, luego se hace la transformación del valor de tipo
# cadena a decimal, a travé de la función float
calificacion = float(calificacion)

# Determinar la calificación cualitativa usando solo if / else
if calificacion >= 0 and calificacion <= 2:
    resultado = "Muy mala"
else:
    if calificacion > 2 and calificacion <= 3:
        resultado = "Mala"
    else:
        if calificacion > 3 and calificacion <= 5:
            resultado = "Deficiente"
        else:
            if calificacion > 5 and calificacion <= 7:
                resultado = "Buena"
            else:
                if calificacion > 7 and calificacion <= 8:
                    resultado = "Buena"
                else:
                    if calificacion > 8 and calificacion <= 9:
                        resultado = "Muy buena"
                    else:
                        if calificacion > 9 and calificacion <= 10:
                            resultado = "Excelente"
                        else:
                            resultado = "Calificación fuera de rango"

# Mostrar el resultado al usuario
# opción 1
print("La calificación cualitativa es %s" % (resultado))

# opción 2
# print(f"La calificación cualitativa es {resultado}")
