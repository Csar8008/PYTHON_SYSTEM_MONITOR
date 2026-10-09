import psutil

"""funcion que recopila las métricas del sistema y devuelve un 
diccionario con los valores de CPU, RAM y Disco."""

def get_system_metrics() -> dict:
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    
    return {
        "cpu_percent": psutil.cpu_percent(interval=None),
        "ram_percent": mem.percent,
        "ram_used_gb": mem.used / (1024**3),
        "ram_total_gb": mem.total / (1024**3),
        "disk_percent": disk.percent,
        "disk_used_gb": disk.used / (1024**3),
        "disk_total_gb": disk.total / (1024**3),
    }

"""funcion que obtiene los procesos ordenados por consumo de memoria RAM 
y devuelve una lista de diccionarios con los valores de PID, nombre y uso 
de memoria en MB."""

def get_top_processes(limit: int = 5) -> list[dict]:
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
        try:
            mem_mb = proc.info['memory_info'].rss / (1024 * 1024)
            processes.append({
                'pid': proc.info['pid'],
                'name': proc.info['name'],
                'memory_mb': mem_mb
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    return sorted(processes, key=lambda x: x['memory_mb'], reverse=True)[:limit]