""" Aqui va la parte de visualizacion del grafo """
# ##TODO hacer la parte visual para esta parte se pueden usar modulos externos

from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
import networkx as nx


grafo = {}


def insertarNodo():
    etiqueta = nodo_entry.get()
    if etiqueta:
        if etiqueta not in grafo:
            grafo[etiqueta] = []
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
        if nodoInicial in grafo and nodoFinal in grafo:
            arista = [nodoFinal, peso]
            if arista not in grafo[nodoInicial]:
                grafo[nodoInicial].append(arista)
                messagebox.showinfo("Éxito", "Arista insertada correctamente.")
            else:
                messagebox.showerror("Error", "La arista ya existe en el grafo.")
        else:
            messagebox.showerror("Error", "Los nodos ingresados no existen en el grafo.")
    else:
        messagebox.showerror("Error", "Ingrese los valores para los nodos y el peso.")


def visualizarGrafo():
    G = nx.DiGraph()
    for nodo, aristas in grafo.items():
        G.add_node(nodo)
        for arista in aristas:
            G.add_edge(nodo, arista[0], weight=arista[1])

    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()


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

# Botón para visualizar el grafo
visualizar_btn = Button(root, text="Visualizar Grafo", command=visualizarGrafo)
visualizar_btn.pack()

root.mainloop()
