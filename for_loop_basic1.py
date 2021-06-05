#Básico : imprime todos los enteros del 0 al 150.
for x in range (0, 151, 1):
    print(x)
#Múltiplos de cinco : imprime todos los múltiplos de 5 de 5 a 1,000
for x in range (0, 1001, 5):
    print(x)
#Contar, Dojo Way - imprime enteros del 1 al 100. Si es divisible por 5, imprima "Coding" en su lugar. 
# Si es divisible por 10, imprima "Coding Dojo".
for x in range (0, 101, 1):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")
    else:
        print(x)
#¡Uf, Eso es bastante grande!: suma enteros impares de 0 a 500,000 e imprime la suma final.
suma = 0
for x in range (0, 5000001, 1):
    if x % 2 != 0:
        suma += x
print(suma)
#Cuenta regresiva por cuatro : imprime números positivos a partir de 2018, cuenta atrás por cuatro.
for x in range (2018, 0, -4):
    print (x)
#Contador flexible : establece tres variables: lowNum, highNum, mult. Comenzando en lowNum y pasando por highNum, imprima solo los enteros que son múltiplos de mult.
#  Por ejemplo, si lowNum = 2, highNum = 9 y mult = 3, el bucle debe imprimir 3, 6, 9 (en líneas sucesivas)
lowNum = 2
highNum = 9
mult = 3
for x in range(1, highNum+1, 1):
    if x * mult >lowNum and x * mult < highNum+1:
        print( x * mult)

# Crea una función que tome una lista y devuelva un diccionario con su mínimo, máximo, promedio y suma.
def funcion(lista):
    minimo = lista[0]
    maximo = lista[0]
    suma = 0
    promedio = 0
    for x in range(len(lista)):
        if lista[x] < minimo:
            minimo = lista[x]
        
        if lista[x] > maximo:
            maximo = lista [x]

        suma += lista[x]

    promedio = suma/len(lista)

    diccionario = { "min":minimo, "max": maximo, "prom": promedio, "suma": suma}
    return   diccionario  




