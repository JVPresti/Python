# Jorge Vazquez
# OnlyCodes
"""

# Ejercicio 30
cad1 = "Horas"
cad2 = "Numero de bacterias"
time = 0
bac = 200
nbac = 0

print(cad1, "\t", cad2, sep=(" "))

for i in range(5):
    print(time, " \t", nbac, sep=(" "))
    time += 5
    nbac = 200 * 2 ** time
print("\n")
time = 0
nbac = 0

print(f"{cad1:>5} {cad2:>25}")
for i in range(5):
    print(f"{time:>5} {nbac:>25}")
    time += 5
    nbac = 200 * 2 ** time


# Ejercicio 31

time = int(input("Ingrese el tiempo en segundos: "))

h = time // 3600
time = time % 3600
m = time // 60
s = time % 60

print(h, m, s, sep=(" -"))


# Ejercicio 32

time = int(input("Ingresar el tiempo en segundos: "))

hr = time // 3600
sr = time % 3600
m = sr // 60
s = sr % 60

print("Horas:", hr, "Minutos:", m, "Segundos:", s)


# Ejercicio 33

num = int(input("Ingrese un entero positivo para saber si es un numero perfecto: "))
sum = 0

for i in range(1, num):
    if num % i == 0:
        sum = sum+i


if sum == num:
    print("El numero ", num, "es perfecto")
else:
    print("El numero ", num, "no es perfecto")


# Ejercicio 34

bin = int(input("Ingrese el numero binario: "))
pb = bin

decimal = 0
posicion = 0
while bin > 0:
    digito = bin % 10
    decimal += digito * (2 ** posicion)
    bin //= 10
    posicion += 1

print("El numero binario", pb, "en decimal es", decimal)


# Ejercicio 35

decimal = int(input("Ingrese el numero entero positivo: "))
dc = decimal
bin = 0
pos = 1
while decimal > 0:
    digitoB = decimal % 2
    bin += digitoB * pos
    decimal //= 2
    pos *= 10

print("El numero entero", dc, "en binario es", bin)


# Ejercicio 36

num = int(input("Ingrese un numero para determinar si es capicua: "))
reverso = 0
numOri = num

while num > 0:
    digito = num % 10
    reverso = reverso * 10 + digito
    num //= 10

if reverso == numOri:
    print("El numero", numOri, "es capicua!")
else:
    print("El numero", numOri, "no es capicua")


# Ejercicio 37

txtUser = input(
    "Ingrese la palabra o frase para determinar si es palindromo o no: ")

# Convertir el texto a minúsculas
txt = ''
for char in txtUser:
    if 'A' <= char <= 'Z':
        char = chr(ord(char) + 32)
    txt += char

txtNorm = ''
for char in txt:
    if 'a' <= char <= 'z' or '0' <= char <= '9':
        txtNorm += char

txtInv = ''
for i in range(len(txtNorm) - 1, -1, -1):
    txtInv += txtNorm[i]

if txtNorm == txtInv:
    print("La palabra o frase es palindrome!")
else:
    print("La palabra o frase no es palindrome :(")

"""
