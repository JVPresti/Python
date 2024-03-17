"""
pot=1
res=0

while res<1000:
    res=7**pot
    pot+=1

print(pot-1)


print("-------------")
n=1
while n<6:
    if(n==5):
        print(n)
    else:
        print(n, end=", ")
    n+=1

print("-------------")
n=5
while n!=0:
    if(n==1):
        print(n)
    else:
        print(n, end=", ")
    n-=1

print("-------------")
n=1
while n<6:
    print(n)
    n+=1

print("-------------")
n=5
while n!=0:
    print(n)
    n-=1

#Ejercicio 22

n= int(input("Ingrese un numero entero para obtener su sumatoria: "))

sumatoria=0
while n>0:
    sumatoria+=n
    n-=1
print("La sumatoria es: ", sumatoria)

#Ejercicio 23

renglon =0 
maximo_renglon=10
maximo_columna=16
cadena_renglon_columna=""

while renglon<maximo_renglon:
    columna=0
    while columna<maximo_columna:
        cadena_renglon_columna+= "*" + " "
        columna+=1
    cadena_renglon_columna+="\n"
    renglon+=1
print(cadena_renglon_columna)

#Ejercicio 24

name= input("Ingrese su nombre completo: ")
caracter= input("Teclee un solo caracter que sera su marco alrededor del nombre: ")
total= len(name)+6

while(total>0):
    print(caracter, end="")
    total-=1
print("\n",caracter, name, caracter)

total= len(name)+6
while(total>0):
    print(caracter, end="")
    total-=1    

"""

# Ejercicio 25  
nimpar = int(input("Ingrese un número impar para establecer la longitud horizontal más larga del rombo: "))
caracter = input("Ingrese el caracter que tendrá el rombo: ")

if nimpar % 2 == 0:
    print("El número no es impar")
else:
    n = 1
    espacios = nimpar // 2
    while n <= nimpar:
        print(" " * espacios + caracter * n)
        n += 2
        espacios -= 1
    
    n -= 4
    espacios = 1
    while n > 0:
        print(" " * espacios + caracter * n)
        n -= 2
        espacios += 1



