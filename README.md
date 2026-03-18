# 🚀 Smart Route Optimization System

![Python](https://img.shields.io/badge/Language-Python-blue)
![Dijkstra](https://img.shields.io/badge/Algorithm-Dijkstra-green)
![Graph](https://img.shields.io/badge/DataStructure-Graph-orange)
![NetworkX](https://img.shields.io/badge/Visualization-NetworkX-blueviolet)
![Matplotlib](https://img.shields.io/badge/Plot-Matplotlib-yellow)
![Rich](https://img.shields.io/badge/CLI-Rich-red)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

🚀 **Smart Route Optimization System** is a Python-based application that finds the shortest path between cities using graph algorithms. It includes an interactive CLI and visual graph representation to help users understand optimal routes efficiently.

---

## 🚀 Project Demo

🔗 GitHub Repository: https://github.com/your-username/Smart-Route-Optimizer

---

## 📌 Features

### 🧠 Shortest Path Computation
- Implements **Dijkstra’s Algorithm**
- Finds optimal routes in weighted graphs
- Finds optimal routes in weighted graphs

### 📍 Dynamic Route Management
- Add routes dynamically (CLI + Web UI)
- Supports undirected weighted graphs

### 📊 Graph Visualization
- Visual representation using **NetworkX & Matplotlib**
- Highlights shortest path in **red color**
- Automatically updates on new input

### 🌐 Web Interface (Flask)
- User-friendly browser-based UI
- Add routes and compute paths interactively
- Displays graph visualization inside browser

### 🎨 Interactive CLI
- Styled terminal interface using **Rich**
- User-friendly menu-driven system

### ❌ Error Handling
- Handles invalid city inputs
- Detects disconnected graphs
- Prevents incorrect path outputs

### 🔄 Case-Insensitive Input
- Accepts both uppercase and lowercase inputs

---

## 🛠 Tech Stack

| Category        | Technology Used                     |
|----------------|------------------------------------|
| Language        | Python                             |
| Algorithms      | Dijkstra’s Algorithm               |
| Data Structures | Graph (Adjacency List)             |
| Backend         | Flask                              |
| Visualization   | NetworkX, Matplotlib               |
| Frontend        | HTML, CSS, Bootstrap               |
| CLI Interface   | Python (Menu-based CLI)            |
| Environment     | Python Virtual Environment (.venv) |

---

### 📂 Project Structure
```bash
Smart-Route-Optimizer/
│
├── app.py              # Flask backend (web app)
├── main.py             # CLI-based application
├── graph.py            # Graph implementation
├── dijkstra.py         # Dijkstra algorithm
├── utils.py            # Path reconstruction
├── visualize.py        # Graph visualization (image generation)
│
├── templates/
│   └── index.html      # Web UI
│
├── static/
│   └── graph.png       # Generated graph image
│
├── public/             # Optional images/screenshots
├── README.md
└── .gitignore

```
---

## 📸 Screenshots

### 🔹 Graph Visualization
![Graph Output](/public/Figure_1.png)
---

### 👤 User Workflow

# 🖥 CLI Mode

- Run main.py
- Add routes via menu
- Find shortest path
- View result in terminal + graph window

# 🌐 Web Mode

- Run app.py
- Open browser (http://127.0.0.1:5000)
- Add routes via form
- Compute shortest path
- View result + graph visualization

---

## 📦 Installation Guide

1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/Smart-Route-Optimizer.git
cd Smart-Route-Optimizer
```

2️⃣ Create Virtual Environment
```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
```

3️⃣ Install Dependencies
```bash
pip install networkx matplotlib flask
```

4️⃣ Run the Project
# 🔹 CLI Version
```bash
python main.py
```
# 🔹 Web Version
```bash
python app.py
```
# Open in Brwoser:
```bash
http://127.0.0.1:5000

```
⏱️ Time Complexity

Dijkstra Algorithm: O((V + E) log V)

🧪 Example
Input
```bash
A → B (10)
B → D (5)
C → A (10)
```

Output
```bash
Shortest Distance: 15
Path: A → B → D
```


## 👤 Author

**Nahida Athanikar**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/)
[![GitHub](https://img.shields.io/badge/GitHub-Profile-black?style=for-the-badge&logo=github)](https://github.com/nahida-athanikar)
[![Email](https://img.shields.io/badge/Email-Contact-red?style=for-the-badge&logo=gmail)](mailto:your-email@gmail.com)
