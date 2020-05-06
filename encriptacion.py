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
        "\tPrimero, elige un único nivel entre los niveles de dificultad de la encripación:\n\t"
            "\t1) Básico\n\t"
            "\t2) Difícil\n\t"
            "\t3) Imposible (No tenemos desencriptado)\n\t"
        "Una vez escogido el nivel de encriptación, escribe el mensaje que quieras encpritar\n\t"
        "y seguidamente su contraseña. Esta contraseña la va a necesitar el respectivo receptor.\n\t"
        "Por ultimo, debes ingresar el título del mensaje para que de este modo no se confunda con\n\t"
        "ningún otro mensaje digitado previamente. Una vez ingresados estos datos, se guardarán tres\n\t"
        "archivos:\n\n\t"
            "\ta. El primer archivo es una foto, la cual contiene una representacion del mensaje\n\t"
            "\tencriptado en un grafo acíclico y conexo. Éste está almacenado en la carpeta /images\n\t"
            "\ty llevará por nombre el título del mensaje.\n\n\t"
            "\tb. El segundo y tercer archivo consisten en la estructura computacional del grafo. Estos\n\t"
            "\testarán almacenados en la carpeta /graphs.\n\n"
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
