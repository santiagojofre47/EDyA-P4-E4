import string
from claseNodo import Nodo

class ArbolHuffman:
    __raiz = None

    def __init__(self):
        archivo = open('C:/Users/Santiago/Documents/facultad/proyectos/Estructuras de Datos y Algoritmos/Practico 4/Ejercicio 4/texto.txt')
        texto = ''
        lista_nodos = []
        for lineas in archivo:
            texto += lineas
        archivo.close()
        texto = texto.translate({ord(c): None for c in string.whitespace}).lower()
        for i in range(len(texto)):
            if texto[i] not in lista_nodos:
                nodo = Nodo(texto[i],texto.count(texto[i]))
                lista_nodos.append(nodo)
        lista_nodos.sort()
        while len(lista_nodos) >= 2:
            nodo = Nodo(lista_nodos[0].getClave()+lista_nodos[1].getClave(),lista_nodos[0].getFrecuencia()+lista_nodos[1].getFrecuencia())
            nodo.setSigIzquierdo(lista_nodos[0])
            nodo.setSigDerecho(lista_nodos[1])
            lista_nodos.pop(0)
            lista_nodos.pop(0)
            lista_nodos.append(nodo)
        self.__raiz = lista_nodos[0]
    
    def getRaiz(self):
        return self.__raiz
    

    def preOrder(self,SubArbol):
        if not SubArbol == None:
            print(SubArbol)
            self.preOrder(SubArbol.getSigIzquierdo())
            self.preOrder(SubArbol.getSigDerecho())
        

  




