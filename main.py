from grafo import *
from busca_largura import *

def main():
    grafo = Grafo()
    #Exemplo componente fortemente conexo
    grafo.novo_Vertice(0)
    grafo.novo_Vertice(1)
    grafo.novo_Vertice(2)
    grafo.novo_Vertice(3)
    grafo.nova_Aresta(0,1,0)
    grafo.nova_Aresta(0,3,0)
    grafo.nova_Aresta(1,2,0)
    grafo.nova_Aresta(2,0,0)
    grafo.nova_Aresta(2,3,0)
    largura, pai, aresta, nivel = busca_em_largura(grafo, 3)
    print("Localizado na largura %s, pai %s, aresta %s, nivel %") % (largura, pai, aresta, nivel)
#    grafo.imprime_Grafo(0,1)

main()
