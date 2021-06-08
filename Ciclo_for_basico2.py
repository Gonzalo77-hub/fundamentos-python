#Tamaño grande: dada una lista, escriba una función que cambie todos los números positivos de la lista a "big".
# Ejemplo: biggie_size ([- 1, 3, 5, -5]) devuelve la misma lista, pero cuyos valores son ahora [-1, "big", "big", -5]
def cambiar(lista):
    for x in range(len(lista)):
        if lista[x] > 0 :
            lista[x]= "big"
    return lista
print(cambiar([-1, 3, 5, -5]))    

#Contar positivos : dada una lista de números, cree una función para reemplazar el último valor con el número de valores positivos.
#  (Tenga en cuenta que cero no se considera un número positivo).
# Ejemplo: count_positives ([- 1,1,1,1]) cambia la lista original a [-1,1,1,3] y la devuelve
# Ejemplo: count_positives ([1,6, -4, -2, -7, -2]) cambia la lista a [1,6, -4, -2, -7,2] y la devuelve
def contarPositivos(lista):
    contador = 0
    for x in range(len(lista)):
        if lista[x] > 0 :
            contador +=1
    lista[len(lista)-1] = contador
    return lista
mylist = [-1, 1, 1, 1,] 
mylist2 = [1,6, -4, -2, -7, -2]   
print(contarPositivos(mylist))
print(contarPositivos(mylist2))
# Suma total : crea una función que toma una lista y devuelve la suma de todos los valores de la matriz.
# Ejemplo: sum_total ([1,2,3,4]) debería devolver 10
# Ejemplo: sum_total ([6,3, -2]) debería devolver 7
def sumaTotal(lista):
    suma = 0
    for x in range(len(lista)):
        suma += lista[x] 
    return suma
mylist = [1, 2, 3, 4,] 
mylist2 = [6, 3, -2]   
print(sumaTotal(mylist))
print(sumaTotal(mylist2))
# Promedio : crea una función que toma una lista y devuelve el promedio de todos los valores.
# Ejemplo: el promedio ([1,2,3,4]) debería devolver 2.5
def promedio(lista):
    suma = 0
    for x in range(len(lista)):
        suma += lista[x] 
    return suma/len(lista)
mylist = [1, 2, 3, 4,] 
mylist2 = [6, 3, -2]   
print(promedio(mylist))
print(promedio(mylist2))
# Longitud : crea una función que toma una lista y devuelve la longitud de la lista.
# Ejemplo: la longitud ([37,2,1, -9]) debería devolver 4
# Ejemplo: longitud ([]) debería devolver 0
def promedio(lista):
    largo = len(lista)
    return largo
mylist = [37, 2, 1, -9,] 
mylist2 = []   
print(promedio(mylist))
print(promedio(mylist2))
# Mínimo : crea una función que tome una lista de números y devuelva el valor mínimo en la lista. Si la lista está vacía, haga que la función devuelva False.
# Ejemplo: mínimo ([37,2,1, -9]) debería devolver -9
# Ejemplo: mínimo ([]) debería devolver False
def minimo(lista):
    if len(lista) < 1:
        return False
    else:
        min = lista[2]
        for x in range(len(lista)):
            if lista[x] < min:
                min = lista[x]
    return min
mylist = [] 
mylist2 = [2,3,4]   
print(minimo(mylist))
print(minimo(mylist2))
# version corta
def minimo(lista):
    if len(lista) < 1:
        return False
    else:
        minin = min(lista)
    return minin
mylist = [] 
mylist2 = [2,3,4]   
print(minimo(mylist))
print(minimo(mylist2))
# Máximo : crea una función que toma una lista y devuelve el valor máximo en la matriz. Si la lista está vacía, haga que la función devuelva False.
# Ejemplo: máximo ([37,2,1, -9]) debería devolver 37
# Ejemplo: máximo ([]) debería devolver False
def maximo(lista):
    if len(lista) < 1:
        return False
    else:
        max = lista[0]
        for x in range(len(lista)):
            if lista[x] > max:
                max = lista[x]
    return max
mylist = [] 
mylist2 = [2,3,4]   
print(maximo(mylist))
print(maximo(mylist2))

# version corta
def minimo(lista):
    if len(lista) < 1:
        return False
    else:
        maxin = max(lista)
    return maxin
mylist = [] 
mylist2 = [2,3,4]   
print(minimo(mylist))
print(minimo(mylist2))
# Análisis final : crea una función que tome una lista y devuelva un diccionario que tenga la suma total, 
# promedio, mínimo, máximo y longitud de la lista.
# Ejemplo: ultimate_analysis ([37,2,1, -9]) debería devolver 
# {'totalTotal': 31, 'promedio': 7.75, 'mínimo': -9, 'máximo': 37, 'longitud': 4}
def maximo(lista):
    if len(lista) < 1:
        return False
    else:
        max = lista[0]
        min = lista[0]
        promedio = 0
        suma = 0
        for x in range(len(lista)):
            if lista[x] > max:
                max = lista[x]
            if lista[x] < min:
                min = lista[x]
            suma += lista[x]
        promedio = suma/len(lista)
        diccionario = { "minimo": min, "maximo": max, "promedio": promedio, "longitud": len(lista) } 
    return diccionario
mylist = [] 
mylist2 = [2,3,4]   
print(maximo(mylist))
print(maximo(mylist2))
# Lista inversa : crea una función que tome una lista y la devuelva con los valores invertidos.
#  Haz esto sin crear una segunda lista. (Se sabe que este desafío aparece durante las entrevistas técnicas básicas).
# Ejemplo: reverse_list ([37,2,1, -9]) debería devolver [-9,1,2,37]
def rever(lista):
    lista2 = lista[::-1] 
    return lista2
mylist = [1, 2, 3, 4,] 
mylist2 = [6, 3, -2]   
print(rever(mylist))
print(rever(mylist2))

def rever(lista):
    lista2 = list(reversed(lista))
    return lista2
mylist = [1, 2, 3, 4,] 
mylist2 = [6, 3, -2]   
print(rever(mylist))
print(rever(mylist2))

def rever(lista):
    return lista[::-1] 
mylist = [1, 2, 3, 4,] 
mylist2 = [6, 3, -2]   
print(rever(mylist))
print(rever(mylist2))


