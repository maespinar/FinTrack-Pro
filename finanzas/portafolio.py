from .activos import Activo, TickerDuplicadoError
from tabulate import tabulate

class PortafolioAuditoria:
    def __init__(self):
        self.activos_dict = [
            {"Ticker": "AAPL", "Empresa": "Apple", "Inversión": "$1,500.00", "Divisa": "USD", "Tasa USD": 1.0, "Consolidado_Num": 1500.00},
            {"Ticker": "AMZN", "Empresa": "Amazon", "Inversión": "€850.00", "Divisa": "EUR", "Tasa USD": 1.09, "Consolidado_Num": 926.50},
            {"Ticker": "SONY", "Empresa": "Sony Corp.", "Inversión": "¥150,000", "Divisa": "JPY", "Tasa USD": 0.0067, "Consolidado_Num": 1005.00}
        ]
        self.cantidad_activos =  3
    
    def añadir_activo(self, activo):
        for i in range(self.cantidad_activos):
            if activo.codigo_ticker == self.activos_dict[i]["Ticker"]:
                raise TickerDuplicadoError(f"El activo con ticker {activo.codigo_ticker} ya esta registrado.")
        valor_usd = activo.monto_invertido*activo.tasa_cambio_usd
        nuevo_dict_activo = {
            "Ticker": activo.codigo_ticker,
            "Empresa": activo.nombre,
            "Inversión": f"${activo.monto_invertido:,.2f}",
            "Divisa": activo.divisa,
            "Tasa USD": activo.tasa_cambio_usd, 
            "Consolidado_Num": valor_usd
        }
        self.activos_dict.append(nuevo_dict_activo)
        self.cantidad_activos += 1
    
    def filtrar_por_divisa(self, divisa):
        lista_activos = []
        for activo in self.activos_dict:
            if activo["Divisa"] == divisa:
                activo_visual = {k: v for k, v in activo.items() if k != "Consolidado_Num"}
                lista_activos.append(activo_visual)
        self.mostrar_reporte(lista_activos) 
    
    def calcular_valor_total_usd(self):
        lista_consolidada = []
        for activo_dict in self.activos_dict:
            activo_consolidado = {
                "Ticker": activo_dict["Ticker"],
                "Empresa": activo_dict["Empresa"],
                "Consolidado USD": f"${activo_dict["Consolidado_Num"]:,.2f}"
            }
            lista_consolidada.append(activo_consolidado)
        self.mostrar_reporte(lista_consolidada)
    
    def mostrar_reporte(self, lista_a_mostrar):
        if self.cantidad_activos == 0:
            print("\n[!] El portafolio esta vacio: Sin activos registrados.")
        else:
            print("\n--- REPORTE DE AUDITORÍA INTERNACIONAL ---")
            tabla = tabulate(lista_a_mostrar, headers="keys", tablefmt="fancy_grid")
            print(tabla)