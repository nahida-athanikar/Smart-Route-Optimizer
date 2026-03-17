from graph import Graph
from dijkstra import dijkstra
from utils import get_path
from visualize import draw_graph

from rich import print
from rich.console import Console

console = Console()

g = Graph()

def menu():
    console.print("\n[bold cyan]===== Smart Route Optimizer =====[/bold cyan]")
    console.print("[green]1.[/green] Add Route")
    console.print("[yellow]2.[/yellow] Find Shortest Path")
    console.print("[red]3.[/red] Exit")


while True:
    menu()
    choice = input("Enter choice: ")

    # ➤ Add Route
    if choice == "1":
        u = input("From city: ").upper()
        v = input("To city: ").upper()

        if not u.isalpha() or not v.isalpha():
            console.print("[red]City name should be alphabets only![/red]")
            continue

        try:
            w = int(input("Distance: "))
        except:
            console.print("[red]Invalid distance![/red]")
            continue

        g.add_edge(u, v, w)
        console.print("[green]Route added successfully![/green]")

    # ➤ Find Shortest Path
    elif choice == "2":
        start = input("Enter start city: ").upper()
        end = input("Enter destination city: ").upper()

        if start not in g.graph or end not in g.graph:
            console.print("[red]Invalid city! Please add route first.[/red]")
            continue

        distances, parent = dijkstra(g.graph, start)

        # ❗ No path check
        if distances[end] == float('inf'):
            console.print("[red]\nNo path exists between these cities![/red]")
            continue

        path = get_path(parent, end)

        console.print(f"\n[bold yellow]Shortest Distance:[/bold yellow] {distances[end]}")
        console.print(f"[bold cyan]Path:[/bold cyan] {' -> '.join(path)}")

        draw_graph(g.graph, path)

    # ➤ Exit
    elif choice == "3":
        console.print("[bold red]Exiting... 👋[/bold red]")
        break

    else:
        console.print("[red]Invalid choice! Try again.[/red]")