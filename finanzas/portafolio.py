from .activos import Activo, TicketDuplicadoError
from tabulate import tabulate

class PortafolioAuditoria:
    def __init__(self):
        self.activos_dict = {}
        self.divisa = divisa
        self.datos_prueba = [
            {"Ticket": "AAPL", "Empresa": "Apple", "Inversión": "$1,500.00", "Divisa": "USD"},
            {"Ticket": "AMZN", "Empresa": "Amazon", "Inversión": "€850.00", "Divisa": "EUR"},
            {"Ticket": "SONY", "Empresa": "Sony Corp.", "Inversión": "¥150,000", "Divisa": "JPY"}
        ]
    
    def añadir_activo(activo):
        pass
    
    def filtrar_por_divisa(divisa):
        lista_activos = []
        return lista_activos
    
    def calcular_valor_totalUSD():
        return 0
    
    def mostrar_reporte():
        print("\n--- REPORTE DE AUDITORÍA INTERNACIONAL ---")
        tabla = tabulate(self.datos_prueba, headers="keys", tablefmt="fancy_grid")
        print(tabla)