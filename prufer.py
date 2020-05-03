import networkx as nx #Librería usada para generar el grafo.
import matplotlib.pyplot as plt #Librería usada para mostrar el grafo generado.
import cifradoVigenere as cif

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
    #index = [chr(x) for x in range(200,300)]
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
    aux = []
    while min(nodos) in msg:
        aux.append(min(nodos))
        nodos.remove(min(nodos))
    x = min(nodos)
    nodos.remove(x)
    nodos += aux
    return x

def cifrado_cesar(msg, mov):
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

def decifrado_cesar(msg, mov):
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

def cambio(nodo_num):
    """si el nodo está marcado con unvalor numérico se cambian estos por
    caracteres ajenos al mensaje para generar más privacidad"""
    l = [chr(x) for x in range(256, 537)]
    i = 0
    dic = {}
    for q in range(len(l)):
        dic[str(i)] = l[q]
        i += 1
    return dic[nodo_num]

def Reconstruccion_de_T(msg):
    """Algoritmo que toma un mensaje como código de Prüfer y lo transforma
    en un árbol T"""
    nodos = complete_nodes(msg)
    G = nx.Graph()
    G.add_nodes_from(nodos)
    while len(nodos) != 2 and len(msg) > 0:
        a = msg[0]
        if min(nodos) not in msg:
            x = min(nodos)
            G.add_edge(x, a)
            nodos.remove(x)
        else:
            x = next_min(nodos, msg)
            G.add_edge(x, a)
        msg = msg[1:]

    G.add_edge(nodos[0], nodos[1])
    nx.draw(G, with_labels = True)
    plt.show()

def Reconstruccion_de_T_anagrama(msg):
    """Similar al anterior, pero distribuye los nodos de tal forma que
    al escribir el código se retorne en forma de anagrama"""
    nodos = complete_nodes_anagrama(msg)
    G = nx.Graph()
    G.add_nodes_from(nodos)
    while len(nodos) != 2 and len(msg) > 0:
        a = msg[0]
        if min(nodos) not in msg:
            x = min(nodos)
            G.add_edge(x, a)
            nodos.remove(x)
        else:
            x = next_min(nodos, msg)
            G.add_edge(x, a)
        msg = msg[1:]

    G.add_edge(nodos[0], nodos[1])
    nx.draw(G, with_labels = True)
    plt.show()

def R_de_T_Secret(msg):
    """Algoritmo que toma un mensaje como código de Prüfer y lo transforma
    en un árbol T sin indicar que hoja es el mínimo (usando la definición
    cambio())"""
    list_num = []
    for h in range(280):
        list_num.append(str(h))

    new_nodos = []
    nodos = complete_nodes(msg)
    G = nx.Graph()
    G.add_nodes_from(nodos)
    while len(nodos) != 2 and len(msg) > 0:
        a = msg[0]
        if min(nodos) not in msg:
            x = min(nodos)
            if x in list_num:
                G.add_edge(cambio(x), a)
            else:
                G.add_edge(x, a)
            nodos.remove(x)
        else:
            x = next_min(nodos, msg)
            if x in list_num:
                G.add_edge(cambio(x), a)
            else:
                G.add_edge(x, a)
        new_nodos.append(x)
        msg = msg[1:]

    for v in new_nodos:
        if v in list_num:
            G.remove_node(v)

    G.add_edge(nodos[0], nodos[1])
    nx.draw(G, with_labels = True)
    #plt.savefig("prueba.PNG")
    plt.show()

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
