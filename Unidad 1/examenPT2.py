#Jorge Vazquez

x= float(input("Ingrese el primer numero: "))
y= float(input("Ingrese el segundo numero: "))
z= float(input("Ingrese el tercer numero: "))
iguales = 0


if (x >= y):
    if (x >= z):
        mayor = x
        if (y >= z):
            medio = y
            menor = z
        if(y<z):
            medio = z
            menor = y
    if(x < z):
        mayor = z
        medio = x
        menor = y
if(x<y):
    if (y >= z):
        mayor = y
        if (x >= z):
            medio = x
            menor = z
        if(x<z):
            medio = z
            menor = x
    if(y<z):
        mayor = z
        medio = y
        menor = x

if(x==y):
    if(x==z):
        print("Los valores ", x,",", y,",", z, " son iguales")
        iguales = 1


if(iguales == 0):
    print("Los valores ", x,",", y,",", z, " no son iguales")
    print("El orden de los numeros de forma descendete son: ", mayor, medio, menor)
if(iguales == 1):
    print("Todos los numeros son iguales, por lo tanto no es necesario mostrar su ordenamiento.")