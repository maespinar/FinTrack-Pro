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
        opcion = input("\nSeleccione una opción (1-5): ").strip()    
        match opcion:
            case "1":
                print("\n[+] Módulo de registro iniciado (En construcción...)")
                try:
                    ticker = input("Código de Ticker (Ej: AAPL): ").strip()
                    nombre = input("Nombre de la empresa: ").strip().title()
                    monto = float(input("Monto invertido original: ").strip())
                    divisa = str(input("Divisa de origen (Ej: EUR): ").strip())
                    tasa = float(input("Tasa de cambio a USD: ").strip())
                    nuevo_activo = ActivoInternacional(ticker, nombre, monto, divisa, tasa)
                    portafolio.añadir_activo(nuevo_activo)
                    print(f"\n[✓] Éxito! El activo {nuevo_activo.codigo_ticker} ha sido auditado y registrado.")
                    
                except ValueError as e:
                    print(f"\n[!] Error de valor: Ingrese valores numerios positivos válidos.")
                    print(f"Detalle de error: {e}")
                except TickerDuplicadoError as e:
                    print(f"\n[!] Error de registro: {e}")
            case "2":
                print("\n[+] Generando reporte del portafolio (En construcción...)")
                lista_limpia = [{k: v for k, v in d.items() if k != "Consolidado_Num"} for d in portafolio.activos_dict]
                portafolio.mostrar_reporte(lista_limpia)
            case "3":
                print("\n[+] Iniciando filtro por divisa (En construcción...)")
                try:
                    divisa_a_filtrar = str(input("Divisa a filtrar: ").strip().upper())
                    portafolio.filtrar_por_divisa(divisa_a_filtrar)
                except:
                    print("\n[!] Error al ingresar la divisa.")
            case "4":
                print("\n[+] Calculando consolidado en USD (En construcción...)")
                portafolio.calcular_valor_total_usd()
            case "5":
                print("\n[!] Cerrando sesión segura de auditoría. ¡Hasta pronto!")
                sys.exit()
            case _:
                print("\n[x] Error de entrada: Por favor, seleccione una opción valida del 1 al 5.")
    
if(__name__ == "__main__"):
    iniciar_sistema()