from .activos import Activo, TickerDuplicadoError
from tabulate import tabulate

class PortafolioAuditoria:
    def __init__(self):
        self.activos_dict = [
            {"Ticker": "AAPL", "Empresa": "Apple", "Inversión": "$1,500.00", "Divisa": "USD"},
            {"Ticker": "AMZN", "Empresa": "Amazon", "Inversión": "€850.00", "Divisa": "EUR"},
            {"Ticker": "SONY", "Empresa": "Sony Corp.", "Inversión": "¥150,000", "Divisa": "JPY"}
        ]
        self.cantidad_activos =  3
    
    def añadir_activo(self, activo):
        for i in range(self.cantidad_activos):
            if activo.codigo_ticker == self.activos_dict[i]["Ticker"]:
                raise TickerDuplicadoError(f"El activo con ticker {activo.codigo_ticker} ya esta registrado.")
        nuevo_dict_activo = {
            "Ticker": activo.codigo_ticker,
            "Empresa": activo.nombre,
            "Inversión": f"${activo.monto_invertido:,.2f}",
            "Divisa": activo.divisa
        }
        self.activos_dict.append(nuevo_dict_activo)
        self.cantidad_activos += 1
    
    def filtrar_por_divisa(self, divisa):
        lista_activos = []
        for activo in self.activos_dict:
            if activo["Divisa"] == divisa:
                lista_activos.append(activo)
        self.mostrar_reporte(lista_activos) 
    
    def calcular_valor_totalUSD(self):
        return 0
    
    def mostrar_reporte(self, lista_a_mostrar):
        if self.cantidad_activos == 0:
            print("\n[!] El portafolio esta vacio: Sin activos registrados.")
        else:
            print("\n--- REPORTE DE AUDITORÍA INTERNACIONAL ---")
            tabla = tabulate(lista_a_mostrar, headers="keys", tablefmt="fancy_grid")
            print(tabla)