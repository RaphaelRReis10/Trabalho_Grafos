import math
import heapq

class MatrizAdjacencia:
    def __init__(self, vertices):
        self.vertices = vertices
        self.matriz = [[0 for _ in range(vertices)] for _ in range(vertices)]
        self.rotulos = [None] * vertices
        self.pesos_vertices = [None] * vertices  # Lista para armazenar pesos dos vértices
        self.arestas = {}

    def adicionar_vertice(self, rotulo=None):
        """Adiciona um novo vértice à matriz de adjacência."""
        for linha in self.matriz:
            linha.append(0)  # Adiciona uma nova coluna
        self.matriz.append([0] * (self.vertices + 1))  # Adiciona uma nova linha
        self.rotulos.append(rotulo)  # Adiciona o rótulo correspondente
        self.pesos_vertices.append(None)  # Adiciona um peso inicial (None) para o novo vértice
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
        # Converte rótulos para índices
        try:
            u = self.rotulos.index(rotulo1)
            v = self.rotulos.index(rotulo2)
        except ValueError:
            raise ValueError("Ambos os vértices precisam estar rotulados para adicionar uma aresta.")

        self.verificar_rotulo_vertice(u)
        self.verificar_rotulo_vertice(v)

        self.matriz[u][v] = 1
        self.matriz[v][u] = 1
        self.arestas[(rotulo1, rotulo2)] = {"peso": 1, "rotulo": None}
        self.arestas[(rotulo2, rotulo1)] = {"peso": 1, "rotulo": None}

    def remover_aresta(self, rotulo1, rotulo2):
        """Remove uma aresta da matriz de adjacência e da lista de arestas."""
        try:
            u = self.rotulos.index(rotulo1)
            v = self.rotulos.index(rotulo2)
        except ValueError:
            raise ValueError("Ambos os vértices precisam estar rotulados para remover uma aresta.")

        # Verificar se a aresta existe na matriz
        if self.matriz[u][v] == 0 or self.matriz[v][u] == 0:
            raise ValueError(f"A aresta entre '{rotulo1}' e '{rotulo2}' não existe.")

        # Remover a aresta da matriz
        self.matriz[u][v] = 0
        self.matriz[v][u] = 0

        # Remover a aresta da lista de arestas
        if (rotulo1, rotulo2) in self.arestas:
            del self.arestas[(rotulo1, rotulo2)]
        if (rotulo2, rotulo1) in self.arestas:
            del self.arestas[(rotulo2, rotulo1)]

    def rotular_vertice(self, vertice, rotulo):
        if 0 <= vertice < self.vertices:
            self.rotulos[vertice] = rotulo
        else:
            raise IndexError("Vértice fora do intervalo permitido.")

    def ponderar_vertice(self, vertice, peso):
        """Define um peso para o vértice."""
        if 0 <= vertice < self.vertices:
            self.pesos_vertices[vertice] = peso
        else:
            raise IndexError("Vértice fora do intervalo permitido.")

    def rotular_aresta(self, rotulo1, rotulo2, rotulo_aresta):
        # Verifica se os vértices estão rotulados
        if rotulo1 not in self.rotulos or rotulo2 not in self.rotulos:
            raise ValueError(f"Um ou ambos os vértices ({rotulo1}, {rotulo2}) não estão rotulados.")
        
        # Verifica se a aresta entre os vértices existe
        self.verificar_rotulo_aresta(rotulo1, rotulo2)
        
        # Se todos os testes passarem, rotula a aresta
        self.arestas[(rotulo1, rotulo2)]["rotulo"] = rotulo_aresta
        self.arestas[(rotulo2, rotulo1)]["rotulo"] = rotulo_aresta

    def ponderar_aresta(self, rotulo1, rotulo2, peso):
        # Verifica se os vértices estão rotulados
        if rotulo1 not in self.rotulos or rotulo2 not in self.rotulos:
            raise ValueError(f"Um ou ambos os vértices ({rotulo1}, {rotulo2}) não estão rotulados.")
        
        # Verifica se a aresta entre os vértices existe
        self.verificar_rotulo_aresta(rotulo1, rotulo2)
        
        # Se todos os testes passarem, pondera a aresta
        self.arestas[(rotulo1, rotulo2)]["peso"] = peso
        self.arestas[(rotulo2, rotulo1)]["peso"] = peso

    def verificar_rotulo_vertice(self, vertice):
        if 0 <= vertice < self.vertices:
            if self.rotulos[vertice] is None:
                raise ValueError(f"O vértice {vertice} ainda não possui um rótulo.")
        else:
            raise IndexError(f"Vértice {vertice} fora do intervalo permitido (0 a {self.vertices - 1}).")

    def verificar_rotulo_aresta(self, rotulo1, rotulo2):
        if (rotulo1, rotulo2) not in self.arestas:
            raise ValueError(f"A aresta entre '{rotulo1}' e '{rotulo2}' não está definida ou não existe.")

    def get_arestas(self):
        arestas = []
        for i in range(self.vertices):
            for j in range(i + 1, self.vertices):  # Considerando grafo não direcionado
                if self.matriz[i][j] != 0:  # Verifica se há aresta
                    rotulo_i = self.rotulos[i] if self.rotulos[i] else f"V{i}"
                    rotulo_j = self.rotulos[j] if self.rotulos[j] else f"V{j}"
                    arestas.append((rotulo_i, rotulo_j))
        return arestas

    def exibir(self):
        """Exibe a matriz de adjacência com rótulos e pesos dos vértices e arestas."""
        print("Matriz de Adjacência:")

        # Define o número máximo de dígitos que os números podem ter para formatação
        max_len = max(
            len(str(int(self.arestas.get((self.rotulos[i], self.rotulos[j]), {}).get("peso", 0))))
            if self.matriz[i][j] != 0 else 1
            for i in range(self.vertices)
            for j in range(self.vertices)
        )
        
        # Exibe a primeira linha com os rótulos dos vértices
        header = [" "] + [self.rotulos[i] if self.rotulos[i] else f"V{i}" for i in range(self.vertices)]
        header_str = "   |   ".join([h.center(max_len) for h in header])
        print(header_str)

        # Exibe a linha de separação
        print("---|---".join(["-" * max_len] * len(header)))

        # Exibe a matriz com os rótulos e os valores das arestas
        for i in range(self.vertices):
            rotulo = self.rotulos[i] if self.rotulos[i] else f"V{i}"
            linha = [f"{rotulo.center(max_len)}"] + [
                # Exibe o peso da aresta (se existir) ou "0" se não houver aresta
                str(int(self.arestas.get((self.rotulos[i], self.rotulos[j]), {}).get("peso", 0)))
                if self.matriz[i][j] != 0 else "0"
                for j in range(self.vertices)
            ]
            
            # Exibe a linha com os valores centralizados e a separação "|"
            print("   |   ".join([str(valor).center(max_len) for valor in linha]))
            
            # Exibe a linha de separação após cada linha da matriz
            if i < self.vertices - 1:
                print("---|---".join(["-" * max_len] * len(header)))

    def existe_aresta(self, v1, v2):
        # Converte rótulos para índices
        try:
            v1 = self.rotulos.index(v1) if isinstance(v1, str) else v1
            v2 = self.rotulos.index(v2) if isinstance(v2, str) else v2
        except ValueError:
            raise ValueError("Vértices não encontrados na lista de rótulos.")
        
        return self.matriz[v1][v2] != 0

    def exibir_todas_arestas(self):
        """Exibe todas as arestas armazenadas no dicionário self.arestas, incluindo as sem peso ou rótulo."""
        if not self.arestas:
            print("Não há arestas na matriz.")
            return

        print("Todas as arestas na matriz de adjacência:")
        for (v1, v2), atributos in self.arestas.items():
            peso = atributos.get("peso", "Não definido")
            rotulo = atributos.get("rotulo", "Não definido")
            print(f"Aresta entre '{v1}' e '{v2}': Peso = {peso}, Rótulo = {rotulo}")

    def vizinhos(self, v1):
        """Retorna os rótulos dos vértices vizinhos de um vértice dado."""
        try:
        # Converte rótulo para índice, se necessário
            v1 = self.rotulos.index(v1) if isinstance(v1, str) else v1
        except ValueError:
        # Retorna None para indicar erro, sem imprimir diretamente
            return None
    # Obtém os índices vizinhos
        vizinhos_indices = [i for i in range(self.vertices) if self.matriz[v1][i] != 0]
        return [self.rotulos[i] if self.rotulos[i] else f"V{i}" for i in vizinhos_indices]
    
    def grau_vertice(self, v1):
        "Calcula e retorna o grau do vértice especificado."
        try:
        # Converte rótulo para índice, se necessário
            v1 = self.rotulos.index(v1) if isinstance(v1, str) else v1
        except ValueError:
        # Retorna None para indicar que o vértice não existe
            return None

    # Soma o número de conexões (grau do vértice)
        grau = sum(1 for i in range(self.vertices) if self.matriz[v1][i] != 0)
        return grau
    
    def eh_completo(self):
        "Verifica se o grafo é completo."
    # Um grafo completo precisa ter pelo menos um vértice
        if self.vertices <= 1:
            return None  # Retorna None para indicar erro ou falta de definição
        # Verifica se todos os pares de vértices estão conectados
        for i in range(self.vertices):
            for j in range(self.vertices):
                # Se i != j, deve haver uma aresta; caso contrário, retorna False
                if i != j and self.matriz[i][j] == 0:
                    return False
        return True  # Todos os pares de vértices estão conectados
    
    def eh_regular(self):
        "Verifica se o grafo é regular (todos os vértices têm o mesmo grau)."
        # Grafo com menos de 1 vértice não é regular
        if self.vertices <= 0:
            return None  # Grafo inválido ou não definido
        # Calcula o grau do primeiro vértice
        grau_referencia = sum(self.matriz[0])
        # Verifica se todos os vértices têm o mesmo grau
        for i in range(1, self.vertices):
            if sum(self.matriz[i]) != grau_referencia:
                return False
        return True  # Todos os vértices têm o mesmo grau
    
    def eh_conexo(self):
        """Verifica se o grafo é conexo a partir do algoritmo DFS(existe um caminho entre todos os pares de vértices)."""
        # Grafo com menos de 2 vértices não pode ser conexo
        if self.vertices < 2:
            return None  # Grafo inválido ou mal definido

        # Função auxiliar para fazer a busca em profundidade (DFS)
        def dfs(v, visitados):
            visitados.add(v)
            for i in range(self.vertices):
                if self.matriz[v][i] != 0 and i not in visitados:
                    dfs(i, visitados)

        # Começamos a busca a partir do primeiro vértice
        visitados = set()
        dfs(0, visitados)

        # Se o número de vértices visitados for igual ao número de vértices no grafo, é conexo
        return len(visitados) == self.vertices

    def eh_ciclico(self):
        """Verifica se o grafo possui ciclo."""
        # Função auxiliar para a busca em profundidade
        def dfs(v, visitados, pai):
            visitados[v] = True
            for i in range(self.vertices):
                if self.matriz[v][i] != 0:  # Se há uma aresta entre v e i
                    # Se o vértice i não foi visitado, faz a DFS recursiva
                    if not visitados[i]:
                        if dfs(i, visitados, v):                           
                            return True
                    # Se o vértice i foi visitado e não é o pai, há um ciclo
                    elif i != pai:                      
                        return True
            return False

        # Lista de vértices visitados
        visitados = [False] * self.vertices
        
        # Verifica se existe ciclo a partir de cada vértice
        for i in range(self.vertices):
            if not visitados[i]:
                if dfs(i, visitados, -1):
                    return True  # Se encontrar um ciclo, retorna True

        return False  # Se não encontrar ciclo, retorna False
    
    def eh_euleriano(self):
        """Verifica se o grafo é euleriano."""
        # Primeiro, verifica se o grafo é conexo
        if not self.eh_conexo2():
            return False  # Se não for conexo, não é euleriano
        
        # Verifica se todos os vértices têm grau par
        for i in range(self.vertices):
            grau = sum(self.matriz[i])  # Grau do vértice i
            if grau % 2 != 0:  # Se o grau for ímpar, o grafo não é euleriano
                return False
        
        # Se for conexo e todos os vértices têm grau par, é euleriano
        return True

    def eh_conexo2(self):
        "Verifica se o grafo é conexo utilizando BFS ou DFS."
        visitados = [False] * self.vertices
        # Realiza uma busca em profundidade (DFS) ou em largura (BFS) a partir do primeiro vértice
        self._dfs(0, visitados)
        
        # Se algum vértice não for visitado, o grafo não é conexo
        for i in range(self.vertices):
            if not visitados[i]:
                return False
        return True

    def _dfs(self, v, visitados):
        "Função auxiliar para DFS a partir do vértice v."
        visitados[v] = True
        for i in range(self.vertices):
            if self.matriz[v][i] == 1 and not visitados[i]:
                self._dfs(i, visitados)

    def busca_em_profundidade(self, vertice_inicial):
        "Realiza uma busca em profundidade no grafo a partir do vértice inicial."
        visitados = set()  # Conjunto para armazenar vértices visitados
        caminho = []  # Lista para registrar a ordem dos vértices visitados

        def dfs(vertice):
            """Função recursiva para visitar os vértices."""
            visitados.add(vertice)
            caminho.append(vertice)
            for vizinho in self.vizinhos(vertice):  # Método já implementado
                if vizinho not in visitados:
                    dfs(vizinho)
        try:
            if vertice_inicial not in self.rotulos:
                raise ValueError(f"Vértice '{vertice_inicial}' não encontrado no grafo.")

            # Inicia a DFS
            dfs(vertice_inicial)

            # Retorna o caminho percorrido
            print(f"Busca em profundidade iniciada no vértice '{vertice_inicial}':")
            print(" -> ".join(caminho))
            return caminho
        except ValueError as e:
            print(f"Erro: {e}")
        except Exception as e:
            print(f"Erro inesperado: {e}")

    def busca_em_largura(estrutura, vertice_inicial):
        "Realiza uma busca em largura (BFS) no grafo a partir do vértice inicial."
        visitados = set()  # Conjunto para armazenar vértices visitados
        fila = []  # Fila para controle da BFS
        caminho = []  # Lista para registrar a ordem dos vértices visitados

        try:
            # Verifica se o vértice inicial é válido
            if vertice_inicial not in estrutura.rotulos:
                raise ValueError(f"Vértice '{vertice_inicial}' não encontrado no grafo.")
            
            # Encontra o índice do vértice inicial
            indice_inicial = estrutura.rotulos.index(vertice_inicial)

            # Adiciona o vértice inicial à fila e ao conjunto de visitados
            fila.append(indice_inicial)
            visitados.add(indice_inicial)

            # Executa a busca em largura
            while fila:
                # Remove o primeiro elemento da fila
                vertice_atual = fila.pop(0)
                rotulo_atual = estrutura.rotulos[vertice_atual]
                caminho.append(rotulo_atual)

                # Obtém os vizinhos do vértice atual
                vizinhos = estrutura.vizinhos(rotulo_atual)
                for vizinho in vizinhos:
                    indice_vizinho = estrutura.rotulos.index(vizinho)
                    if indice_vizinho not in visitados:
                        fila.append(indice_vizinho)
                        visitados.add(indice_vizinho)

            # Imprime o resultado
            print(f"Busca em largura iniciada no vértice '{vertice_inicial}':")
            print(" -> ".join(caminho))
            return caminho

        except ValueError as e:
            print(f"Erro: {e}")
        except Exception as e:
            print(f"Erro inesperado: {e}")

    def dijkstra2(estrutura, vertice_origem):
        """Calcula a menor distância do vértice de origem para todos os outros vértices usando o algoritmo de Dijkstra."""
        try:
            # Verifica se o vértice de origem é válido
            if vertice_origem not in estrutura.rotulos:
                raise ValueError(f"Vértice '{vertice_origem}' não encontrado no grafo.")

            # Verifica se há pesos negativos nas arestas
            for i in range(len(estrutura.matriz)):
                for j in range(len(estrutura.matriz[i])):
                    if estrutura.matriz[i][j] < 0:
                        raise ValueError("O grafo contém arestas com pesos negativos. "
                                        "Dijkstra não suporta pesos negativos. Considere usar Bellman-Ford.")

            # Inicializa os índices e estruturas auxiliares
            n = len(estrutura.rotulos)
            distancias = {vertice: math.inf for vertice in estrutura.rotulos}  # Dicionário de distâncias
            distancias[vertice_origem] = 0  # Distância para a origem é 0
            visitados = set()  # Conjunto para manter rastreamento dos vértices visitados
            fila_prioridade = [(0, vertice_origem)]  # Fila de prioridade como (distância, vértice)

            while fila_prioridade:
                # Extração do vértice com menor distância
                distancia_atual, vertice_atual = heapq.heappop(fila_prioridade)

                if vertice_atual in visitados:
                    continue
                visitados.add(vertice_atual)

                # Atualiza as distâncias dos vizinhos
                indice_atual = estrutura.rotulos.index(vertice_atual)
                for vizinho in estrutura.vizinhos(vertice_atual):
                    indice_vizinho = estrutura.rotulos.index(vizinho)
                    peso_aresta = estrutura.matriz[indice_atual][indice_vizinho]
                    # Aqui é onde o peso da aresta é utilizado para calcular a nova distância
                    if peso_aresta >= 0:  # Considera apenas arestas válidas com peso não negativo
                        nova_distancia = distancia_atual + peso_aresta
                        if nova_distancia < distancias[vizinho]:
                            distancias[vizinho] = nova_distancia
                            heapq.heappush(fila_prioridade, (nova_distancia, vizinho))
            # Exibe os resultados
            print(f"Menores distâncias a partir do vértice '{vertice_origem}':")
            for vertice, distancia in distancias.items():
                print(f"{vertice}: {'Infinito' if distancia == math.inf else distancia}")
            return nova_distancia

        except ValueError as e:
            print(f"Erro: {e}")
        except Exception as e:
            print(f"Erro inesperado: {e}")

    def dijkstra(self, inicio):
        try:
            # Verifica se o grafo possui vértices e arestas
            if not any(self.rotulos):
                raise ValueError("O grafo está vazio, nenhum vértice foi adicionado.")
            if not self.arestas:
                raise ValueError("O grafo não possui arestas.")

            # Verifica se o vértice inicial está no grafo
            if inicio not in self.rotulos:
                raise ValueError(f"O vértice '{inicio}' não está no grafo.")

            # Verifica se há pesos negativos nas arestas
            if any(info["peso"] < 0 for info in self.arestas.values()):
                raise ValueError("O algoritmo de Dijkstra não suporta arestas com pesos negativos.")

            # Obter índice do vértice inicial
            indice_inicio = self.rotulos.index(inicio)

            # Inicializa as distâncias, caminhos e o conjunto de visitados
            distancias = {rotulo: float('inf') for rotulo in self.rotulos if rotulo is not None}
            distancias[inicio] = 0
            caminhos = {rotulo: [] for rotulo in self.rotulos if rotulo is not None}
            caminhos[inicio] = [inicio]
            visitados = set()

            # Min-heap para selecionar o vértice com menor distância
            heap = [(0, inicio)]  # Armazena (distância acumulada, rótulo do vértice)

            while heap:
                distancia_atual, vertice_atual = heapq.heappop(heap)

                # Ignora vértices já visitados
                if vertice_atual in visitados:
                    continue

                visitados.add(vertice_atual)

                # Obter índice do vértice atual
                indice_atual = self.rotulos.index(vertice_atual)

                # Atualiza as distâncias e caminhos para os vértices adjacentes
                for (v1, v2), info in self.arestas.items():
                    if v1 == vertice_atual and v2 not in visitados:
                        peso_aresta = info["peso"]
                        
                        # Obter índice do vértice adjacente
                        indice_v2 = self.rotulos.index(v2)

                        # Obter peso do vértice adjacente (ou 0 se None)
                        peso_vertice = self.pesos_vertices[indice_v2]
                        if peso_vertice is None:
                            peso_vertice = 0
                        print(peso_vertice)

                        # Calcula a nova distância
                        nova_distancia = distancia_atual + peso_aresta + peso_vertice

                        if nova_distancia < distancias[v2]:
                            distancias[v2] = nova_distancia
                            heapq.heappush(heap, (nova_distancia, v2))
                            # Atualiza o caminho
                            caminhos[v2] = caminhos[vertice_atual] + [v2]

            # Verifica se existem vértices desconectados (sem caminho do vértice inicial)
            for rotulo in self.rotulos:
                if rotulo is not None and distancias[rotulo] == float('inf'):
                    distancias[rotulo] = "Inacessível"
                    caminhos[rotulo] = "Inacessível"

            # Formata a saída com distâncias e caminhos
            resultado = {}
            for vertice, distancia in distancias.items():
                if distancia != "Inacessível":
                    caminho = "->".join(caminhos[vertice])
                    resultado[vertice] = f"{caminho} = {distancia}"
                else:
                    resultado[vertice] = "Inacessível"

            return resultado
        except Exception as e:
            raise RuntimeError(f"Erro ao executar o algoritmo de Dijkstra: {e}")

    def floyd_warshall(self):
        """Calcula a menor distância entre todos os pares de vértices utilizando o algoritmo de Floyd-Warshall."""
        try:
            # Verifica se o grafo foi corretamente inicializado
            if not self.matriz or not self.vertices:
                raise ValueError("O grafo não foi corretamente inicializado. Verifique os dados de entrada.")

            # Inicializa a matriz de distâncias
            distancias = [[math.inf for _ in range(self.vertices)] for _ in range(self.vertices)]

            # Preenche a matriz de distâncias com os valores das arestas
            for i in range(self.vertices):
                for j in range(self.vertices):
                    if i == j:
                        distancias[i][j] = 0
                    elif self.matriz[i][j] != 0:
                        distancias[i][j] = self.arestas.get((self.rotulos[i], self.rotulos[j]), {}).get("peso", 1)

            # Aplica o algoritmo de Floyd-Warshall
            for k in range(self.vertices):
                for i in range(self.vertices):
                    for j in range(self.vertices):
                        if distancias[i][j] > distancias[i][k] + distancias[k][j]:
                            distancias[i][j] = distancias[i][k] + distancias[k][j]

            if any(distancias[i][i] < 0 for i in range(self.vertices)):
                print("Atenção: O grafo contém ciclos negativos. Não é possível calcular distâncias mínimas.")
                return None

            # Exibe a matriz de distâncias resultante
            self.exibir_matriz_distancias(distancias)

            return distancias

        except ValueError as ve:
            print(f"Erro nos dados de entrada: {ve}")
        except RuntimeError as re:
            print(f"Erro de execução: {re}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

    def exibir_matriz_distancias(self, distancias):
        """Exibe a matriz de distâncias calculada pelo algoritmo de Floyd-Warshall."""
        print("Matriz de Distâncias Mínimas:")

        # Calcula o comprimento máximo necessário para formatar os números
        max_len = max(len(str(distancias[i][j])) for i in range(self.vertices) for j in range(self.vertices) if distancias[i][j] != float('inf'))

        # Exibe os rótulos dos vértices na primeira linha
        header = [" "] + [self.rotulos[i] if self.rotulos[i] else f"V{i}" for i in range(self.vertices)]
        header_str = "   |   ".join([h.center(max_len) for h in header])
        print(header_str)

        # Exibe a linha de separação
        print("---|---".join(["-" * max_len] * len(header)))

        # Exibe a matriz de distâncias com os rótulos dos vértices
        for i in range(self.vertices):
            rotulo = self.rotulos[i] if self.rotulos[i] else f"V{i}"
            linha = [f"{rotulo.center(max_len)}"] + [
                str(int(distancias[i][j])) if distancias[i][j] != float('inf') else "∞"
                for j in range(self.vertices)
            ]
            print("   |   ".join([str(valor).center(max_len) for valor in linha]))
            if i < self.vertices - 1:
                print("---|---".join(["-" * max_len] * len(header)))

