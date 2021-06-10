import random
def randInt(min= 0 , max= 100 ):
    if min > max:
        return ("El numero minimo debe ser mayor al numero maximo")
    elif max <= 0:
        return ("El numero maximo debe ser mayor a 0")
    else:    
        num = (random.random() * (max-min) + min)
    return round(num)
print(randInt())
print(randInt(max=50))
print(randInt(min=50))
print(randInt(min=50, max=500))
print(randInt(min=50, max=0))