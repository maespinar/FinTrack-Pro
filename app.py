import sys
from finanzas import Activo, ActivoInternacional, PortafolioAuditoria, TickerDuplicadoError

def imprimir_cabecera():
    print("\n" + "=" * 50)
    print("     FINTRACK PRO v1.0 - AUDITORÍA IN SITU")
    print("=" * 50)
    print("1. Registrar Activo Internacional")
    print("2. Visualizar Portafolio Actual")
    print("3. Filtrar Activos por Divisa")
    print("4. Calcular Valor Consolidado (USD)")
    print("5. Salir")
    
def iniciar_sistema():
    portafolio = PortafolioAuditoria()
    while True:
        imprimir_cabecera()
        opcion = input("\nSeleccione una opcion (1-5): ").strip()    
        match opcion:
            case "1":
                print("\n[+] Modulo de registro iniciado (En construccion...)")
                try:
                    ticker = input("Codigo de Ticker (Ej: AAPL): ").strip()
                    nombre = input("Nombre de la empresa: ").strip()
                    monto = float(input("Monto invertido original: ").strip())
                    divisa = input("Divisa de origen (Ej: EUR): ").strip()
                    tasa = float(input("Tasa de cambio a USD: ").strip())
                    nuevo_activo = ActivoInternacional(ticker, nombre, monto, divisa, tasa)
                    portafolio.añadir_activo(nuevo_activo)
                    print(f"\n[✓] Exito! El activo {nuevo_activo.codigo_ticker} ha sido auditado y registrado.")
                    
                except ValueError as e:
                    print(f"\n[!] Error de valor: Ingrese valores numerios positivos validos.")
                    print(f"Detalle de error: {e}")
                except TickerDuplicadoError as e:
                    print(f"\n[!] Error de registro: {e}")
                
            case "2":
                print("\n[+] Generando reporte del portafolio (En construcción...)")
                portafolio.mostrar_reporte()
            case "3":
                print("\n[+] Iniciando filtro por divisa (En construcción...)")
                
            case "4":
                print("\n[+] Calculando consolidado en USD (En construcción...)")
                
            case "5":
                print("\n[!] Cerrando sesión segura de auditoría. ¡Hasta pronto!")
                sys.exit()
            case _:
                print("\n[x] Error de entrada: Por favor, seleccione una opcion valida del 1 al 5.")
    
if(__name__ == "__main__"):
    iniciar_sistema()