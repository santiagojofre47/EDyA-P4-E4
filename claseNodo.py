class Nodo:
    __clave = None
    __frecuencia = None
    __sigIzq = None
    __sigDer = None
    
    def __init__(self, clave,frecuencia):
        self.__clave = clave
        self.__frecuencia = frecuencia
        self.__sigIzq = None
        self.__sigDer = None
    
    def setSigIzquierdo(self, sig):
        self.__sigIzq = sig
    
    def setSigDerecho(self, sig):
        self.__sigDer = sig
    
    def setClave(self, clave):
        self.__clave = clave
    
    def getClave(self):
        return self.__clave
    
    def getSigIzquierdo(self):
        return self.__sigIzq
    
    def getSigDerecho(self):
        return self.__sigDer
    
    def getFrecuencia(self):
        return self.__frecuencia
    
    def __str__(self):
        return 'Caracter: {} frecuencia: {}'.format(self.__clave,self.__frecuencia)
    
    def __eq__(self, otro):
        if type(otro) == str:
            return self.getClave() == otro
    
    def __gt__(self, otro):
        if isinstance(otro,Nodo):
            return otro.getFrecuencia() < self.getFrecuencia()
        
    