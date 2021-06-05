#Cuenta regresiva : crea una función que acepte un número como entrada. Devuelve una nueva lista que cuenta hacia atrás en uno,
#  desde el número (como el elemento 0) hasta 0 (como el último elemento).
def Cuenta_regresiva():
    numero = int(input("Ingresa un numero entero: "))
    lista = []
    for x in range(numero, 0, -1):
        lista.append(x)
    return lista

print(Cuenta_regresiva())

#Imprimir y volver : crea una función que recibirá una lista con dos números. Imprima el primer valor y devuelva el segundo.
# Ejemplo: print_and_return ([1,2]) debería imprimir 1 y devolver 2

def imprimirVolver(a,b):
    print(a)
    return b


imprimirVolver(1,2)

#First Plus Length : crea una función que acepta una lista y devuelve la suma del primer valor de la lista más la longitud de la lista.
# Ejemplo: first_plus_length ([1,2,3,4,5]) debería devolver 6 (primer valor: 1 + longitud: 5)
def firstPlus(lista):
    for i in range(len(lista)):
        suma = lista[0] + len(lista)
    return suma

myList = [1,2,3,4,5]
print(firstPlus(myList))
# Valores mayores que el segundo : escribe una función que acepte una lista y crea una nueva lista que contenga solo los valores de la lista original que sean mayores que su segundo valor. 
# Imprima cuántos valores son y luego devuelva la nueva lista. Si la lista tiene menos de 2 elementos, haga que la función devuelva False
# Ejemplo: values_greater_than_second ([5,2,3,2,1,4]) debería imprimir 3 y devolver [5,3,4]
# Ejemplo: values_greater_than_second ([3]) debería devolver False
def valorMayor(lista):
    newList = []
    if len(lista) < 2:
        return False
    else:
        for i in range(len(lista)):
            if lista[i] > lista[1]:
                newList.append(lista[i])
         

    return newList

myList = [5,2,3,2,1,4]
list2 = [2]
print(valorMayor(list2))
# Esta longitud, ese valor : escribe una función que acepte dos enteros como parámetros: tamaño y valor.
# La función debe crear y devolver una lista cuya longitud es igual al tamaño dado y cuyos valores son todos los valores dados.
# Ejemplo: length_and_value (4,7) debería devolver [7,7,7,7]
# Ejemplo: length_and_value (6,2) debería devolver [2,2,2,2,2,2]
def Longitud2(tamaño, valor):
    newlista = []
    for x in range (tamaño+1):
        newlista.append(valor)
    return newlista

print(Longitud2(6,2))


