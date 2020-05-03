import prufer as pf #se incluye el script que contiene las definiciones fundamentales

print("ingresa mensaje que deseas codificar: ")#Usuario ingresa mensaje
msg = input()
# print("¿Desea codificar el mensaje como un anagrama?")#Tipo de codificación
# ans = input()
# print("Árbol correspondiente al mensaje", uinput)
#
# if ans in ["N", "n", "No", "no", "NO"]:
#     pf.Reconstruccion_de_T(uinput)
# elif ans in ["YES", "Y", "yes", "Yes", "S", "si", "SI", "Si", "y", "s"]:
#     pf.Reconstruccion_de_T_anagrama(uinput)
mov = int(input("Ingrese el mov: "))
cif = pf.cifrado_cesar(msg, mov)
print("Este es su cifrado de cesar: ", cif)
print("Este es su decifrado: ", pf.decifrado_cesar(cif, mov))
