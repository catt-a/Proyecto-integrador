import random

# Categorias disponibles:
CATEGORIAS = (
    ("Letras mayusculas", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
    ("Letras minusculas", "abcdefghijklmnopqrstuvwxyz"),
    ("Numeros",          "0123456789"),
    ("Simbolos",         "!@#%^&*()-_=+[];,.?"))

    
def pedir_longitud():
    longitud = 0
    while longitud <= 0:
        entrada = input("Ingresa la longitud de la contrasena: ")
        if entrada.isdigit():
            longitud = int(entrada)
            if longitud <= 0:
                print("La longitud debe ser mayor que cero.")
        else:
            print("Debes ingresar un numero entero positivo.")
    return longitud


def seleccionar_caracteres():
    print("\nSelecciona los tipos de caracteres que quieres usar:")
    for i in range(len(CATEGORIAS)):
        print(str(i + 1) + ". " + CATEGORIAS[i][0])

    seleccion = input("\nEscribe los numeros separados por comas (ejemplo: 1,2,3): ")
    partes = seleccion.split(",")

    caracteres = ""
    for parte in partes:
        parte = parte.strip()
        if parte.isdigit():
            numero = int(parte)
            if 1 <= numero <= len(CATEGORIAS):
                # Agregar caracteres elegidos
                caracteres = caracteres + CATEGORIAS[numero - 1][1]

    if caracteres == "":
        print("Selecciona al menos una categoria.")
        return seleccionar_caracteres()

    return caracteres


def generar_contrasena(longitud, caracteres):
    contrasena = ""
    for i in range(longitud):
        indice = random.randint(0, len(caracteres) - 1)
        contrasena = contrasena + caracteres[indice]
    return contrasena


def main():
    print("Generador seguro de contrasenas\n")

    continuar = True
    while continuar:
        longitud = pedir_longitud()
        caracteres = seleccionar_caracteres()
        contrasena = generar_contrasena(longitud, caracteres)

        print("\nContrasena generada: " + contrasena)
        print("Longitud: " + str(len(contrasena)) + " caracteres")

        respuesta = input("\nDeseas generar otra contrasena? (si/no): ")
        if respuesta.lower() != "si":
            continuar = False

    print("\nPrograma finalizado")


main()