import matplotlib.pyplot as plt
import networkx as nx

def desenhar_grafo(matriz, rotulos, pesos_vertices, arestas):
    """Desenha o grafo exibindo rótulos e pesos dos vértices e arestas."""
    G = nx.Graph()

    # Adicionar vértices com pesos e rótulos
    for i, rotulo in enumerate(rotulos):
        if rotulo is None:
            rotulo = f"V{i}"
        G.add_node(rotulo, peso=pesos_vertices[i])

    # Adicionar arestas com pesos e rótulos
    for (rotulo1, rotulo2), atributos in arestas.items():
        peso = atributos.get("peso", 1)
        rotulo_aresta = atributos.get("rotulo", "")
        G.add_edge(rotulo1, rotulo2, peso=peso, rotulo=rotulo_aresta)

    # Layout dos nós
    pos = nx.spring_layout(G, seed=42)

    # Configurações para os nós
    node_colors = ["#87CEEB"]  # Todos os nós na cor azul claro
    node_sizes = [800 for _ in G.nodes()]  # Tamanho fixo para todos os nós

    # Criar rótulos dos vértices no formato "rótulo (peso)"
    node_labels = {node: f"{node} ({G.nodes[node]['peso']})" for node in G.nodes()}

    # Desenhar nós
    nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, edgecolors="#2F4F4F")
    nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=10, font_color="black")

    # Desenhar arestas
    nx.draw_networkx_edges(G, pos, width=1, edge_color="black")  # Arestas pretas e finas

    # Criar rótulos das arestas no formato "rótulo (peso)"
    edge_labels = {
        (u, v): f"{data['rotulo']} ({int(data['peso'])})" if data["rotulo"] else f"{int(data['peso'])}"
        for u, v, data in G.edges(data=True)
    }
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8, font_color="black")

    # Título estilizado
    plt.title("Grafo", fontsize=25, color="#4682B4")
    plt.axis("off")
    plt.show()
