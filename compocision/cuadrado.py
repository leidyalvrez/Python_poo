class cuadrado: 
    # Metodo constructor 
    def __init__(self, v1, v2, v3, v4):
        self.V1 = v1  
        self.V2 = v2
        self.V3 = v3
        self.V4 = v4
    
    def mostrarVertices(self):
        print("El cuadrado esta compuesto por los siguientes vertices")
        self.v1.mostrarCordenada()
        self.v2.mostrarCordenada()
        self.v3.mostrarCordenada()
        self.v4.mostrarCordenada()

def main():
    v1 = cordenada(1,1)
    v2 = cordenada(4,1)
    v3 = cordenada(4,4)
    v4 = cordenada(1,4)
    cuadrado = cuadrado(v1, v2, v3, v4) 
