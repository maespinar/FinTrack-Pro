import sys
#from finanzas import Activo, PortafolioAuditoria, TickerDuplicadoError

def imprimirCabecera():
    print("\n" + "=" * 50)
    print("     FINTRACK PRO v1.0 - AUDITORÍA IN SITU")
    print("=" * 50)
    print("1. Registrar Activo Internacional")
    print("2. Visualizar Portafolio Actual")
    print("3. Filtrar Activos por Divisa")
    print("4. Calcular Valor Consolidado (USD)")
    print("5. Salir")
    
def iniciarSistema():
    
    while(True):
        imprimirCabecera()
        opcion = input("\nSeleccione una opcion (1-5): ").strip()    
        match opcion:
            case "1":
                print("\n[+] Modulo de registro iniciado (En construccion...)")
                
            case "2":
                print("\n[+] Generando reporte del portafolio (En construcción...)")
                
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
    iniciarSistema()