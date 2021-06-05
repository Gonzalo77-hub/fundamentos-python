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

    promedio = round(suma/len(lista))

    diccionario = { "minimo":minimo, "maximo": maximo, "promedio": promedio, "suma": suma}
    return   diccionario  
""" val= max([7,1,2,3,4,5]) """
""" val2 = min([7,1,2,3,4,5]) """
print(funcion([7,1,2,3,4,5]))
""" print(val) """

# Imprime en ese caso "Es palindroma"
miCadenaDeTexto = "ojo"
if str(miCadenaDeTexto) == str(miCadenaDeTexto)[::-1]:
    print("Es palindroma")
else:
    print("No es palindroma")

def function(lista=[]):
    if len(lista) < 2:
        return False,     
    else:         
        primer = lista[0]         
        ultimo = lista[-1]                
        return primer, ultimo      

lista_1 = [1, 2, 3, 4] 
lista_2 = [2] 
primer, ultimo = function(lista_1) 
print(f"el primero es {primer} y el ultimo es {ultimo}")

# Crea una función que tome una lista y devuelva el primer y el último valor de la lista. Si la longitud de la lista es menor que 2, haga que devuelva False.
def valorMayor(lista):
    newList = []
    if len(lista) < 2:
        return False
    else:
        primer = []

    return 

myList = [5,2,3,2,1,4]
list2 = [2]
print(valorMayor(list2))
