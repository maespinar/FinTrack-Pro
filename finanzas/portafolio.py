from .activos import Activo, TickerDuplicadoError
from tabulate import tabulate

class PortafolioAuditoria:
    def __init__(self):
        self.activos_dict = {}
        #self.divisa = divisa
        self.datos_prueba = [
            {"Ticker": "AAPL", "Empresa": "Apple", "Inversión": "$1,500.00", "Divisa": "USD"},
            {"Ticker": "AMZN", "Empresa": "Amazon", "Inversión": "€850.00", "Divisa": "EUR"},
            {"Ticker": "SONY", "Empresa": "Sony Corp.", "Inversión": "¥150,000", "Divisa": "JPY"}
        ]
    
    def añadir_activo(self, activo):
        if activo.codigo_ticker in self.activos_dict:
            raise TickerDuplicadoError(f"El activo con ticker {activo.codigo_ticker} ya esta registrado")
        self.activos_dict[activo.codigo_ticker] = activo
    
    def filtrar_por_divisa(self, divisa):
        lista_activos = []
        return lista_activos
    
    def calcular_valor_totalUSD(self):
        return 0
    
    def mostrar_reporte(self):
        print("\n--- REPORTE DE AUDITORÍA INTERNACIONAL ---")
        tabla = tabulate(self.datos_prueba, headers="keys", tablefmt="fancy_grid")
        print(tabla)