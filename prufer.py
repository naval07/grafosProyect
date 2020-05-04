import networkx as nx #Librería usada para generar el grafo.
import matplotlib.pyplot as plt #Librería usada para mostrar el grafo generado.
import cifradoVigenere as cv #Modulo del cifrado de Vigenere
import cifradoCesar as cc #Modulo del cifrado de César


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

#----------Cifrado de Mensajes a Grafos-----------------

def Reconstruccion_de_T(msg):
    """Algoritmo que toma un mensaje como código de Prüfer y una constraseña de cifrado
    para crear una codificacion del mensaje, un árbol T"""

    assert(len(msg) <= 280), u"Mensaje muy largo. Máximo 280 caracteres"
    # cifra la contraseña mediante el cif. de Cesar con su long.
    pas = input("Ingrese la contraseña: ")
    assert(len(pas) >0), u"No ingresó contraseña"
    pasCes = cc.code(pas, len(pas))
    # cifrra el mensaje mediante el cif. de Vigenere
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
    nx.draw(G, with_labels = True)
    #plt.savefig("prueba.PNG")
    plt.show()

def Reconstruccion_de_T_anagrama(msg):
    """Similar al anterior, pero distribuye los nodos de tal forma que
    al escribir el código se retorne en forma de anagrama"""

    assert(len(msg) <= 280), u"Mensaje muy largo. Máximo 280 caracteres"
    # cifra la contraseña mediante el cif. de Cesar con su long.
    pas = input("Ingrese la contraseña: ")
    assert(len(pas) >0), u"No ingresó contraseña"
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
    nx.draw(G, with_labels = True)
    plt.show()

def R_de_T_Secret(msg):
    """Algoritmo que toma un mensaje como código de Prüfer y lo transforma
    en un árbol T sin indicar que hoja es el mínimo (usando la definición
    cambio())"""

    assert(len(msg) <= 280), u"Mensaje muy largo. Máximo 280 caracteres"
    # cifra la contraseña mediante el cif. de Cesar con su long.
    pas = input("Ingrese la contraseña: ")
    assert(len(pas) >0), u"No ingresó contraseña"
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

    nx.draw(G, with_labels = True, node_size = 350)
    plt.show()

#---------Descifrado de Grafos a mensajes--------------

def codigo_prufer(A):
    """Toma un árbol y retorna el mensaje en código de Prüfer"""
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

    return prufer

def codigo_prufer_Secret(A):
    """Toma un árbol sin nodos numéricos y lo transforma a código de Prüfer"""
    for v in A.nodes():
        if v in l:
            x = letter2number(v)
            A.add_node(x)
            for u in A.nodes():
                if (u, v) in A.edges() or (v, u) in A.edges():
                    A.add_edge(u, x)
            A.remove_node(v)
    return codigo_prufer(A)