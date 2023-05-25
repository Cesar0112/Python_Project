""" Aqui va la parte de visualizacion del grafo """
# ##TODO hacer la parte visual para esta parte se pueden usar modulos externos

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import tkinter as tk
import numpy as np
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

def eliminarNodo():

    etiqueta = nodo_entry.get()
    if etiqueta in graf:
        grafo.eliminarNodo(etiqueta)

        messagebox.showinfo("Exito","Nodo eliminado correctamente")
    else:
        messagebox.showerror("ERROR","No existe el nodo indicado")

def modificarNodo():
    etiquetaActual=nodo_entry.get()
    etiquetaNueva = nodo_nuevo_entry.get()
    if etiquetaActual in graf:#si existe el nodo entonces se puede modificar
        if etiquetaNueva not in graf:#si no existe la etiqueta nueva en el grafo entonces se puede modificar para evitar repeticion de nodos
            grafo.modificarNodo(etiquetaActual,etiquetaNueva)
            messagebox.showinfo("Exito","Nodo modificado")
        else:
            messagebox.showerror("ERROR","Ya existe ese nodo en el grafo")
    else:
        messagebox.showerror("ERROR","No existe el nodo a modificar, en el grafo")

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
        if len(aristas) > 0:
            for arista in aristas:
                if len(arista)>1:
                    G.add_edge(nodo, arista[0],weight=arista[1])

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

def eliminarArista():
    nodoInicial = nodo_ini_entry.get()
    nodoFinal = nodo_fin_entry.get()
    peso = grafo.getAristaPeso(nodoInicial, nodoFinal)
    if (nodoInicial in graf) and (nodoFinal in graf):
        if [nodoFinal, peso] in graf[nodoInicial]: #si encuentra la conexion al nodo final desde el inicial con el mismo peso
            grafo.eliminarArista(nodoInicial,nodoFinal,peso)
            messagebox.showinfo("Exito","Eliminación exitosa")
        else:
            messagebox.showerror("ERROR","No existe esa arista")
    else:
        messagebox.showerror("ERROR","No existe esa arista entre los nodos indicados")

def importarGrafo():
    nombreArchivo = filedialog.askopenfilename(initialdir="/",title="Seleccionar archivo",filetypes=(("Archivos de texto", "*.txt*"),("Todos los archivos", "*.*")))
    if nombreArchivo is not None and nombreArchivo != "":
        grafo.importarGrafo(nombreArchivo)
        messagebox.showinfo("Exito","Grafo importado correctamente")
def exportarGrafo():
    nombreArchivo = filedialog.asksaveasfilename(initialdir="/",
                                           defaultextension=".txt",
                                           filetypes=(("Archivos de texto", "*.txt*"),
                                                      ("Todos los archivos", "*.*")))
    if nombreArchivo is not None and nombreArchivo != "":
        grafo.exportarGrafo(nombreArchivo,graf)
        messagebox.showinfo("Exito","Grafo exportado correctamente")


def dibujarCirculos(nombres):
    ventana = tk.Tk()
    ventana.title("Recorrido a lo ancho")
    while("" in nombres):
        nombres.remove("")
    # Dimensiones del canvas
    width = 600
    height = 100

    canvas = tk.Canvas(ventana, width=width, height=height)
    canvas.pack()

    # Dibujo de los círculos
    radio = 30
    margen = 20
    distancia = (width - (2 * margen)) // len(nombres)
    for i, nombre in enumerate(nombres):
        x = margen + (i * distancia)
        y = height // 2
        canvas.create_oval(x - radio, y - radio, x + radio, y + radio, fill="lightblue")
        canvas.create_text(x, y, text=nombre)

    ventana.mainloop()


def recorrerAncho():
    dibujarCirculos(grafo.recorrerAncho())
