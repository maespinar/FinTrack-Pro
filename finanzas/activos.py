class Activo:
    def __init__(self):
        self.codigoTicket = codigoTicket
        self.nombre = nombre
        self.__montoInvertido = montoInvertido
       
    @property   #getter
    def montoInvertido(self):
        return self.__montoInvertido
    
    @montoInvertido.setter
    def montoInvertido(self, nuevoMonto):
        if(nuevoMonto <= 0):
            raise ValueError("El monto no puede ser negativo")
        self.__montoInvertido = nuevoMonto
        
class ActivoInternacional(Activo):
    def __init__(self):
        self.divisa = divisa
        self.__tasaCambioUSD = tasaCambioUSD
    
    @property   #getter    
    def tasaCambioUSD(self):
        return self.__tasaCambioUSD
    
    @tasaCambioUSD.setter
    def tasaCambioUSD(self, nuevaTasa):
        if(nuevaTasa <= 0):
            raise ValueError("La tasa de cambio no puede ser negativa")
        self.__tasaCambioUSD = nuevaTasa