"""
Jorge Vazquez
OnlyCodes

# Ejercicio 1

x=2
y=3
print('x=',x) # Imprime que x es igual a 2 en pantalla
print('Value of', x, '+', x, 'is', (x + x)) # Imprime el valor de x + x en pantalla mostrando con todo y suma
print('x=') # Imprime x= en pantalla
print((x+y), 'x=', (x+y)) # Imprime el valor de x+y y luego x= y el valor de x+y

# Ejercicio 2

# calificacion= input("Ingrese una calificación entre 1 y 100: ") #El problema es que no se especifica que tipo de dato se espera

# Ejercicio 3

calificacion= int(input("Ingrese una calificación entre 1 y 100: ")) #Se espera un número entero
if calificacion>= 90:
    print('Felicidades, tu calificacion de 91 te otorga una A en este curso.')

# Ejercicio 4
    
radio= 2
pi= 3.14159

print('El diámetro de la circunferencia es', 2*radio) #Imprime el diámetro de la circunferencia
print("La circunferencia de la circunferencia es", 2*pi*radio) #Imprime la circunferencia de la circunferencia
print("El área de la circunferencia es", pi*radio**2) #Imprime el área de la circunferencia

# Ejercicio 5

dato= int(input("Ingrese un número entero a evaluar si es par o no: ")) #Se espera un número entero
if(dato%2)==0:
    print(dato, 'es par.') #Imprime que el número es par
if(dato%2)!=0:
    print(dato, 'es impar.') #Imprime que el número es impar

# Ejercicio 6

n1= int(input("Ingrese el primer entero: ")) #Se espera un número entero
n2= int(input("Ingrese el segundo entero: ")) #Se espera un número entero
if(n1>n2):
    if(n1%n2)==0:
        print(n1, 'es múltiplo de', n2) #Imprime que n1 es múltiplo de n2
    if(n1%n2)!=0:
        print(n1, 'no es múltiplo de', n2) #Imprime que n1 no es múltiplo de n2
if(n1<n2):
    if(n2%n1)==0:
        print(n2, 'es múltiplo de', n1) #Imprime que n2 es múltiplo de n1
    if(n2%n1)!=0:
        print(n2, 'no es múltiplo de', n1) #Imprime que n2 no es múltiplo de n1
    
# Ejercicio 7

print("Numero\tCuadrado\tCubo") #Imprime el encabezado de la tabla
print(0, '\t', 0**2, '\t\t', 0**3) #Imprime el valor de 0, su cuadrado y su cubo
print(1, '\t', 1**2, '\t\t', 1**3) #Imprime el valor de 1, su cuadrado y su cubo
print(2, '\t', 2**2, '\t\t', 2**3) #Imprime el valor de 2, su cuadrado y su cubo
print(3, '\t', 3**2, '\t\t', 3**3) #Imprime el valor de 3, su cuadrado y su cubo
print(4, '\t', 4**2, '\t\t', 4**3) #Imprime el valor de 4, su cuadrado y su cubo
print(5, '\t', 5**2, '\t\t', 5**3) #Imprime el valor de 5, su cuadrado y su cubo

# Ejercicio 8

print(f'{"Número":>7} {"Cuadrado":>9} {"Cubo":>9}')
print(f'{0:>7} {0**2:>9} {0**3:>9}')
print(f'{1:>7} {1**2:>9} {1**3:>9}')
print(f'{2:>7} {2**2:>9} {2**3:>9}')
print(f'{3:>7} {3**2:>9} {3**3:>9}')
print(f'{4:>7} {4**2:>9} {4**3:>9}')
print(f'{5:>7} {5**2:>9} {5**3:>9}')


"""