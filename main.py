import prufer as pf #se incluye el script que contiene las definiciones fundamentales

print("ingresa mensaje que deseas codificar: ")#Usuario ingresa mensaje
uinput = input()
print("¿Desea codificar el mensaje como un anagrama?")#Tipo de codificación
ans = input()
print("Árbol correspondiente al mensaje", uinput)

if ans in ["N", "n", "No", "no", "NO"]:
    pf.Reconstruccion_de_T(uinput)
elif ans in ["YES", "Y", "yes", "Yes", "S", "si", "SI", "Si", "y", "s"]:
    pf.Reconstruccion_de_T_anagrama(uinput)