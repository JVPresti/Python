"""
#Ejercicio 5

n= int(input("Ingrese un numero entero para evaluar si es par o impar: "))
if n%2==0:
    print("El numero entero ",n," es par")
else:
    print("El numero entero ",n," es impar")

# Ejercicio 6
    
n1= int(input("Ingrese el primer entero: "))
n2= int(input("Ingrese el segundo entero: ")) 
if(n1>n2):
    if(n1%n2)==0:
        if n1<n2:
            print(n1, 'es múltiplo de', n2) 
        else:
            print(n2, "es multiplo de ", n1)
    else:
        if n1<n2:
            print(n1, 'no es múltiplo de', n2) 
        else:
            print(n2, "no es multiplo de ", n1) 
else:
    if(n2%n1)==0:
        if n1<n2:
            print(n1, 'es múltiplo de', n2) 
        else:
            print(n2, "es multiplo de ", n1)
    else:
        if n1>n2:
            print(n1, 'no es múltiplo de', n2) 
        else:

# Ejercicio 7
        
a= float(input("Ingresa el primer numero: "))
b= float(input("Ingresa el segundo numero: "))
c= float(input("Ingresa el tercer numero: "))

if(a==b):
    if(a==c):
        print("Los valores ", a,",", b,",", c, " son iguales")
else:
    if(a!=c):
        print("Los valores ", a,",", b,",", c, " no son iguales")
"""



calif= float(input("Ingresa tu calificación: "))

if calif >= 90:
    print("A")
elif calif >= 80:
    print("B")
elif calif >= 70:
    print("C")
elif calif >= 60:
    print("D")
else:
    print("F")

