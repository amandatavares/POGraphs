#Aresta = arco
class Aresta():
    def __init__(self,origem,destino,peso = 0):
        self.origem = origem
        self.destino = destino
        self.peso = peso
    
    def __str__(self):
        return "A(%s----%i---->%s)" % (self.origem,self.peso,self.destino)
