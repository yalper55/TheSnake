from os import system
import time
import random


def borrarContenido():
    "Borra el contenido mostrado anteriormente luego de 1.5 segundos"
    time.sleep(1.5)
    system("cls")


def sumarNumeros(A, B):
    "Devuelve la suma del primer elemento con el segundo"
    return A+B

# A esta funcion se le puede agregar un return si se busca almacenar el resultado


def tirarDados():
    "Genera dos numeros al azar entre 1 y 6, luego los suma e imprime por pantalla"
    Guion = '-'
    primer_numero = random.randint(1, 6)
    segundo_numero = random.randint(1, 6)
    print("El primer dado arrojó:", primer_numero,
          "\nEl segundo dado arrojó:", segundo_numero)
    print("La suma de ambos numeros es:",
          sumarNumeros(primer_numero, segundo_numero))
    print(Guion*31)
    time.sleep(1.5)

# En este programa el usuario recibe la bienvenida, y se le dan dos opciones
# Tirar los dados o salir, usando una interfaz bastante sencilla,


def menuPrincipal():
    TirarDados = True
    Error = False
    print("Bienvenido")
    while(TirarDados):
        opcion = input("\nElija su opcion \n[1:Tirar dados]\t[2:Salir]\n:")
        if opcion == '1':
            borrarContenido()
            tirarDados()
        elif opcion == '2':
            borrarContenido()
            print("Gracias por probar esta aplicacion.")
            time.sleep(1)
            break
        else:
            print("Opcion Incorrecta, vuelva a intentarlo")
            Error = True

        if Error == True:
            borrarContenido()
            Error = False


menuPrincipal()
