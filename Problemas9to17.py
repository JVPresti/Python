"""
Jorge Vazquez

# Ejercicio 9

print(ord('A'), ord('B'), ord('C'), ord('D'), ord('b'))
print(ord('c'), ord('d'), ord('0'), ord('1'), ord('2'), ord('$'), ord('*'), ord('+'), ord(' '))

# Ejercicio 10
n1= float(input("Ingrese el primer número: "))
n2= float(input("Ingrese el segundo número: "))
n3= float(input("Ingrese el tercer número: "))
print("La suma de los numeros es: ", n1+n2+n3)
print("El promedio de los numeros es: ", (n1+n2+n3)/3)
print("El producto de los numeros es: ", n1*n2*n3)
if(n1>n2):
    if(n1>n3):
        print("El mayor de los numeros ", n1, n2, n3, "es: ", n1)
if(n2>n1):
    if(n2>n3):
        print("El mayor de los numeros ", n1, n2, n3, "es: ", n2)
if(n3>n1):
    if(n3>n2):
        print("El mayor de los numeros ", n1, n2, n3, "es: ", n3)
        
if(n1<n2):
    if(n1<n3):
        print("El menor de los numeros ", n1, n2, n3, "es: ", n1)
if(n2<n1):
    if(n2<n3):
        print("El menor de los numeros ", n1, n2, n3, "es: ", n2)
if(n3<n1):
    if(n3<n2):
        print("El menor de los numeros ", n1, n2, n3, "es: ", n3)

# Ejercicio 11

num= input("Ingresa un valor entero de 5 digitos: ")
print("El numero ingresado es: ", num)
print(" ", num[0], " ", num[1], " ", num[2], " ", num[3], " ", num[4])

# Ejericio 12

print("Si empiezas con 100,000.00 e inviertes por 30 años a un interes del 7%")
a= 100000*(1+0.07)**30
print("Tendrás: ", a)
# Ejercicio 13

import sys

sys.set_int_max_str_digits(14300)

print("El valor de exponente maximo sin utilizar alguna funcion es de 14285")
print("El valor de exponente maximo utilizando alguna funcion puede variar dependiendo la necesidad")

# Ejercicio 14

n= input("Ingresa un numero para regresar el ultimo digito: ")
print("El ultimo digito del numero ", n, " es: ", n[-1])

# Ejercicio 15

num1= float(input("Ingresa el primer numero: "))
num2= float(input("Ingresa el segundo numero: "))
num3= float(input("Ingresa el tercer numero: "))

menor= num1

if(num2<menor):
    menor= num2
if(num3<menor):
    menor= num3
print("El menor de los numeros es: ", menor)
# Ejercicio 16

a= float(input("Ingresa el primer numero: "))
b= float(input("Ingresa el segundo numero: "))
c= float(input("Ingresa el tercer numero: "))

if(a==b):
    if(a==c):
        print("Los valores ", a,",", b,",", c, " son iguales")
if(a!=b and a!=c):
    if(a!=c):
        print("Los valores ", a,",", b,",", c, " no son iguales")

# Ejercicio 17

x= float(input("Ingresa el primer numero: "))
y= float(input("Ingresa el segundo numero: "))
z= float(input("Ingresa el tercer numero: "))

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


print("El orden de los numeros de forma ascendente es: ", menor, medio, mayor)
"""