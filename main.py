# -*- coding: utf-8 -*-

from grafo import *
from busca_largura import *

def main():
    grafo = Grafo()
    print("Grafo demais App")
    print("1 - Criar vértice")
    print("2 - Criar aresta")
    print("3 - Imprimir grafo")
    print("4 - Sair")

    while(True):
        opt = input(str("Opção: "))
        if opt == 1:
            #Exemplo componente fortemente conexo
            nome_Vertice = input(str("Identificador do Vertice: "))
            grafo.novo_Vertice(nome_Vertice)
        elif opt == 2:
            origem = input(str("Origem: "))
            destino = input(str("Destino: "))
            peso = input(str("Peso: "))
            grafo.nova_Aresta(origem, destino, peso)
        elif opt == 3:
            origem = input(str("Origem: "))
            destino = input(str("Destino: "))
            grafo.imprime_Grafo(origem,destino)
        elif opt == 4:
            break
        else:
            print("Selecione uma opção válida")

main()
