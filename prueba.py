from grafo import grafo, insertarNodo, insertarArista\
    ,eliminarNodo,eliminarArista,modificarNodo\
    ,modificarArista,importarGrafo,exportarGrafo\
    ,vecinosNodo,recorrerAncho,recorrerProfundidad

A='A'
B='B'
C='C'
D='D'
E='E'
F='F'
insertarNodo(A)
insertarNodo(B)
insertarNodo(C)
insertarNodo(D)
insertarNodo(E)
insertarNodo(F)
insertarArista(A, B, 3)
insertarArista(A, C, 3)
insertarArista(B,C,4)
insertarArista(B,A,2)
insertarArista(C,B,4)
insertarArista(B,A,7)
insertarArista(A,A,2)#ciclo lazo
insertarArista(C,E,2)
insertarArista(C,F,1)
for k, v in grafo.items():
    print(f"{k},->{v}")

"""eliminarNodo(B)
eliminarArista(A,C,3)"""

"""modificarNodo(C,D)"""

"""modificarArista(B,A,2,5)"""
"""grafo = importarGrafo("grafo")"""
"""print("------------------------------")
for k, v in grafo.items():
    print(f"{k},->{v}")"""
"""exportarGrafo("grafoNuevo",grafo)"""

"""print(vecinosNodo("B"))"""
print(recorrerAncho())
print(recorrerProfundidad())
