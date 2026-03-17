def get_path(parent, destination):
    path = []
    while destination:
        path.append(destination)
        destination = parent[destination]
    return path[::-1]