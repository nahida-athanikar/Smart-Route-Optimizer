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
- Finds optimal routes between cities
- Efficient handling of weighted graphs

### 📍 Dynamic Route Management
- Add routes dynamically via CLI
- Supports undirected weighted graphs

### 📊 Graph Visualization
- Visual representation using **NetworkX & Matplotlib**
- Highlights shortest path in **red color**

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
| Algorithms      | Dijkstra’s Shortest Path Algorithm |
| Data Structures | Graph (Adjacency List)             |
| Visualization   | NetworkX, Matplotlib               |
| CLI Interface   | Rich (Colorful Terminal UI)        |
| Environment     | Python Virtual Environment (.venv) |

---

## 📂 Project Structure

```bash
Smart-Route-Optimizer/
│
├── main.py          # Main CLI application
├── graph.py         # Graph implementation
├── dijkstra.py      # Dijkstra algorithm
├── utils.py         # Path reconstruction
├── visualize.py     # Graph visualization
├── README.md
└── .gitignore

```
---

## 📸 Screenshots

![Graph Output](screenshot.png)

---

## 👤 User Workflow

1. **Start Application**
   - Run the Python script using terminal

2. **Add Routes**
   - Input city connections with distances

3. **Find Shortest Path**
   - Enter source and destination cities

4. **View Result**
   - Displays shortest distance and path

5. **Visualize Graph**
   - Graph window shows nodes and highlighted shortest path

6. **Exit Application**
   - Select exit option from menu

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
pip install networkx matplotlib rich
```

4️⃣ Run the Project
```bash
python main.py
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

🚀 Future Improvements

🌍 Map-based visualization (Folium)

💾 Save & load graph from files

🖥 GUI version (Tkinter / Web)

🔍 Multi-route comparison


## 👤 Author

**Nahida Athanikar**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/)
[![GitHub](https://img.shields.io/badge/GitHub-Profile-black?style=for-the-badge&logo=github)](https://github.com/nahida-athanikar)
[![Email](https://img.shields.io/badge/Email-Contact-red?style=for-the-badge&logo=gmail)](mailto:your-email@gmail.com)
