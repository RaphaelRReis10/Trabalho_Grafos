class ListaAdjacencia:
    def __init__(self, vertices):
        self.vertices = vertices
        self.lista = [[] for _ in range(vertices)]
        self.rotulos = [None for _ in range(vertices)]
        self.pesos = [None for _ in range(vertices)]
        self.arestas = {}  # Dicionário para armazenar informações de arestas: {(rotulo1, rotulo2): {"peso": x, "rotulo": y}}

    def adicionar_vertice(self, rotulo=None):
        """Adiciona um novo vértice à lista de adjacência."""
        self.lista.append([])  # Adiciona uma nova lista para o novo vértice
        self.rotulos.append(rotulo)  # Adiciona o rótulo correspondente
        self.pesos.append(None)  # Adiciona um peso padrão (None)
        self.vertices += 1  # Incrementa o número total de vértices
        print(f"Vértice '{rotulo}' adicionado com sucesso!")

    def remover_vertice(self, rotulo):
        """Remove um vértice, suas conexões e suas arestas associadas."""
        try:
            # Verifica se o vértice existe pelo rótulo
            if rotulo not in self.rotulos:
                raise ValueError(f"O vértice '{rotulo}' não existe no grafo.")

            # Encontra o índice do vértice
            indice = self.rotulos.index(rotulo)

            # Remove a linha correspondente na matriz de adjacência
            self.matriz.pop(indice)

            # Remove a coluna correspondente em todas as linhas
            for linha in self.matriz:
                linha.pop(indice)

            # Remove o rótulo e o peso do vértice
            self.rotulos.pop(indice)
            self.pesos_vertices.pop(indice)

            # Atualiza o número de vértices
            self.vertices -= 1

            # Remove as arestas associadas ao vértice
            arestas_a_remover = []
            for (v1, v2) in self.arestas.keys():
                if v1 == rotulo or v2 == rotulo:
                    arestas_a_remover.append((v1, v2))

            for aresta in arestas_a_remover:
                self.arestas.pop(aresta)

            print(f"Vértice '{rotulo}' e suas arestas foram removidos com sucesso!")

        except ValueError as e:
            print(f"Erro: {e}")
        except Exception as e:
            print(f"Erro inesperado: {e}")


    def adicionar_aresta(self, rotulo1, rotulo2):
        """Adiciona uma aresta entre dois vértices identificados por rótulos."""
        indices = [i for i, rotulo in enumerate(self.rotulos) if rotulo in [rotulo1, rotulo2]]
        if len(indices) < 2:
            raise ValueError("Ambos os vértices precisam estar rotulados para adicionar uma aresta.")

        u, v = indices
        if v not in self.lista[u]:
            self.lista[u].append(v)
        if u not in self.lista[v]:
            self.lista[v].append(u)
        self.arestas[(rotulo1, rotulo2)] = {"peso": None, "rotulo": None}
        self.arestas[(rotulo2, rotulo1)] = {"peso": None, "rotulo": None}

    def remover_aresta(self, rotulo1, rotulo2):
        """Remove uma aresta entre dois vértices na lista de adjacência."""
        try:
            # Obter os índices dos vértices a partir dos rótulos
            u = self.rotulos.index(rotulo1)
            v = self.rotulos.index(rotulo2)
        except ValueError:
            raise ValueError(f"Um ou ambos os vértices '{rotulo1}' e '{rotulo2}' não estão rotulados.")

        # Remover 'v' da lista de adjacência de 'u'
        if v in self.lista[u]:
            self.lista[u].remove(v)

        # Remover 'u' da lista de adjacência de 'v'
        if u in self.lista[v]:
            self.lista[v].remove(u)

        # Remover informações da aresta no dicionário de arestas
        self.arestas.pop((rotulo1, rotulo2), None)
        self.arestas.pop((rotulo2, rotulo1), None)

    def rotular_vertice(self, vertice, rotulo):
        """Define um rótulo para um vértice."""
        if 0 <= vertice < self.vertices:
            self.rotulos[vertice] = rotulo
        else:
            raise IndexError(f"Vértice {vertice} fora do intervalo permitido (0 a {self.vertices - 1}).")

    def ponderar_vertice(self, vertice, peso):
        """Define o peso para um vértice."""
        if 0 <= vertice < self.vertices:
            self.pesos[vertice] = peso
        else:
            raise IndexError(f"Vértice {vertice} fora do intervalo permitido (0 a {self.vertices - 1}).")

    def rotular_aresta(self, rotulo1, rotulo2, rotulo_aresta):
        """Define um rótulo para uma aresta."""
        if (rotulo1, rotulo2) in self.arestas:
            self.arestas[(rotulo1, rotulo2)]["rotulo"] = rotulo_aresta
            self.arestas[(rotulo2, rotulo1)]["rotulo"] = rotulo_aresta
        else:
            raise ValueError("A aresta entre esses vértices não existe.")

    def ponderar_aresta(self, rotulo1, rotulo2, peso):
        """Define um peso para uma aresta."""
        if (rotulo1, rotulo2) in self.arestas:
            self.arestas[(rotulo1, rotulo2)]["peso"] = peso
            self.arestas[(rotulo2, rotulo1)]["peso"] = peso
        else:
            raise ValueError("A aresta entre esses vértices não existe.")
        
    def vertices_rotulados(self):
        """Retorna uma lista de índices de vértices que possuem rótulos não nulos."""
        return [i for i, rotulo in enumerate(self.rotulos) if rotulo is not None]

    def exibir(self):
        """Exibe a lista de adjacência com rótulos na primeira linha e coluna."""
        print("Lista de Adjacência:")
        
        # Exibe os rótulos no formato tabela
        for i in range(self.vertices):
            rotulo = self.rotulos[i] if self.rotulos[i] else f"V{i}"
            vizinhos = [self.rotulos[v] if self.rotulos[v] else f"V{v}" for v in self.lista[i]]
            print(f"{rotulo}: {', '.join(vizinhos) if vizinhos else 'Nenhum vizinho'}")
    