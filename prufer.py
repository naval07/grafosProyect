import networkx as nx #Librería usada para generar el grafo.
import matplotlib.pyplot as plt #Librería usada para mostrar el grafo generado.
import cifradoVigenere as cv #Modulo del cifrado de Vigenere
import cifradoCesar as cc #Modulo del cifrado de César
import os #Módulo para escribir y leer archivos txt


"""creación del diccionario que le asigna un caracter a un número"""
l = [chr(x) for x in range(256, 537)]
i = 0
dic = {}
for q in range(len(l)):
    dic[str(i)] = l[q]
    i += 1

"""creación del diccionario que le asigna un número a un caracter ajeno
al texto"""
j = 0
cid = {}
for q in l:
    cid[q] = str(j)
    j += 1

#---------- Funciones de ayuda -----------------

def word_nodes(word):
    """Crea la lista de nodos con los diferentes caracteres del mensaje."""
    L = []
    while len(word) > 0:
        x = word[0]
        if x in L:
            pass
        else:
            L.append(x)
        word = word[1:]
    return L

def complete_nodes(word):
    """Añade nuevos vértices para completar
    de manera adecuada las iteraciones del algoritmo."""
    len_word = len(word)
    graph_nodes = word_nodes(word)
    i = 0
    while len(graph_nodes) != len_word + 2:
        graph_nodes.append(str(i))
        i += 1
    return graph_nodes

def complete_nodes_anagrama(word):
    """Añade nuevos vértices para completar
    de manera adecuada las iteraciones del algoritmo."""
    len_word = len(word)
    graph_nodes = word_nodes(word)
    i = 0
    while len(graph_nodes) != len_word + 2:
        graph_nodes.append(str(i))
        i += -1
    return graph_nodes

def next_min(nodos, msg):
    """retorna el segundo mínimo del conjunto en caso de que el mínimo pertenezca
    al mensaje"""
    aux = []
    while min(nodos) in msg:
        aux.append(min(nodos))
        nodos.remove(min(nodos))
    x = min(nodos)
    nodos.remove(x)
    nodos += aux
    return x

def numbers2letter(nodo_num):
    """si el nodo está marcado con un valor numérico se cambian estos por
    caracteres ajenos al mensaje para generar más privacidad"""
    return dic[nodo_num]

def letter2number(nodo_let):
    """si el nodo está marcado con un caracter ajeno a mensaje, se cambia este
    por uno numérico para generar de manera adecuada la reconstrucción del
    código de Prüfer"""
    return cid[nodo_let]

def guardarGrafo(G, title):
    plt.savefig(title+".PNG")
    nodos = open(title+"N.txt", "w")
    for x in G.nodes:
        nodos.write(x + "*")
    nodos.write("stop")
    nodos.close()
    aristas = open(title+"E.txt", "w")
    for x in G.edges:
        aristas.write(x[0] + "*" + x[1] + os.linesep)
    aristas.close()

#----------Cifrado de Mensajes a Grafos-----------------

def crypt(msg):
    """Algoritmo que toma un mensaje como código de Prüfer y una constraseña de cifrado
    para crear una codificacion del mensaje, un árbol T"""

    assert(len(msg) <= 280), u"Mensaje muy largo. Máximo 280 caracteres"
    # cifra la contraseña mediante el cif. de Cesar con su long.
    pas = input("\t Ingrese la contraseña: ")
    while len(pas) == 0:
        pas = input("\t Error! No ingresó contraseña. Por favor,\n\t Ingrese una contraseña nueva: ")
    #assert(len(pas) >0), u"No ingresó contraseña"
    pasCes = cc.code(pas, len(pas))
    # cifra el mensaje mediante el cif. de Vigenere
    msgVige = cv.code(msg, pasCes)
    nodos = complete_nodes(msgVige)
    G = nx.Graph()
    G.add_nodes_from(nodos)
    while len(nodos) != 2 and len(msgVige) > 0:
        a = msgVige[0]
        if min(nodos) not in msgVige:
            x = min(nodos)
            G.add_edge(x, a)
            nodos.remove(x)
        else:
            x = next_min(nodos, msgVige)
            G.add_edge(x, a)
        msgVige = msgVige[1:]

    G.add_edge(nodos[0], nodos[1])
    nx.draw(G, with_labels = True, node_size = 350)
    #plt.show()

    title = input("\t Ingrese el título del mensaje: ")

    # Guarda el grafo
    guardarGrafo(G, title)

    print("\n\t Preparando grafo...")

    return G