def recorrerProfundidad():
    dibujarCirculos(grafo.recorrerProfundidad())


    """root = Tk()
root.title("Grafo Dirigido Ponderado")
root.geometry("400x400")

#boton importar grafo
importar_grafo_btn = Button(root,text="Importar Grafo",command=importarGrafo)
importar_grafo_btn.pack()

#boton exportar grafo
exportar_grafo_btn = Button(root,text="Exportar Grafo",command=exportarGrafo)
exportar_grafo_btn.pack()

# Etiqueta y entrada para insertar nodo
nodo_label = Label(root, text="Etiqueta del Nodo:")
nodo_label.pack()
nodo_entry = Entry(root)
nodo_entry.pack()

#boton insertar
insertar_nodo_btn = Button(root, text="Insertar Nodo", command=insertarNodo)
insertar_nodo_btn.pack()

eliminar_nodo_btn = Button(root, text = "Eliminar Nodo",command=eliminarNodo)
eliminar_nodo_btn.pack()
# Etiqueta y entrada para el nuevo nodo
nodo_label_nueva = Label(root, text="Etiqueta Nueva del Nodo:")
nodo_label_nueva.pack()
nodo_entry_nueva = Entry(root)
nodo_entry_nueva.pack()

#boton modificar creado e insertado
modificar_nodo_btn = Button(root,text="Modificar Nodo",command=modificarNodo)
modificar_nodo_btn.pack()

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

eliminar_arista_btn = Button(root,text="Eliminar Arista",command=eliminarArista)
eliminar_arista_btn.pack()


# Botón para visualizar el grafo
visualizar_btn = Button(root, text="Visualizar Grafo", command=visualizarGrafo)
visualizar_btn.pack()



root.mainloop()"""
root = tk.Tk()
root.title("Grafo Dirigido Ponderado")
root.geometry("600x500")

# Etiquetas y entradas para insertar nodo
nodo_label = tk.Label(root, text="Etiqueta del Nodo:")
nodo_label.grid(column=0, row=0, padx=10, pady=10)
nodo_entry = tk.Entry(root)
nodo_entry.grid(column=1, row=0, padx=10, pady=10)

#boton insertar
insertar_nodo_btn = tk.Button(root, text="Insertar Nodo", command=insertarNodo)
insertar_nodo_btn.grid(column=2, row=0, padx=10, pady=10)

eliminar_nodo_btn = tk.Button(root, text = "Eliminar Nodo",command=eliminarNodo)
eliminar_nodo_btn.grid(column=2, row=1, padx=10, pady=10)

# Etiquetas y entradas para modificar nodo
nodo_nuevo_label = tk.Label(root, text="Etiqueta Nueva del Nodo:")
nodo_nuevo_label.grid(column=0, row=2, padx=10, pady=10)
nodo_nuevo_entry = tk.Entry(root)
nodo_nuevo_entry.grid(column=1, row=2, padx=10, pady=10)

#boton modificar
modificar_nodo_btn = tk.Button(root,text="Modificar Nodo",command=modificarNodo)
modificar_nodo_btn.grid(column=2, row=2, padx=10, pady=10)

# Etiquetas y entradas para insertar arista
nodo_ini_label = tk.Label(root, text="Nodo Inicial:")
nodo_ini_label.grid(column=0, row=3, padx=10, pady=10)
nodo_ini_entry = tk.Entry(root)
nodo_ini_entry.grid(column=1, row=3, padx=10, pady=10)

nodo_fin_label = tk.Label(root, text="Nodo Final:")
nodo_fin_label.grid(column=0, row=4, padx=10, pady=10)
nodo_fin_entry = tk.Entry(root)
nodo_fin_entry.grid(column=1, row=4, padx=10, pady=10)

peso_label = tk.Label(root, text="Peso:")
peso_label.grid(column=0, row=5, padx=10, pady=10)
peso_entry = tk.Entry(root)
peso_entry.grid(column=1, row=5, padx=10, pady=10)

#boton insertar arista
insertar_arista_btn = tk.Button(root, text="Insertar Arista", command=insertarArista)
insertar_arista_btn.grid(column=2, row=4, padx=10, pady=10)

eliminar_arista_btn = tk.Button(root,text="Eliminar Arista",command=eliminarArista)
eliminar_arista_btn.grid(column=2, row=6, padx=10, pady=10)

modificar_arista_btn = tk.Button(root, text="Modificar Arista",command=modificarArista)
modificar_arista_btn.grid(column=2, row=5, padx=10, pady=10)

#boton importar grafo
importar_grafo_btn = tk.Button(root,text="Importar Grafo",command=importarGrafo)
importar_grafo_btn.grid(column=0, row=8, pady=10)

#boton exportar grafo
exportar_grafo_btn = tk.Button(root,text="Exportar Grafo",command=exportarGrafo)
exportar_grafo_btn.grid(column=1, row=8, padx=10, pady=10)

# Botón para visualizar el grafo
visualizar_btn = tk.Button(root, text="Visualizar Grafo", command=visualizarGrafo)
visualizar_btn.grid(column=0, row=9, pady=10, columnspan=3)

recorrer_ancho_btn = tk.Button(root, text="Recorrer a lo ancho",command=recorrerAncho)
recorrer_ancho_btn.grid(column=2,row=9,pady=20,columnspan=3)

recorrer_profundidad_btn = tk.Button(root, text="Recorrer en profundidad",command=recorrerProfundidad)
recorrer_profundidad_btn.grid(column=2,row=10,pady=20,columnspan=3)

root.mainloop()