"""En este archivo va a estar la estructura de python que va a almacenar el grafo junto 
con sus funciones de control y creacion """
# es un grafo ponderado dirigido
# el grafo contiene la clave que es un nodo y su valor va a ser una lista de listas de dos
#  valores el primero es el nodo al cual se conecta y el otro es el peso de la arista que los conecta
#  ejemplo
#  k->[[E0,P0],[E1,P1]]
#  A->[[B,3],[C,9]]
grafo = {}


def insertarNodo(etiqueta: str) -> str:
    """#verificar si ya existe para poder introducirlo"""
    if etiqueta not in grafo:  # si el nodo existe(llave)
        grafo[etiqueta] = []
        return "Exito","Nodo insertado con exito" #insertado con exito
    else:
        return "ERROR","Ese nodo ya existe en el grafo" #no insertado con exito

def insertarArista(nodoInicial: str, nodoFinal: str, peso) -> str:
    """#verificar si existe una arista entre esos nodos con el mismo peso
    si devuelve:
    """
    # si es asi no se inserta esa arista

    if nodoInicial in grafo: #si existe el nodo inicial
        if nodoFinal in grafo: #si existe el nodo final
            if [nodoFinal, peso] not in grafo[nodoInicial]: #si ese camino (arista) no existe entonces se agrega de lo contrario
                grafo[nodoInicial].append([nodoFinal, peso])#agregale a la lista
                return "Arista insertada correctamente"
            else:
                return "ERROR: Ya existe una arista entre esos nodos con ese peso"
        else:
            return "ERROR: No existe el nodo final"
    else:
        return "ERROR: No existe el nodo inicial"

def eliminarNodo(etiqueta: str) -> str:
    """#verificar si existe antes de intentar borrarlo
    retorna el nodo eliminado
    """
    if etiqueta in grafo:
        nodoEliminado = grafo.pop(etiqueta)#elimina el elemento en la parte de las claves


        #eliminar todas las incidencias en todos lo nodos
        for listaDeListas in grafo.values():#recorre las listas de listas nodo,peso de cada clave del diccionario
            for lista in listaDeListas:#recorre cada lista dentro de la lista de listas
                if etiqueta in lista[0]:#si encuentra la etiqueta en la parte de etiqueta de la lista eliminalo
                    listaDeListas.remove(lista)#elimina la lista que contiene la etiqueta del nodo

        return "Nodo eliminado correctamente"
    else:
        return "ERROR: No existe el nodo indicado"



def eliminarArista(nodoInicial: str, nodoFinal: str, peso) -> str:
    """#verificar si existe antes de intentar borrarla
    """
    if (nodoInicial in grafo) and (nodoFinal in grafo):
        if [nodoFinal, peso] in grafo[nodoInicial]: #si encuentra la conexion al nodo final desde el inicial con el mismo peso
            (grafo[nodoInicial]).remove([nodoFinal, peso])
            return "Eliminación exitosa"
        else:
            return "ERROR: No existe esa arista"
    else:
        return "ERROR: No existe esa arista entre los nodos indicados"


def modificarNodo(etiquetaActual: str, etiquetaNueva: str) -> str:
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
            return "Nodo modificado"
        else:
            return "ERROR:Ya existe ese nodo en el grafo"
    else:
        return "ERROR: No existe el nodo a modificar, en el grafo"

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
                        return f"ERROR:No existe arista entre esos nodos con el peso {pesoActual}"
                else:#si no encuentra conexion significa que no existe arista entre esos nodos con direccion al nodo final
                    if not encontroArista:
                        return f"ERROR:No existe arista de  {nodoInicial}->{nodoFinal}"
        else:
            return "ERROR:No existe arista con el nodo final indicado"
    else:
        return "ERROR:No existe arista con el nodo inicial indicado"


def importarGrafo(nombreArchivo: str) -> str:
    """ Permite importar un grafo desde un txt """

    with open(nombreArchivo, 'r', encoding='utf8') as archivo:
        for lineaTexto in archivo:
            linea = lineaTexto.strip().split(';')#divido la linea leida en un arreglo dividido por punto y comas
            if linea[0] not in grafo:#verificar que el nodo  no este en el grafo
                grafo[linea[0]] = []  # declaro el espacio del nodo como una lista para almacenar listas de solo dos elementos en este
            if len(linea) > 1:#si hay aristas que salen de ese nodo hacia otro aunque sea a el
                for arista in linea[1:]:#recorre cada arista
                    grafo[linea[0]].append(arista.strip().split(','))#agregala al grafo al nodo que le corresponde

    return "Grafo importado correctamente"


def exportarGrafo(nombreArchivo:str,grafo: dict) -> str :
    """ Permite exportar un grafo a un archivo txt """
    archivo =open(nombreArchivo,"w")
    for nodo, listaDeListas in grafo.items():
        linea=""
        linea = linea + str(nodo)
        if len(listaDeListas) > 1:#si hay mas de 1 elemento significa que el nodo clave se conecta a otros nodos
            for lista in listaDeListas:
                linea += ";"+str(lista)
                #remplazar todos los caracteres que no sea comas ni punto y comas con caracter vacio
                linea = linea.replace("[","").replace("]","").replace("'","").replace(" ","")
            linea += "\n"
        archivo.write(linea)
    archivo.close()
    return "Grafo exportado correctamente"

def recorrerProfundidad() -> list:
    """ Recorre el grafo a lo profundo """
    recorrido = []
    pila=[]
    nodoInicial=0

    #se escoje el nodo inicial
    for nodo in grafo.keys():
        nodoInicial=nodo
        if not (nodoInicial == None):
            break


    pila.append(nodoInicial)#primero agregar el nodo a la pila
    #mientras la pila no este vacia
    while len(pila) > 0:
        ultimoNodoPila=pila.pop()
        if ultimoNodoPila not in recorrido:
            recorrido.append(ultimoNodoPila)#sacar el ultimo nodo de la pila y visitarlo
        vecinos_nodo=vecinosNodo(ultimoNodoPila)
        #agregar todos los vecinos no visitados a la pila
        for vecino in vecinos_nodo:#recorre los vecinos
            if vecino not in recorrido:#si el vecino no esta en el recorrido significa q no fue visitado
                 pila.append(vecino)


    return recorrido


def recorrerAncho() -> list:
    """ Recorre el grafo a lo ancho """
    recorrido = []
    cola=[]
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

def getAristaPeso(nodoInicial:str, nodoFinal:str):
    if nodoInicial in grafo and nodoFinal in grafo:
        for arista in grafo[nodoInicial]:
            if arista[0] == nodoFinal:#si existe la conexion
                return arista[1]