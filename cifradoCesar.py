def code(msg, mov):
    """Cifrado César modificado: altera el órden de ubicación de caracteres
    de una cadena ingresada cierto número de movimientos en el abecedario"""
    new = ""
    minus = [chr(x) for x in range(97, 123)]
    mayus = [chr(x) for x in range(65, 91)]
    corres = {}
    mv = mov % 26
    for i in range(0, 26):
        if i + mov < 26:
            corres[minus[i]] = minus[i + mv]
            corres[mayus[i]] = mayus[i + mv]
        else:
            corres[minus[i]] = minus[i + mv - 26]
            corres[mayus[i]] = mayus[i + mv - 26]
    for l in msg:
        if l in mayus + minus:
            new += corres[l]
        else:
            new += l
    return new

def decode(msg, mov):
    """Decifra el mensaje cifrado con el metodo anterior y su respectivo numero de
    movimiento"""
    new = ""
    minus = [chr(x) for x in range(97, 123)]
    mayus = [chr(x) for x in range(65, 91)]
    corres = {}
    mv = mov % 26
    for i in range(0, 26):
        if i - mov < 26:
            corres[minus[i]] = minus[(i - mv) % 26]
            corres[mayus[i]] = mayus[(i - mv) % 26]
        else:
            corres[minus[i]] = minus[(i - mv - 26) % 26]
            corres[mayus[i]] = mayus[(i - mv - 26) % 26]
    for l in msg:
        if l in mayus + minus:
            new += corres[l]
        else:
            new += l
    return new
