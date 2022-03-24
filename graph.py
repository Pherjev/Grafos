# -*- coding: utf-8 -*-

import math
import random
import numpy as np
import graphviz
from PIL import Image
#from colormap import rgb2hex

from edge import Edge
from node import Node


class Graph:
        """
        Clase grafo: Referente al grafo
        """
        def __init__(self,digraph=False,eng = 'fdp'):

                """
                Inicializa un grafo vacío.
                """

                self.id = 'graph'
                self.nodes = dict()
                self.edges = dict()
                self.digraph = digraph
                if digraph:
                        self.display = graphviz.Digraph(format='png',engine=eng)
                else:
                        self.display = graphviz.Graph(format='png',engine = eng)

        def addNode(self, name,pos='0'):
                """
                Agrega un nodo al grafo con el id name.
                pos: posición del nodo
                """
                if name not in self.nodes.keys():
                        node = Node(name)
                        #colour = rgb2hex(random.randint(0,255),random.randint(0,255),random.randint(0,255))
                        colour = 'red'
                        self.nodes[name] = node
                        if pos == '0':
                                self.display.node(name,shape='point',color=colour)
                        else:
                                self.display.node(name,shape='point',color=colour,pos=pos)
                #return self.getNode(name)

        def addEdge(self, name, node0, node1):
                """
                Agrega una arista con nodos node0 y node1 como ids. 
                Crea los nodos si no existen.
                """
                if name not in self.edges.keys():
                        self.addNode(node0)
                        self.addNode(node1)
                        n0 = self.getNode(node0)
                        n1 = self.getNode(node1)
                        e = Edge(n0,n1,name)
                        self.edges[name] = e
                        self.display.edge(node0,node1,color='gray')
                        n0.degree += 1
                        n1.degree += 1
                #return e

        def getNode(self,name):
                """
                Invoca al nodo con el id name.
                """
                return self.nodes.get(name)

        def getEdge(self,name):
                """
                Invoca a la arista con el id name.
                """
                return self.edges.get(name)

        def show(self):
                """
                Guarda al nodo en el archivo graph.gv para leer en Gephi.
                Guarda una imagen del nodo con el archivo graph.png
                Muestra la imagen.
                """
                self.display.render(filename='graph.gv',view=True)
                im = Image.open('graph.gv.png') #cv2.imread('graph.png')
                im.show()
                #cv2.imshow('img',img) # MODIFICAR 
                #cv2.waitKey()

g = Graph()
g.addNode('3')
g.addEdge('12','1','2')
g.addEdge('31','3','1')
g.show()
