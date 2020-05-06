import numpy as np

abc = [chr(x) for x in range(97,123)]
ABC = [chr(x) for x in range(65,91)]
dic = {}
c = 0
for q in abc:
    dic[q] = c
    c += 1

# return the text in lowercase and a list of the upppercase letters indexes
def lowercase(msg):
    global abc, ABC
    upper_indexes = []
    new_msg = ""
    count = 0
    for q in msg:
        if q in ABC:
            new_msg += q.lower()
            upper_indexes.append(count)
        else:
            new_msg += q
        count += 1
    return new_msg, upper_indexes

# put the respectives letters in uppercase recursively
def set_uppercases(msg, indexes):
    idxs = indexes[0:] # copy of indexes
    msg_aux = msg # copy of msg
    new_msg = ""
    if len(idxs) == 0:
        return msg_aux
    elif idxs[0] == 0:
        new_msg += msg_aux[0].upper()
        msg0 = msg_aux[1:]
        idxs.remove(0)
        for q  in range(len(idxs)):
            idxs[q] -= 1
    else:
        new_msg += msg_aux[:idxs[0]]
        new_msg += msg_aux[idxs[0]].upper()
        msg0 = msg_aux[idxs[0] + 1:]
        idx0 = idxs[0]
        idxs.remove(idx0)
        for q in range(len(idxs)):
            idxs[q] -= idx0 + 1
    return new_msg + set_uppercases(msg0, idxs)

# create the Vigenere matrix
def create_mat():
    mat = []
    for q in range(26):
        l = abc[q:]
        l += abc[:q]
        mat.append(l)
    mat = np.array(mat)
    return mat

# set the password to the message
def getPass(msg, pas):
    while len(pas) > len(msg):
        pas = input("\t Error! Longitud de la contraseña muy larga. Por favor, ingrese una nueva: ")
    str = ""
    c_p, c_m = 0, 0
    while c_m < len(msg):
        if c_p < len(pas):
            if msg[c_m] == " ":
                str += " "
                c_m += 1
            else:
                str += pas[c_p]
                c_m += 1
                c_p += 1
        else:
            c_p = 0
    return str

# cifrate the message with its respective password
def code(msg, pas):
    global dic
    matrix = create_mat()
    pasw = getPass(msg, pas).lower()
    msg_aux, indexes = lowercase(msg)
    cif = ""
    for q in range(len(msg_aux)):
        # do not code the simbols
        if msg_aux[q] not in abc:
            cif += msg_aux[q]
        # code the letters
        else:
            row = dic[pasw[q]]
            column = dic[msg_aux[q]]
            cif += matrix[row][column]
    return set_uppercases(cif, indexes)

# Decode the message mathematically
def decode(msg, pas):
    global dic
    pasw = getPass(msg,pas).lower()
    msg_aux, indexes = lowercase(msg)
    deco = ""
    for q in range(len(msg_aux)):
        if msg_aux[q] not in abc:
            deco += msg_aux[q]
        else:
            n = dic[msg_aux[q]] # value of the letter q in msg (Ej. msg[q] = a ent. n = 0)
            m = dic[pasw[q]] # value of the letter q in pas (Ej. pas[q] = z ent. m = 25)
            letter = (n - m) % 26
            # get the key of the value letter
            for key, value in dic.items():
                if letter == value:
                    deco += key
                    break
    return set_uppercases(deco, indexes)

# main
if __name__ == "__main__":
    print("\t¡Texto no mas de 280 caracteres, sin tildes y de clave una sola palabra!\n")
    msg = input("Ingrese el texto a cifrar:\t")
    pas = input("Ingrese la clave de cifrado:\t")
    print("cifrado:\t\t\t", code(msg,pas))
    cif = code(msg,pas)
    print("Decifrado: \t\t\t", decode(cif, pas))
