#Vertice = no
class Vertice():
    def __init__(self, id):
        self.id = id
        self.estimativa = 999999
        self.input = 0
        self.output = 0
        self.visitado = False
        self.predecessor = []
    
    # quando imprimir a classe, vai sair dessa forma
    def __str__(self):
        return (" Vertice  : %s \n Estimativa: %i \n Tempo(%i\%i): " % (
                                                                        self.id, self.estimativa, self.input, self.output))  # imprimir o predecesso
    # sobrecarga do operador less than
    def __lt__(self, v):
        return self.estimativa < v.estimativa
    
    # sobrecarga do operador equal
    def __eq__(self, v):
        return self.estimativa == v.estimativa
    
    def __eq__(self, v):
        return self.id == v.id
    
    # sobrecarga do operador greater than
    def __gt__(self, v):
        return self.estimativa > v.estimativa

