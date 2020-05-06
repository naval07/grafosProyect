import prufer as pf

difs = ["1","2","3"]
print(
                            "\n\t\t\t\t\tBienvenido al desencriptador\n\n"
"REGLAS\n"
        "\n\t1) Todos los caractéres que ingreses tienen que pertenecer al abecedario américano.\n\t"
        "Es decir, sin tíldes y sin la letra ñ.\n\t"
        "2) Asegurate de ingresar correctamente el título del mensaje y su contraseña.\n\t"
        "3) La contraseña no puede tener números ni caracteres ajenos al abecedario.\n\n"
"¿CÓMO FUNCIONA?\n\n"
        "\t-Primero, ingresa el título del mensaje que quieras desencriptar.\n\t"
        "-Segundo, ingresa el número del nivel en el que fue encriptado el mensaje.\n\t"
        "-Por último ingresa la contraseña con la que fue encriptado el mensaje.\n\t"
        "Y listo, ¡Verás como el mensaje es impreso por la terminal!\n\n"
)

print("EJECUCIÓN\n")

title = input("\t Ingrese el título del mensaje: ")
dif = input("\t Ingrese la dificultad de encriptado: ")

if dif == "1":
    pf.decrypt(msg)

elif dif == "2":
    pf.decryptSecret(msg)

else:
    print("Lo sentimos, esto es un problema de grado factorial.")
