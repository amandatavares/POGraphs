# -*- coding: utf-8 -*-
from vertice import *
from aresta import *

# Grafo
class Grafo:
    def __init__(self, direcionado=True):
        self.lista_Vertices = []
        self.lista_Arestas = []
        self.direcionado = direcionado
        self.tempo = 0
    
    def novo_Vertice(self, identificador):
#        string = input(str("Identificador do Vertice: "))
        self.lista_Vertices.append(Vertice(identificador))

    def busca_Aresta(self, u, v):  # Método recebe dois objetos do tipo Vértice
        for w in self.lista_Arestas:
            origem = w.getOrigem()
            destino = w.getDestino()
            if origem.getId() == u.getId() and destino.getId() == v.getId():
                return w

    def busca_Vertice(self, identificador):  # Método recebe um int
        for i in self.lista_Vertices:
            if identificador == i.id:
                return i
        else:
            return None

    def nova_Aresta(self, origem, destino, peso):  # Método recebe dois identificadores
        origem_aux = self.busca_Vertice(origem)
        destino_aux = self.busca_Vertice(destino)
        if (origem_aux is not None) and (destino_aux is not None):
            self.lista_Arestas.append(Aresta(origem_aux, destino_aux, peso))
        else:
            print("Um do Vertice ou ambos são invalidos")
        
        if self.direcionado == False:
            self.lista_Arestas.append(Aresta(destino_aux, origem_aux, peso))  # Aresta(u,v) e Aresta(v,u)

    def esta_Vazio(self):
        if len(self.lista_Vertices) == 0:
            return True
        else:
            return False

    def busca_Adjacente(self, u):  # Método recebe um vertice
        for i in range(len(self.lista_Arestas)):
            origem = self.lista_Arestas[i].getOrigem()
            destino = self.lista_Arestas[i].getDestino()
            if (u.getId() == origem.getId()) and (destino.getVisitado() == False):
                destino.setVisitado(True)  # Para que não retorn o mesmo vertice seguidas veses
                return destino
        else:
            return None

    ####################################################################

    def imprime_Grafo_com_Destino(self, origem, destino):
        destino_Aux = self.busca_Vertice(destino)
        if len(destino_Aux.predecessor) == 0:
            print("Não ha caminho")
        else:
            print(destino)
            self.imprime_Grafo(origem, destino)

    def imprime_Grafo(self, origem, destino):
        if origem == destino:
            print("Fim")
        else:
            destino_Aux = self.busca_Vertice(destino)
            if len(destino_Aux.predecessor) == 0:
                print("Não ha caminho")
            else:
                print(destino_Aux.predecessor[0])
                self.imprime_Grafo(origem, destino_Aux.predecessor[0])


    def grau(self, u):
        grau = 0
        for w in self.lista_Arestas:
            if u == w.getOrigem():
                grau += 1
        return grau

    ####################################################################
    def eh_Ponto(self, u):
        for v in self.lista_Vertices:
            v.setVisitado(False)

            u.setVisitado(True)
            self.visita(self.busca_Adjacente(u))
            for v in self.lista_Vertices:
                if v.getVisitado() == False:
                    return True

    def Articulation(self):
        art = []
        for u in self.lista_Vertices:
            if self.eh_Ponto(u):
                art.append(u.getId())
        print("Pontos de Articulação", art)

    ####################################################################
#    def busca_em_largura(self, vertice_do_grafo):
#        fila = [] # fila da busca, afinal ela eh em largura! .append(elemento) -> adiciona elemento na fila ; .pop(0) -> proximo na fila
#        # como os graus de entrada e saida de cada vertice sao iguais em uma busca em largura, chamamos ambos os valores de largura do vertice
#        largura = {}
#        l = 1 # contador de largura dos vertices na busca
#        pai = {} # dicionario com os pais de cada vertice na arvore de busca em largura
#        nivel = {} # nivel de cada vertice na arvore de busca em largura
#        aresta = {} # classificacao das arestas na arvore de busca em largura do grafo
#        
#        # primeira insercao na fila eh o vertice do grafo escolhido arbitrariamente (passado como parametro dessa funcao)
#        fila.append(vertice_do_grafo)
#        largura[vertice_do_grafo] = l # a largura da raiz da arvore de busca em largura comeca por 1
#        pai[vertice_do_grafo] = None # o primeiro vertice a entrar na fila (raiz da arvore de busca em largura) tem pai nulo (None object)
#        nivel[vertice_do_grafo] = 1 # o nivel do primeiro vertice a entrar na fila a (raiz da arvore de busca em largura) eh 1
#        
#        # enquanto tivermos alguem na fila vamos continuar a busca. Grafos nao-conexos nao estao sendo tratados!
#        while len(fila):
#            vertice = fila.pop(0) # pega o proximo vertice da fila
#            # colocando os vizinhos que ainda naum estavam na fila
#            for vizinho in grafo.get(vertice):
#                # testando se o vizinho jah foi visitado (se o get retornar None, significa que este vertice nunca entrou na fila)
#                if not largura.get(vizinho): # se o vizinho ainda naum foi visitado...
#                    fila.append(vizinho) # ... colocamos na fila para visita-lo no seu devido momento
#                    l += 1 # atualizando o contador de largura
#                    largura[vizinho] = l
#                    pai[vizinho] = vertice
#                    nivel[vizinho] = nivel[vertice] + 1 # um vizinho estah sempre um nivel abaixo do pai
#                # MOMENTO PARA VISITAR A ARESTA vertice -> vizinho
#                # (descomente os codigos abaixo para ver a ordem em que as arestas sao visitadas e suas respectivas classificacoes)
#                # print('%s -> %s:' % (str(vertice), str(vizinho)))
#                if pai[vizinho] == vertice or pai[vertice] == vizinho:
#                    aresta[(vertice, vizinho)] = 'aresta de arvore'
#                # print('aresta de arvore')
#                elif nivel[vertice] == nivel[vizinho]:
#                    if pai[vertice] == pai[vizinho]:
#                        aresta[(vertice, vizinho)] = 'aresta irma'
#                    # print('aresta irma')
#                    else:
#                        aresta[(vertice, vizinho)] = 'aresta primo'
#                # print('aresta primo')
#                else:
#                    if nivel[vertice] < nivel[vizinho]:
#                        aresta[(vertice, vizinho)] = 'aresta tia'
#                    # print('aresta tia')
#                    else:
#                        aresta[(vertice, vizinho)] = 'aresta sobrinha'
#        # print('aresta sobrinha')
#        #largura, pai, aresta, nivel = busca_em_largura(grafo, 'a')
#        return largura, pai, aresta, nivel
#
#
