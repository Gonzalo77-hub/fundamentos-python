# 1. TAREA: imprimir "Hola mundo"
print( "Hola mundo" )
# 2. imprimir "Hola Noelle!" con el nombre en una variable
name = "Gonzalo"
print("Hola", name)	# con una coma
print("Hola" + name)	# con un +
# 3. imprimir "Hola 42!" con un numero en una variable
name = 22
print("Hola", name )	# con una coma
print("Hola" + name )	# con un + - !Este debería darnos un error!
# 4. imprimir "Me encanta comer sushi and pizza." con los alimentos en variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print( "Me encanta comer {} y {}.".format(fave_food1, fave_food2) ) # con .format()
print(f"Me encanta comer {fave_food1} y {fave_food2}") # con una cadena f
#NINJA BONUS: descubre cómo resolver el error desde arriba, sin cambiar el signo + a una coma
name = "Gonzalo"
print("Hola " + name)
#BONIFICACIÓN DE NINJA: ¡Dedica unos minutos a jugar con otros métodos de cadenas para ver qué hay ahí fuera!
titulo= "Hola Python"
tit_minuscula = titulo.lower()#Convierte el texto en minisculas
tit_mayuscula = titulo.upper()#Convierte el texto en mayusculas
tit_find = titulo.find("Python")#Devuelve el índice en el que aparece la subcadena (-1 si no aparece):
tit_replace = titulo.replace('o','0')# remplaza los caracteres seleccionados
tit_count = titulo.count('m')# Devuelve la cantidad de veces que aparece una subcadena en el texto
print(tit_mayuscula)
print(tit_minuscula)
print(tit_find)
print(tit_replace)