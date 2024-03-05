# Jorge Vazquez

nhuevos = int(input("Ingresar la cantidad de huevos obtenidos: "))
carteras= nhuevos // 6
need = nhuevos - (carteras * 6)
no = 1
si = 1

if(nhuevos == 0):
    print("La cantidad de huevos que se necesitan para llenar una cartera es de: 6. ")
    no=0

if(nhuevos % 6 == 0):
    if(no != 0):
        if(carteras == 1):
            print("Se lleno ", carteras, " carteras de 6 huevos")
            si=0
        if(carteras != 1):
            print("Se llenaron ", carteras, " carteras de 6 huevos")
            si=0
if(nhuevos % 6 != 0):
    if(carteras != 0):
        if(carteras == 1):
            print("Se lleno ", carteras, " carteras de 6 huevos")
            si=0
        if(carteras != 1):
            print("Se llenaron ", carteras, " carteras de 6 huevos")
            si=0

if(nhuevos % 6 != 0):
    if(no == 0):
        if(si != 0):
            print("La cantidad de huevos que se necesitan para llenar una cartera es de: 6. ")

if(nhuevos % 6 != 0):
    if(si != 0):
        print("La cantidad de huevos que se necesitan para llenar una cartera es de:", 6-need,".")
    if(nhuevos %6 == 1):
        print("En la ultima cartera se coloco: ", nhuevos % 6, "huevo")
    if(nhuevos %6 != 1):
        print("En la ultima cartera se colocaron: ", nhuevos % 6, "huevos")
    print("La cantidad de huevos adicionales que se necesitan para llenar la ultima cartera es de: ", 6-need, ".")