def cryptAnagram(msg):
    """Similar al anterior, pero distribuye los nodos de tal forma que
    al escribir el código se retorne en forma de anagrama.(No cuenta con
    desencriptacion)"""

    assert(len(msg) <= 280), u"Mensaje muy largo. Máximo 280 caracteres"
    # cifra la contraseña mediante el cif. de Cesar con su long.
    pas = input("\t Ingrese la contraseña: ")
    while len(pas) == 0:
        pas = input("\t Error! No ingresó contraseña. Por favor,\n\t Ingrese una contraseña nueva: ")
    #assert(len(pas) >0), u"No ingresó contraseña"
    pasCes = cc.code(pas, len(pas))
    # cifrra el mensaje mediante el cif. de Vigenere
    msgVige = cv.code(msg, pasCes)
    nodos = complete_nodes_anagrama(msgVige)
    G = nx.Graph()
    G.add_nodes_from(nodos)
    while len(nodos) != 2 and len(msgVige) > 0:
        a = msgVige[0]
        if min(nodos) not in msgVige:
            x = min(nodos)
            G.add_edge(x, a)
            nodos.remove(x)
        else:
            x = next_min(nodos, msgVige)
            G.add_edge(x, a)
        msgVige = msgVige[1:]

    G.add_edge(nodos[0], nodos[1])
    nx.draw(G, with_labels = True, node_size = 350)

    title = input("\t Ingrese el título del mensaje: ")
    # guarda el grafo
    guardarGrafo(G, title)

    print("\nPreparando grafo...")
    #plt.show()

def cryptSecret(msg):
    """Algoritmo que toma un mensaje como código de Prüfer y lo transforma
    en un árbol T sin indicar que hoja es el mínimo (usando la definición
    cambio())"""

    assert(len(msg) <= 280), u"Mensaje muy largo. Máximo 280 caracteres"
    # cifra la contraseña mediante el cif. de Cesar con su long.
    pas = input("\t Ingrese la contraseña: ")
    while len(pas) == 0:
        pas = input("\t Error! No ingresó contraseña. Por favor,\n\t Ingrese una contraseña nueva: ")
    # assert(len(pas) >0), u"No ingresó contraseña"
    pasCes = cc.code(pas, len(pas))
    # cifrra el mensaje mediante el cif. de Vigenere
    msgVige = cv.code(msg, pasCes)
    list_num = []
    for h in range(280):
        list_num.append(str(h))

    new_nodos = []
    nodos = complete_nodes(msgVige)
    G = nx.Graph()
    G.add_nodes_from(nodos)
    while len(nodos) != 2 and len(msgVige) > 0:
        a = msgVige[0]
        if min(nodos) not in msgVige:
            x = min(nodos)
            if x in list_num:
                G.add_edge(numbers2letter(x), a)
            else:
                G.add_edge(x, a)
            nodos.remove(x)
        else:
            x = next_min(nodos, msgVige)
            if x in list_num:
                G.add_edge(numbers2letter(x), a)
            else:
                G.add_edge(x, a)
        new_nodos.append(x)
        msgVige = msgVige[1:]

    for v in new_nodos:
        if v in list_num:
            G.remove_node(v)

    G.add_edge(nodos[0], nodos[1])

    nx.draw(G, with_labels = True, node_size = 300)
    title = input("\t Ingrese el título del mensaje: ")

    # guarda el grafo
    guardarGrafo(G, title)

    print("\nPreparando grafo...")
    #plt.show()

    # return G

#---------Descifrado de Grafos a mensajes--------------

def decrypt(title):
    """Toma un árbol y retorna el mensaje en código de Prüfer"""
    A = nx.Graph()
    # añade nodos
    nodos = open(title + "N.txt", "r")
    line = nodos.read()
    while line[:4] != "stop":
        sep = line.find("*")
        A.add_node(line[:sep])
        line = line[sep+1:]
    nodos.close()
    #añade aristas
    aristas = open(title + "E.txt" , "r")
    for li in aristas.readlines():
        sep = li.find("*")
        u = li[:sep]
        v = li[sep+1:-1]
        A.add_edge(u,v)
    aristas.close()

    nx.draw(A, with_labels = True, node_size = 350)
    #plt.show()

    prufer = ""
    while len(A.nodes()) != 2:
        hojas = []
        for x in A.nodes():
            if A.degree(x) == 1:
                hojas.append(x)
        if len(hojas) > 0:
            s = min(hojas)
            for v in A.nodes():
                if (s, v) in A.edges() or (v, s) in A.edges():
                    prufer += v
            A.remove_node(s)

    pas = input("\t Ingrese la contraseña: ")
    while len(pas) == 0:
        pas = input("\t Error! No ingresó contraseña. Por favor,\n\t Ingrese una contraseña nueva: ")

    pas = cc.code(pas, len(pas))
    prufer = cv.decode(prufer, pas)

    return prufer

def decryptSecret(title): #title
    """Toma un árbol sin nodos numéricos y lo transforma a código de Prüfer"""
    A = nx.Graph()
    # añade nodos
    nodos = open(title + "N.txt", "r")
    line = nodos.read()
    while line[:4] != "stop":
        sep = line.find("*")
        A.add_node(line[:sep])
        line = line[sep+1:]
    nodos.close()
    #añade aristas
    aristas = open(title + "E.txt" , "r")
    for li in aristas.readlines():
        sep = li.find("*")
        u = li[:sep]
        v = li[sep+1:-1]
        A.add_edge(u,v)
    aristas.close()
    aux_nodes = [x for x in A.nodes]
    for w in aux_nodes:
        if w in l:
            x = letter2number(w)
            print("\t" + str(x))
            A.add_node(x)
            for u in A.nodes():
                if (u, w) in A.edges() or (w, u) in A.edges():
                    A.add_edge(u, x)
            A.remove_node(w)

    guardarGrafo(A, title)

    return decrypt(title)
