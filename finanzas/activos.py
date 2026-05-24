class TickerDuplicadoError(Exception):
    pass

class Activo:
    def __init__(self, codigo_ticker, nombre, monto_invertido):
        self.codigo_ticker = codigo_ticker.upper()
        self.nombre = nombre
        self.monto_invertido = monto_invertido
       
    @property   #getter
    def monto_invertido(self):
        return self.__monto_invertido
    
    @monto_invertido.setter
    def monto_invertido(self, nuevo_monto):
        if nuevo_monto <= 0:
            raise ValueError("El monto no puede ser negativo o cero")
        self.__monto_invertido = nuevo_monto
        
class ActivoInternacional(Activo):
    def __init__(self, codigo_ticker, nombre, monto_invertido, divisa, tasa_cambio_usd):
        super().__init__(codigo_ticker, nombre, monto_invertido)
        self.divisa = divisa.upper()
        self.tasa_cambio_usd = tasa_cambio_usd
    
    @property   #getter    
    def tasa_cambio_usd(self):
        return self.__tasa_cambio_usd
    
    @tasa_cambio_usd.setter
    def tasa_cambio_usd(self, nuevaTasa):
        if nuevaTasa <= 0:
            raise ValueError("La tasa de cambio no puede ser negativa o cero")
        self.__tasa_cambio_usd = nuevaTasa