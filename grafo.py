"""En este archivo va a estar la estructura de python que va a almacenar el grafo junto 
con sus funciones de control y creacion """
# es un grafo ponderado dirigido
# el grafo contiene la clave que es un nodo y su valor va a ser una lista de listas de dos
#  valores el primero es el nodo al cual se conecta y el otro es el peso de la arista que los conecta
#  ejemplo
#  k->[[E0,P0],[E1,P1]]
#  A->[[B,3],[C,9]]
grafo = {}


def insertarNodo(etiqueta: str):
    """#verificar si ya existe para poder introducirlo"""
    if etiqueta not in grafo:  # si el nodo existe(llave)
        grafo[etiqueta] = []


def insertarArista(nodoInicial: str, nodoFinal: str, peso):
    """#verificar si existe una arista entre esos nodos con el mismo peso"""
    # si es asi no se inserta esa arista

    if nodoInicial in grafo: #si existe el nodo inicial
        if nodoFinal in grafo: #si existe el nodo final
            if [nodoFinal, peso] not in grafo[nodoInicial]: #si ese camino (arista) no existe entonces se agrega de lo contrario
                grafo[nodoInicial].append([nodoFinal, peso])#agregale la lista
            else:
                print("ERROR: ya existe esa arista en el grafo")
        else:
            print("ERROR: No existe el nodo Final")
    else:
        print("ERROR: No existe el nodo Inicial")

def eliminarNodo(etiqueta: str):
    """#verificar si existe antes de intentar borrarlo"""
    if etiqueta in grafo:
        grafo.pop(etiqueta)#elimina el elemento en la parte de las claves


        #eliminar todas las incidencias en todos lo nodos
        for listaDeListas in grafo.values():#recorre las listas de listas nodo,peso de cada clave del diccionario
            for lista in listaDeListas:#recorre cada lista dentro de la lista de listas
                if etiqueta in lista[0]:#si encuentra la etiqueta en la parte de etiqueta de la lista eliminalo
                    listaDeListas.remove(lista)#elimina la lista que contiene la etiqueta del nodo
    else:
        print("ERROR: Esa etiqueta no existe")


def eliminarArista(nodoInicial: str, nodoFinal: str, peso):
    """#verificar si existe antes de intentar borrarla"""
    if (nodoInicial in grafo) and (nodoFinal in grafo):
        if [nodoFinal, peso] in grafo[nodoInicial]: #si encuentra la conexion al nodo final desde el inicial con el mismo peso
            (grafo[nodoInicial]).remove([nodoFinal, peso])
        else:
            print("ERROR:No existe esa arista")
    else:
        print("ERROR:Esa arista no existe porque los nodos indicados son incorrectos")


def modificarNodo(etiquetaActual: str, etiquetaNueva: str):
    """verificar si existe antes de intentar modificar"""

    if etiquetaActual in grafo:#si existe el nodo entonces se puede modificar
        if etiquetaNueva not in grafo:#si no existe la etiqueta nueva en el grafo entonces se puede modificar para evitar repeticion de nodos
            valorNodo= grafo.pop(etiquetaActual)#almacena el valor de la etiqueta a modificar y la borro
            grafo[etiquetaNueva]=valorNodo#inserta el nodo con la etiqueta nueva y el valor del antiguo nodo

            #modificar todas las referencias a este nodo en las listas de listas de cada nodo
            for listaDeListas in grafo.values():#recorre las listas de listas de cada nodo(clave)
                for lista in listaDeListas:#recorre las listas(arista) de cada lista de listas
                    if etiquetaActual in lista[0]:#si encuentra la referencia al nodo que se desea modificar se cambia
                        lista[0] = etiquetaNueva#se cambia la etiqueta de esa referencia
        else:
            print("ERROR:Ya existe ese nodo")
    else:
        print("ERROR: No exite ese nodo en el grafo")

