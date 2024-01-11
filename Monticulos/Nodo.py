class Nodo:

    def __init__(self, valor):

        self.valor = valor           # Almacena el valor del nodo
        self.hijo_izquierda = None   # Inicialmente no tiene hijo izquierdo
        self.hijo_derecha = None     # Inicialmente no tiene hijo derecho

    
    def __str__(self):

        return self.valor.__str__()