x = [ [5,2,3], [10,8,9] ] 

def cambiarelemento(lista):
    lista[1][0] = 15
    return lista 
print(cambiarelemento(x))

    
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
def cambiar(diccio):
    diccio[0]['last_name']= 'Bryant'
    return diccio 
print(cambiar(students))




sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
def cambiar(diccio):
    diccio['soccer'][0]= 'Andres'
    return diccio 
print(cambiar(sports_directory))

z = [ {'x': 10, 'y': 20} ] 

def cambiar(diccio):
    diccio[0]['y'] = 30
    return diccio 
print(cambiar(z))

# 2 itera a traves de una lisgta de diccionarios
# La salida debería ser: (Está bien si cada clave y valor quedan en dos líneas separadas)
# Bonus: Hacer que aparezcan exactamente así!
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(diccio):
    for elements in diccio:
        """ print(f"first_name - {elements['first_name']}, last_name - {elements['last_name']}") """ # esta linea es por el bonus
        for k, v in elements.items():
            print(k, v)
iterateDictionary(students)


# 3 Obtén valores de una lista de diccionarios
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
]  
def iterateDictionary2(key_name, some_list):
    for elements in some_list:
        print(elements[key_name])

iterateDictionary2('first_name',students)
iterateDictionary2('last_name',students)

# Itera a través de un diccionario con valores de listas

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for elements in some_dict:
        print(len(some_dict[elements]), elements.upper())
        for valores in some_dict[elements]:
            print(valores)
            if valores == 'Burbank':
                print(" ")
        

printInfo(dojo)





""" def reverse_in_place(lst):    
    size = len(lst)            
    i = size - 1
    its = size/2               
    for z in range(0, int(its)):    
        temp = lst[i]    
        lst[i] = lst[z]
        lst[z] = temp
        i -= 1           
    return lst
print(reverse_in_place([2,5,8,9,4])) """