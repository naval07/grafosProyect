import prufer as pf #se incluye el script que contiene las definiciones fundamentales

difs = ["1","2","3"]
print(
                            "\n\t\t\t\t\tBienvenido al encriptador\n\n"
    "REGLAS\n"
        "\n\t1) Escribe un mensaje y la contraseña con el abecedario americano, es decir,\n\t"
        "sin tíldes ni la letra ñ.\n\t"
        "2) La longitud del mensaje debe ser menor o igual a 280.\n\t"
        "3) Escribir los números letra por letra. Tanto para el mensaje como para\n\t"
        "la contraseña. (Ej: trece)\n\t"
        "4) La contraseña debe ser menor o igual de larga que el mensaje.\n\t"
        "5) El título del mensaje puede contener distintos caracteres, incluyendo números.\n\n"
    "¿CÓMO FUNCIONA?\n\n"
        "\tPrimero, elige un nivel entre los niveles de dificultad de la encripación:\n\t"
            "\t1) Básico\n\t"
            "\t2) Difícil\n\t"
            "\t3) Imposible (No tenemos desencriptado)\n\t"
        "Una vez escogido el nivel de encriptación, escribe el mensaje que quieras encpritar\n\t"
        "y seguidamente su contraseña. Esta contraseña la va a necesitar el receptor del mensaje.\n\t"
        "Una vez ingresados estos datos, se guardarán dos archivos en la carpeta contenedora de\n\t"
        "este documento:\n\n\t"
            "\ta. El primer archivo es una foto, la cual contiene una representacion del \n\t"
            "\tmensaje encriptado en un grafo acíclico y conexo.\n\n\t"
            "\tb. El segundo archivo consiste en un documento de texto en el cual se almacena\n\t"
            "\tla estructura computacional del grafo.\n\n"
)

print("EJECUCIÓN\n")
msg = input("\t Ingrese el mensaje: ")
dif = input("\t Ingrese el nivel de dificultad (sólo el número): ")

while dif not in difs:
    dif = input("\t Error! ingrese un nivel adecuado: ")

if dif == "1":
    pf.crypt(msg)

elif dif == "2":
    pf.cryptSecret(msg)

else:
    pf.cryptAnagram(msg)

print("¡Listo!")
