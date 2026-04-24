class cordenada: 
    # Metodo constructor 
    def__init__(self, x, y):
    self.x = x 
    self.y = y 
    # Metodo de accseso 
    def getX(self):
        return self.__x
    
    def setX(self, x): 
        self.__x = x 
    
    def getY(self):
        return self.__Y
    
    def setY(self, y ): 
        self.__Y = y 
    
    # Metodo para mostrar la cordenada
    def mostrarCordenada(self):
        print("(",self.__x,","self.__y,")")



