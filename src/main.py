import time
from rich.live import Live
from layout import create_app_layout

def main():
    print("Iniciando SysMonitor CLI...\nPresiona Ctrl+C para salir.")
    time.sleep(1)
    
    try:
        with Live(create_app_layout(), refresh_per_second=1) as live:
            while True:
                time.sleep(1)
                live.update(create_app_layout())
    except KeyboardInterrupt:
        print("\n[!] Monitor detenido correctamente.")

if __name__ == "__main__":
    main()