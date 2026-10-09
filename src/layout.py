from rich.align import Align
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table

from system_info import get_system_metrics, get_top_processes

"""funcion que genera la tabla con las métricas del sistema y devuelve un objeto 
Table de Rich."""

def build_system_table() -> Table:
    metrics = get_system_metrics()
    
    table = Table(title="Métricas del Sistema", expand=True)
    table.add_column("Recurso", style="bold yellow", no_wrap=True)
    table.add_column("Uso / Estado", style="white")

    table.add_row("CPU Global", f"{metrics['cpu_percent']}%")
    table.add_row(
        "Memoria RAM", 
        f"{metrics['ram_percent']}% ({metrics['ram_used_gb']:.2f} GB / {metrics['ram_total_gb']:.2f} GB)"
    )
    table.add_row(
        "Disco (/)", 
        f"{metrics['disk_percent']}% ({metrics['disk_used_gb']:.2f} GB / {metrics['disk_total_gb']:.2f} GB)"
    )

    return table

"""funcion que genera la tabla con el Top 5 de procesos y devuelve un objeto
Table de Rich."""

def build_process_table() -> Table:
    processes = get_top_processes(limit=5)
    
    table = Table(title="Top 5 Procesos (por Memoria)", expand=True)
    table.add_column("PID", style="dim", width=8)
    table.add_column("Nombre", style="bold magenta")
    table.add_column("Uso Memoria (MB)", justify="right")

    for proc in processes:
        table.add_row(str(proc['pid']), proc['name'], f"{proc['memory_mb']:.1f} MB")

    return table

"""funcion que organiza la estructura de la pantalla dividida en paneles y devuelve
un objeto Layout de Rich."""

def create_app_layout() -> Layout:
    layout = Layout()
    layout.split_column(
        Layout(name="header", size=3),
        Layout(name="body")
    )
    layout["body"].split_row(
        Layout(name="left"),
        Layout(name="right")
    )

    header_text = Align.center("[bold green]SysMonitor CLI - Monitor de Recursos[/bold green]")
    layout["header"].update(Panel(header_text, style="green"))
    layout["left"].update(build_system_table())
    layout["right"].update(build_process_table())

    return layout