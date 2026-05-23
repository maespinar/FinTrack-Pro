class TicketDuplicadoError(Exception):
    pass

class Activo:
    def __init__(self, codigo_ticket, nombre, monto_invertido):
        self.codigo_ticket = codigo_ticket.upper()
        self.nombre = nombre
        self.__monto_invertido = monto_invertido
       
    @property   #getter
    def monto_invertido(self):
        return self.__monto_invertido
    
    @monto_invertido.setter
    def monto_invertido(self, nuevo_monto):
        if nuevo_monto <= 0:
            raise ValueError("El monto no puede ser negativo")
        self.__monto_invertido = nuevo_monto
        
class ActivoInternacional(Activo):
    def __init__(self):
        self.divisa = divisa
        self.__tasa_cambioUSD = tasa_cambioUSD
    
    @property   #getter    
    def tasa_cambioUSD(self):
        return self.__tasa_cambioUSD
    
    @tasa_cambioUSD.setter
    def tasa_cambioUSD(self, nuevaTasa):
        if nuevaTasa <= 0:
            raise ValueError("La tasa de cambio no puede ser negativa")
        self.__tasa_cambioUSD = nuevaTasa