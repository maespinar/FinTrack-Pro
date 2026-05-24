from .activos import Activo, TickerDuplicadoError
from tabulate import tabulate

class PortafolioAuditoria:
    def __init__(self):
        self.activos_dict = [
            {"Ticker": "AAPL", "Empresa": "Apple", "Inversión": "$1,500.00", "Divisa": "USD"},
            {"Ticker": "AMZN", "Empresa": "Amazon", "Inversión": "€850.00", "Divisa": "EUR"},
            {"Ticker": "SONY", "Empresa": "Sony Corp.", "Inversión": "¥150,000", "Divisa": "JPY"}
        ]
        self.numero_activos =  3
    
    def añadir_activo(self, activo):
        for i in range(self.numero_activos):
            if activo.codigo_ticker == self.activos_dict[i]["Ticker"]:
                raise TickerDuplicadoError(f"El activo con ticker {activo.codigo_ticker} ya esta registrado.")
        nuevo_dict_activo = {
            "Ticker": activo.codigo_ticker,
            "Empresa": activo.nombre,
            "Inversión": f"${activo.monto_invertido:,.2f}",
            "Divisa": activo.divisa
        }
        self.activos_dict.append(nuevo_dict_activo)
        self.numero_activos += 1
    
    def filtrar_por_divisa(self, divisa):
        lista_activos = []
        return lista_activos
    
    def calcular_valor_totalUSD(self):
        return 0
    
    def mostrar_reporte(self):
        if self.numero_activos == 0:
            print("\n[!] El portafolio esta vacio: Sin activos registrados.")
        else:
            print("\n--- REPORTE DE AUDITORÍA INTERNACIONAL ---")
            tabla = tabulate(self.activos_dict, headers="keys", tablefmt="fancy_grid")
            print(tabla)