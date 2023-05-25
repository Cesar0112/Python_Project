""" Aqui va la parte de visualizacion del grafo """
# ##TODO hacer la parte visual para esta parte se pueden usar modulos externos

from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
import networkx as nx
from grafo import grafo as graf
import grafo
def insertarNodo():
    etiqueta = nodo_entry.get()
    if etiqueta:
        if etiqueta not in graf:
            grafo.insertarNodo(etiqueta)
            messagebox.showinfo("Éxito", "Nodo insertado correctamente.")
        else:
            messagebox.showerror("Error", "El nodo ya existe en el grafo.")
    else:
        messagebox.showerror("Error", "Ingrese una etiqueta para el nodo.")


def insertarArista():
    nodoInicial = nodo_ini_entry.get()
    nodoFinal = nodo_fin_entry.get()
    peso = peso_entry.get()
    if nodoInicial and nodoFinal and peso:
        if nodoInicial in graf and nodoFinal in graf:
            arista = [nodoFinal, peso]
            if arista not in graf[nodoInicial]:
                grafo.insertarArista(nodoInicial,nodoFinal,peso)
                messagebox.showinfo("Éxito", "Arista insertada correctamente.")
            else:
                messagebox.showerror("Error", "La arista ya existe en el grafo.")
        else:
            messagebox.showerror("Error", "Los nodos ingresados no existen en el grafo.")
    else:
        messagebox.showerror("Error", "Ingrese los valores para los nodos y el peso.")


def visualizarGrafo():
    G = nx.DiGraph()
    for nodo, aristas in graf.items():
        G.add_node(nodo)
        #recorre cada nodo al que apunta en cada aristay le apunta
        for arista in aristas:
            G.add_edge(nodo, arista[0], weight=arista[1])

    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

def modificarArista():

    encontroArista = False
    nodoInicial=nodo_ini_entry.get()
    nodoFinal=nodo_fin_entry.get()

    pesoNuevo = peso_entry.get()
    if nodoInicial in graf and not encontroArista:  # verifica existencia del nodo inicial para saber si puede existir la arista
        if nodoFinal in graf and not encontroArista:  # verifica existencia del nodo final para saber si puede existir la arista
            for arista in graf[nodoInicial]:  # recorre cada lista(arista) de cada nodo
                if (nodoFinal in arista[0]) and not encontroArista:  # si encuentra el nodo final significa que el nodo inicial se conecta a el nodo final con direccion a este
                    pesoActual=grafo.getAristaPeso(nodoInicial,nodoFinal)#si ya verifico la conexion no da error
                    if pesoActual == arista[1] and not encontroArista:  # si encuentra el peso Actual indicado significa que es la arista correcta a modificar
                        grafo.modificarArista(nodoInicial,nodoFinal,pesoActual,pesoNuevo)  # cambia el peso actual al peso nuevo
                        messagebox.showinfo("Éxito", "Arista modificada correctamente.")
                        encontroArista = True
                    else:
                        messagebox.showerror("ERROR", f"No existe arista entre esos nodos con el peso {pesoActual}")
                else:  # si no encuentra conexion significa que no existe arista entre esos nodos con direccion al nodo final
                    if not encontroArista:
                        messagebox.showerror("ERROR",f"No existe arista de  {nodoInicial}->{nodoFinal}")
        else:
            messagebox.showerror("ERROR","No existe arista con el nodo final indicado")
    else:
        messagebox.showerror("ERROR", "No existe arista con el nodo inicial indicado")


root = Tk()
root.title("Grafo Dirigido Ponderado")
root.geometry("400x300")

# Etiqueta y entrada para insertar nodo
nodo_label = Label(root, text="Etiqueta del Nodo:")
nodo_label.pack()
nodo_entry = Entry(root)
nodo_entry.pack()

insertar_nodo_btn = Button(root, text="Insertar Nodo", command=insertarNodo)
insertar_nodo_btn.pack()

# Etiquetas y entradas para insertar arista
nodo_ini_label = Label(root, text="Nodo Inicial:")
nodo_ini_label.pack()
nodo_ini_entry = Entry(root)
nodo_ini_entry.pack()

nodo_fin_label = Label(root, text="Nodo Final:")
nodo_fin_label.pack()
nodo_fin_entry = Entry(root)
nodo_fin_entry.pack()

peso_label = Label(root, text="Peso:")
peso_label.pack()
peso_entry = Entry(root)
peso_entry.pack()

insertar_arista_btn = Button(root, text="Insertar Arista", command=insertarArista)
insertar_arista_btn.pack()

modificar_arista_btn = Button(root, text="Modificar Arista",command=modificarArista)
modificar_arista_btn.pack()

# Botón para visualizar el grafo
visualizar_btn = Button(root, text="Visualizar Grafo", command=visualizarGrafo)
visualizar_btn.pack()



root.mainloop()