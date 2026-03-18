from flask import Flask, render_template, request
from graph import Graph
from dijkstra import dijkstra
from utils import get_path
from visualize import draw_graph   # ✅ ADD THIS
import os


app = Flask(__name__)

# Global graph
g = Graph()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add():
    u = request.form["u"].upper()
    v = request.form["v"].upper()
    w = int(request.form["w"])

    g.add_edge(u, v, w)

     #clean route list (no duplicates)
    route_list = []
    seen = set()
    
    for city in g.graph:
        for neighbor, weight in g.graph[city]:
            edge = tuple(sorted([city, neighbor]))  # undirected fix
            if edge not in seen:
                seen.add(edge)
                route_list.append((city, neighbor, weight))
                
                
    return render_template("index.html", message="Route added successfully!", routes=route_list)
  
  
@app.route("/find", methods=["POST"])
def find():
    start = request.form["start"].upper()
    end = request.form["end"].upper()

    # 🔥 FIRST: build route list (IMPORTANT FIX)
    route_list = []
    seen = set()

    for city in g.graph:
        for neighbor, weight in g.graph[city]:
            edge = tuple(sorted([city, neighbor]))
            if edge not in seen:
                seen.add(edge)
                route_list.append((city, neighbor, weight))

    # ❌ Invalid city
    if start not in g.graph or end not in g.graph:
        return render_template(
            "index.html",
            message="Invalid city!",
            routes=route_list
        )

    distances, parent = dijkstra(g.graph, start)

    # ❌ No path
    if distances[end] == float('inf'):
        return render_template(
            "index.html",
            message="No path exists!",
            routes=route_list
        )

    path_list = get_path(parent, end)
    path = " -> ".join(path_list)

    draw_graph(g.graph, path_list)

    return render_template(
        "index.html",
        distance=distances[end],
        path=path,
        routes=route_list
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)