def modificarArista(nodoInicial: str, nodoFinal: str, pesoActual, pesoNuevo):
    """#verificar su existencia antes de modificar la arista"""
    #lo que se modifica es el peso de la arista
    encontroArista=False
    if nodoInicial in grafo and not encontroArista:#verifica existencia del nodo inicial para saber si puede existir la arista
        if nodoFinal in grafo and not encontroArista:#verifica existencia del nodo final para saber si puede existir la arista
            for lista in grafo[nodoInicial] :#recorre cada lista(arista) de cada nodo
                if (nodoFinal in lista[0]) and  not encontroArista:#si encuentra el nodo final significa que el nodo inicial se conecta a el nodo final con direccion a este
                    if pesoActual == lista[1] and not encontroArista:#si encuentra el peso Actual indicado significa que es la arista correcta a modificar
                        lista[1] = pesoNuevo #cambia el peso actual al peso nuevo
                        encontroArista = True
                    else:
                        print(f"ERROR:No existe arista entre esos nodos con el peso {pesoActual}")
                else:#si no encuentra conexion significa que no existe arista entre esos nodos con direccion al nodo final
                    if not encontroArista:
                        print(f"ERROR:No existe arista de  {nodoInicial}->{nodoFinal}")
        else:
            print("ERROR:No existe arista con el nodo final indicado")
    else:
        print("ERROR:No existe arista con el nodo inicial indicado")


def importarGrafo(nombreArchivo: str) :
    """ Permite importar un grafo desde un txt """
    grafo={}
    with open(nombreArchivo, 'r', encoding='utf8') as archivo:
        for lineaTexto in archivo:
            linea = lineaTexto.strip().split(';')
            if linea[0] not in grafo:
                grafo[linea[0]] = []  # declaro el espacio de la comuna como un arreglo para almacenar listas en este
            if len(linea) > 1:#si hay aristas que salen de ese nodo
                for arista in linea[1:]:#recorre cada arista
                    grafo[linea[0]].append(arista.strip().split(','))#agregala al grafo al nodo que le corresponde

    return grafo


def exportarGrafo(nombreArchivo:str,grafo: dict):
    """ Permite exportar un grafo a un archivo txt """
    archivo =open(nombreArchivo,"w")
    for nodo, listaDeListas in grafo.items():
        linea=""
        linea = linea + str(nodo)
        if len(listaDeListas) > 1:#si hay mas de 1 elemento significa que el nodo clave se conecta a otros nodos
            for lista in listaDeListas:
                linea += ";"+str(lista)
                linea = linea.replace("[","").replace("]","").replace("'","").replace(" ","")
            linea += "\n"
        archivo.write(linea)
    archivo.close()

def recorrerProfundidad(grafo:dict) -> list:
    """ Recorre el grafo en profundidad """
    recorrido = []
    return recorrido


def recorrerAncho() -> list:
    """ Recorre el grafo a lo ancho """
    recorrido = []
    cola=[]
    ##TODO
    nodoInicial=0

    #se escoje el nodo inicial
    for nodo in grafo.keys():
        nodoInicial=nodo
        if not (nodoInicial == None):
            break


    cola.append(nodoInicial)#primero agregar el nodo a la cola
    #mientras la cola no este vacia
    while len(cola) > 0:
        primerNodoCola=cola.pop(0)
        if primerNodoCola not in recorrido:
            recorrido.append(primerNodoCola)#sacar el primer nodo de la cola y visitarlo
        vecinos_nodo=vecinosNodo(primerNodoCola)
        #agregar todos los vecinos no visitados a la cola
        for vecino in vecinos_nodo:#recorre los vecinos
            if vecino not in recorrido:#si el vecino no esta en el recorrido significa q no fue visitado
                 cola.append(vecino)


    return recorrido

def vecinosNodo(nodo:str)->list:
    """Funcion q devuelve los nodos vecinos de un nodo"""
    vecinos=[]
    if nodo in grafo:
        if len(grafo[nodo]) > 0:
            for arista in grafo[nodo]:#recorre las aristas de ese nodo
                nodoVecino=arista[0]
                if (nodoVecino not in vecinos) and  not (nodoVecino == nodo):#si no esta dentro de los vecinos y no es el propio nodo
                    vecinos.append(nodoVecino)#agrega la parte de la etiqueta a los vecinos
    else:
        print("ERROR:Ese nodo no esta en el grafo")
    return vecinos