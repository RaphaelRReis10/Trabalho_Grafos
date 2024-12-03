from matriz_adjacencia import MatrizAdjacencia
from lista_adjacencia import ListaAdjacencia
import desenhar
import random


# Menu inicial
def main_menu():
    global matriz, lista
    print("Bem-vindo ao trabalho sobre grafos!")
    print("Escolha uma das opções abaixo:")
    print("1. Determinar o número de vértices do grafo")
    print("2. Criar um grafo aleatório com 9 vértices e 12 arestas")

    try:
        opcao = int(input("Digite o número da sua escolha: "))
    except ValueError:
        print("Erro: Por favor, digite um número válido.")
        main_menu()
        return

    if opcao == 1:
        try:
            vertices = int(input("Digite o número de vértices: "))
            if vertices <= 0:
                raise ValueError("O número de vértices deve ser maior que zero.")
        except ValueError as e:
            print(f"Erro: {e}")
            main_menu()
            return

        matriz = MatrizAdjacencia(vertices)
        lista = ListaAdjacencia(vertices)

        print(f"Grafo com {vertices} vértices criado em ambas as representações (Matriz e Lista).")
        graph_menu()

    elif opcao == 2:
        vertices = 5
        matriz = MatrizAdjacencia(vertices)
        lista = ListaAdjacencia(vertices)

        criar_grafo_aleatorio(matriz, lista)
        graph_menu()
    else:
        print("Opção inválida. Tente novamente.")
        main_menu()

# Função para criar um grafo aleatório
def criar_grafo_aleatorio(matriz, lista):
    vertices = ["A", "B", "C", "D", "E"]  # Lista de vértices para o grafo
    arestas = 6  # Número fixo de arestas para o grafo aleatório
    aux = 0

    print(f"Criando um grafo aleatório com {len(vertices)} vértices e {arestas} arestas...")
    
    # Rotular todos os vértices
    for vertice in range(matriz.vertices):
        rotulo = vertices[aux]
        matriz.rotular_vertice(vertice, rotulo)
        lista.rotular_vertice(vertice, rotulo)
        aux += 1

    # Gerar as arestas aleatórias
    for _ in range(arestas):
        rotulo1 = random.choice(vertices)  # Escolhe um rótulo aleatório
        rotulo2 = random.choice(vertices)  # Escolhe outro rótulo aleatório
        while rotulo1 == rotulo2:  # Evita laços (arestas de um vértice para ele mesmo)
            rotulo2 = random.choice(vertices)

        # Rotulação das arestas conforme os vértices adjacentes (exemplo: 'AB')
        rotulo_aresta = rotulo1 + rotulo2
        
        # Atribuindo uma ponderação aleatória para a aresta (por exemplo, entre 1 e 10)
        peso = random.randint(1, 10)

        try:
            # Adiciona a aresta ao grafo (na matriz e na lista)
            matriz.adicionar_aresta(rotulo1, rotulo2)
            lista.adicionar_aresta(rotulo1, rotulo2)

            matriz.rotular_aresta(rotulo1, rotulo2, rotulo_aresta)
            lista.rotular_aresta(rotulo1, rotulo2, rotulo_aresta)


            matriz.ponderar_aresta(rotulo1, rotulo2, peso)
            lista.ponderar_aresta(rotulo1, rotulo2, peso)


            

            print(f"Aresta {rotulo_aresta} com peso {peso} adicionada entre '{rotulo1}' e '{rotulo2}'.")
        except ValueError as e:
            print(f"Erro: {e}")

# Menu principal
def graph_menu():
    while True:
        print("\nEscolha uma das opções abaixo:")
        print("1 - Opções de Vértices")
        print("2 - Opções de Arestas")
        print("3 - Opções de Visualização")
        print("4 - Opções de Checagem")
        print("0 - Encerrar Programa")
        choice = input("Digite sua escolha: ")

        if choice == "1":
            vertices_menu()
        elif choice == "2":
            arestas_menu()
        elif choice == "3":
            Visualizacao_menu()
        elif choice == "4":
            Checagem_menu()
        elif choice == "0":
            print("Tem certeza que quer sair?")
            opcao = input("Escreva: S/N: ")
            if opcao.lower() == "s":
                print("Saindo do programa. Até mais!")
                break
            elif opcao.lower() == "n":
                print("Retornando ao menu Principal!")
            else:
                print("Opção inválida. Tente novamente.")
        else:
            print("Opção inválida, Tente novamente.")

# Menu de vértices
def vertices_menu():
    while True:
        print("\nSubmenu - Opções de Vértices")
        print("1 - Ponderação e Rotulação de Vértices")
        print("2 - Inserção e Remoção de Vértices")
        print("0 - Voltar ao Menu Principal")
        choice = input("Digite sua escolha: ")

        if choice == "1":
            prv_menu()
        elif choice == "2":
            IRV_menu()
        elif choice == "0":
            print("Voltando ao menu principal...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Menu de arestas
def arestas_menu():
    while True:
        print("\nSubmenu - Opções de Arestas")
        print("1 - Inserção e Remoção de Arestas")
        print("2 - Ponderação e Rotulação de Arestas")
        print("0 - Voltar ao Menu Principal")
        choice = input("Digite sua escolha: ")

        if choice == "1":
            IRA_menu()  # Submenu de inserção e remoção de arestas
        elif choice == "2":
            PRA_menu()  # Submenu de ponderação e rotulação de arestas
        elif choice == "0":
            print("Voltando ao menu principal...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Submenu de inserção e remoção de vertices
def IRV_menu():
    while True:
        print("\nSubmenu - Inserção e Remoção de Vértices")
        print("1 - Adicionar Vértice")
        print("2 - Remover Vértice")
        print("0 - Voltar ao Menu de vértices")
        choice = input("Digite sua escolha: ")

        if choice == "1":
            try:
                rotulo = input("Digite o rótulo do novo vértice: ")
                if rotulo in lista.vertices_rotulados():
                    raise ValueError(f"Já existe um vértice com o rótulo '{rotulo}'.")
                lista.adicionar_vertice(rotulo)
                matriz.adicionar_vertice(rotulo)
                print(f"Vértice '{rotulo}' adicionado com sucesso!")
            except ValueError as e:
                print(f"Erro: {e}")
        elif choice == "2":
            try:
                rotulo = input("Digite o rótulo do vértice a ser removido: ")
                lista.remover_vertice(rotulo)
                matriz.remover_vertice(rotulo)
                print(f"Vértice '{rotulo}' removido com sucesso!")
            except ValueError as e:
                print(f"Erro: {e}")
        elif choice == "0":
            print("Voltando ao menu principal...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Submenu de inserção e remoção de arestas
def IRA_menu():
    while True:
        print("\nMenu de inserção e remoção de arestas")
        print("1 - Inserir aresta")
        print("2 - Remover aresta")
        print("0 - Voltar ao menu de arestas")
        choice = input("Digite sua escolha: ")

        if choice == "1":
            rotulo1 = input("Digite o rótulo do primeiro vértice: ")
            rotulo2 = input("Digite o rótulo do segundo vértice: ")
            try:
                matriz.adicionar_aresta(rotulo1, rotulo2)
                lista.adicionar_aresta(rotulo1, rotulo2)
                print(f"Aresta adicionada entre '{rotulo1}' e '{rotulo2}'.")
            except ValueError as e:
                print(f"Erro: {e}")
        elif choice == "2":
            rotulo1 = input("Digite o rótulo do primeiro vértice: ")
            rotulo2 = input("Digite o rótulo do segundo vértice: ")
            try:
                matriz.remover_aresta(rotulo1, rotulo2)  # Remoção na matriz de adjacência
                lista.remover_aresta(rotulo1, rotulo2)  # Remoção na lista de adjacência
                print(f"Aresta removida entre '{rotulo1}' e '{rotulo2}'.")
            except ValueError as e:
                print(f"Erro: {e}")
        elif choice == "0":
            print("Voltando ao menu principal...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Submenu de ponderação e rotulação de vértices
def prv_menu():
    while True:
        print("\nSubmenu de ponderação e rotulação de vértices:")
        print("1 - Rotular um único vértice")
        print("2 - Ponderar um único vértice")
        print("3 - Rotular todos os vértices")
        print("4 - Ponderar todos os vértices")
        print("0 - Voltar ao menu de vértices")
        choice = input("Digite sua escolha: ")

        if choice == "1":
            # Rotular um único vértice
            while True:
                try:
                    vertice = int(input(f"Digite o número do vértice (0 a {matriz.vertices - 1}): "))
                    if vertice < 0 or vertice >= matriz.vertices:
                        print(f"Erro: O número do vértice deve estar entre 0 e {matriz.vertices - 1}. Tente novamente.")
                        continue
                    break  # Sai do loop se o valor for válido
                except ValueError:
                    print("Erro: Digite um número inteiro válido para o vértice.")
            
            rotulo = input("Digite o rótulo para o vértice: ")
            matriz.rotular_vertice(vertice, rotulo)
            lista.rotular_vertice(vertice, rotulo)
            print(f"Vértice {vertice} rotulado como '{rotulo}'.")
        elif choice == "2":
            # Ponderar um único vértice
            while True:
                try:
                    vertice = int(input(f"Digite o número do vértice (0 a {matriz.vertices - 1}): "))
                    if vertice < 0 or vertice >= matriz.vertices:
                        print(f"Erro: O número do vértice deve estar entre 0 e {matriz.vertices - 1}. Tente novamente.")
                        continue
                    break  # Sai do loop se o valor for válido
                except ValueError:
                    print("Erro: Digite um número inteiro válido para o vértice.")
            
            while True:
                try:
                    peso = int(input("Digite o peso para o vértice (um número inteiro): "))
                    break  # Sai do loop se o valor for um número válido
                except ValueError:
                    print("Erro: Digite um número inteiro válido para o peso.")
            
            matriz.ponderar_vertice(vertice, peso)
            lista.ponderar_vertice(vertice, peso)
            print(f"Peso {peso} atribuído ao vértice {vertice}.")
        elif choice == "3":
            # Rotular todos os vértices
            for vertice in range(matriz.vertices):
                rotulo = input(f"Digite o rótulo para o vértice {vertice}: ")
                matriz.rotular_vertice(vertice, rotulo)
                lista.rotular_vertice(vertice, rotulo)
            print("Todos os vértices foram rotulados.")
        elif choice == "4":
            # Ponderar todos os vértices
            for vertice in range(matriz.vertices):
                while True:
                    try:
                        peso = int(input(f"Digite o peso para o vértice {vertice} (um número inteiro): "))
                        break  # Sai do loop se o valor for um número válido
                    except ValueError:
                        print("Erro: Digite um número inteiro válido para o peso.")
                matriz.ponderar_vertice(vertice, peso)
                lista.ponderar_vertice(vertice, peso)
            print("Todos os vértices foram ponderados.")
        elif choice == "0":
            print("Voltando ao menu principal...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Submenu de ponderação e rotulação de arestas
def PRA_menu():
    while True:
        print("\nSubmenu de rotulação e ponderação de arestas:")
        print("1 - Rotular uma única aresta")
        print("2 - Ponderar uma única aresta")
        print("3 - Rotular todas as arestas")
        print("4 - Ponderar todas as arestas")
        print("0 - Voltar ao menu de arestas")
        choice = input("Digite sua escolha: ")

        if choice == "1":
            # Rotular uma única aresta
            try:
                rotulo1 = input("Digite o rótulo do primeiro vértice: ")
                rotulo2 = input("Digite o rótulo do segundo vértice: ")
                
                if not matriz.existe_aresta(rotulo1, rotulo2):
                    print(f"Erro: Não existe aresta entre '{rotulo1}' e '{rotulo2}'.")
                    continue
                
                rotulo_aresta = input("Digite o rótulo para a aresta: ")
                matriz.rotular_aresta(rotulo1, rotulo2, rotulo_aresta)
                lista.rotular_aresta(rotulo1, rotulo2, rotulo_aresta)
                print(f"Aresta entre '{rotulo1}' e '{rotulo2}' rotulada como '{rotulo_aresta}'.")
            except Exception as e:
                print(f"Erro ao rotular a aresta: {e}")
        
        elif choice == "2":
            # Ponderar uma única aresta
            try:
                rotulo1 = input("Digite o rótulo do primeiro vértice: ")
                rotulo2 = input("Digite o rótulo do segundo vértice: ")
                
                if not matriz.existe_aresta(rotulo1, rotulo2):
                    print(f"Erro: Não existe aresta entre '{rotulo1}' e '{rotulo2}'.")
                    continue
                
                while True:
                    try:
                        peso = int(input("Digite o peso para a aresta (um número inteiro): "))
                        break
                    except ValueError:
                        print("Erro: Digite um número inteiro válido para o peso.")
                
                matriz.ponderar_aresta(rotulo1, rotulo2, peso)
                lista.ponderar_aresta(rotulo1, rotulo2, peso)
                print(f"Peso {peso} atribuído à aresta entre '{rotulo1}' e '{rotulo2}'.")
            except Exception as e:
                print(f"Erro ao ponderar a aresta: {e}")
        
        elif choice == "3":
            # Rotular todas as arestas
            try:
                for aresta in matriz.get_arestas():
                    rotulo1, rotulo2 = aresta
                    rotulo_aresta = input(f"Digite o rótulo para a aresta entre '{rotulo1}' e '{rotulo2}': ")
                    matriz.rotular_aresta(rotulo1, rotulo2, rotulo_aresta)
                    lista.rotular_aresta(rotulo1, rotulo2, rotulo_aresta)
                print("Todas as arestas foram rotuladas.")
            except Exception as e:
                print(f"Erro ao rotular todas as arestas: {e}")
        
        elif choice == "4":
            # Ponderar todas as arestas
            try:
                for aresta in matriz.get_arestas():
                    rotulo1, rotulo2 = aresta
                    while True:
                        try:
                            peso = int(input(f"Digite o peso para a aresta entre '{rotulo1}' e '{rotulo2}' (um número inteiro): "))
                            break
                        except ValueError:
                            print("Erro: Digite um número inteiro válido para o peso.")
                    matriz.ponderar_aresta(rotulo1, rotulo2, peso)
                    lista.ponderar_aresta(rotulo1, rotulo2, peso)
                print("Todas as arestas foram ponderadas.")
            except Exception as e:
                print(f"Erro ao ponderar todas as arestas: {e}")
        
        elif choice == "0":
            print("Voltando ao menu principal...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

# Menu de visualização
def Visualizacao_menu():
    while True:
        print("\nEscolha uma das opções abaixo:")
        print("1 - Visualizar grafo")
        print("2 - Representação pela matriz de adjacência")
        print("3 - Representação pela lista de adjacência")
        print("4 - Representação das arestas (Rótulo e Ponderação)")
        print("0 - Voltar ao menu principal")
        choice = input("Digite sua escolha: ")

        if choice == "1":
            # Visualizar grafo pela matriz
            desenhar.desenhar_grafo(matriz.matriz, matriz.rotulos, matriz.pesos_vertices, matriz.arestas)
        if choice == "2":
            matriz.exibir()
        if choice == "3":
            lista.exibir()
        if choice == "4":
            matriz.exibir_todas_arestas()
        if choice == "0":
            print("Voltando ao menu principal...")
            break

# Função para exibir o menu de checagens
def Checagem_menu():
    while True:
        print("\nMenu de Checagem de Grafo:")
        print("1 - Adjacência entre vértices")
        print("2 - Vizinhança do vértice")
        print("3 - Grau do vértice")
        print("4 - Grafo completo")
        print("5 - Grafo Regular")
        print("6 - Grafo conexo")
        print("7 - Grafo acíclico")
        print("8 - Grafo Euleriano")
        print("9 - Busca em profundidade")
        print("10 - Busca em largura")
        print("11 - Calcular a menor distância de uma origem para todos os outros vértices (Dijkstra)")
        print("12 - Calcular a menor distância de todos para todos (Floyd-Warshall)")
        print("0 - Voltar ao menu principal")
        
        choice = input("Digite sua escolha: ")

        if choice == "1":
            # Verificar adjacência entre vértices
            vertice1 = input("Digite o primeiro vértice: ")
            vertice2 = input("Digite o segundo vértice: ")
            try:
                if verifica_adjacencia(vertice1, vertice2):
                    print(f"Existe uma aresta entre os vértices {vertice1} e {vertice2}.")
                else:
                    print(f"Não existe aresta entre os vértices {vertice1} e {vertice2}.")
            except Exception as e:
                print(f"Erro ao verificar adjacência: {e}")

        elif choice == "2":
            # Verificar vizinhança do vértice
            vertice = input("Digite o vértice: ").strip()
            try:
                vizinhos = vizinhança(vertice)
                if not vizinhos:
                    print(f"O vértice '{vertice}' não existe ou não possui vizinhos.")
                else:
                    print(f"Vizinhança do vértice {vertice}: {vizinhos}")
            except Exception as e:
                print(f"Erro ao verificar vizinhança: {e}")
        
        elif choice == "3":
            # Grau do vértice
            vertice = input("Digite o vértice: ").strip()
            try:
                grau = grau_vertice(vertice)
                if grau is not None:
                    print(f"O grau do vértice {vertice} é {grau}.")
                else:
                    print(f"O vértice '{vertice}' não está no grafo.")
            except Exception as e:
                print(f"Erro ao calcular o grau: {e}")
        
        elif choice == "4":
            # Grafo completo
            try:
                if grafo_completo():
                    print("O grafo é completo.")
                else:
                    print("O grafo não é completo.")
            except Exception as e:
                print(f"Erro ao verificar se o grafo é completo: {e}")
        
        elif choice == "5":
            # Grafo regular
            try:
                if grafo_regular():
                    print("O grafo é regular.")
                else:
                    print("O grafo não é regular.")
            except Exception as e:
                print(f"Erro ao verificar se o grafo é regular: {e}")
        
        elif choice == "6":
            # Grafo conexo
            try:
                if grafo_conexo():
                    print("O grafo é conexo.")
                else:
                    print("O grafo não é conexo.")
            except Exception as e:
                print(f"Erro ao verificar se o grafo é conexo: {e}")
        
        elif choice == "7":
            # Grafo acíclico
            try:
                if grafo_aciclico():
                    print("O grafo é Cíclico.")
                else:
                    print("O grafo é Acíclico.")
            except Exception as e:
                print(f"Erro ao verificar se o grafo é acíclico: {e}")
        
        elif choice == "8":
            # Grafo Euleriano
            try:
                if grafo_euleriano():
                    print("O grafo é euleriano.")
                else:
                    print("O grafo não é euleriano.")
            except Exception as e:
                print(f"Erro ao verificar se o grafo é euleriano: {e}")
        
        elif choice == "9":
            # Busca em profundidade
            vertice_inicial = input("Digite o vértice inicial: ").strip()
            try:
                resultado = busca_profundidade(vertice_inicial)
                print(f"Resultado da busca em profundidade: {resultado}")
            except Exception as e:
                print(f"Erro na busca em profundidade: {e}")
        
        elif choice == "10":
            # Busca em largura
            vertice_inicial = input("Digite o vértice inicial: ").strip()
            try:
                resultado = busca_largura(vertice_inicial)
                print(f"Resultado da busca em largura: {resultado}")
            except Exception as e:
                print(f"Erro na busca em largura: {e}")
        
        elif choice == "11":
            # Dijkstra
            origem = input("Digite o vértice de origem: ").strip()
            try:
                distancias = dijkstra(origem)
                print("Menor distância de cada vértice:")
                for destino, distancia in distancias.items():
                    print(f"{origem} -> {destino}: {distancia}")
            except Exception as e:
                print(f"Erro ao executar Dijkstra: {e}")
        
        elif choice == "12":
            # Floyd-Warshall
            try:
                floyd_warshall()
            except Exception as e:
                print(f"Erro ao executar Floyd-Warshall: {e}")
        
        elif choice == "0":
            print("Voltando ao menu principal...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Verifica a adjacencia entre vertices
def verifica_adjacencia(vertice1, vertice2):
    "Verifica se existe uma aresta entre os vértices vertice1 e vertice2"
    return matriz.existe_aresta(vertice1, vertice2)

# Mostra todos os vizinhos do vertice
def vizinhança(vertice):
    "Retorna os vértices vizinhos de um vértice."
    vizinhos = matriz.vizinhos(vertice)
    if vizinhos is None:  # Caso o vértice não exista
        return []
    return vizinhos

# mostra o grau do vertice
def grau_vertice(vertice):
    """Retorna o grau de um vértice ou None se o vértice não existir."""
    return matriz.grau_vertice(vertice)

# Verifica se o grafo é completo
def grafo_completo():
    "Verifica se o grafo é completo. Retorna True, False ou None em caso de erro."
    return matriz.eh_completo()

# Verifica se o grafo é regular (todos os vértices têm o mesmo grau)
def grafo_regular():
    "Verifica se o grafo é regular (todos os vértices têm o mesmo grau)"
    return matriz.eh_regular()

# Verifica se o grafo é conexo
def grafo_conexo():
    "Verifica se o grafo é conexo"
    return matriz.eh_conexo()

# Verifica se o grafo possui ciclo 
def grafo_aciclico():
    "Verifica se o grafo é acíclico"
    return matriz.eh_ciclico()

# Verifica se o grafo é euleriano
def grafo_euleriano():
    "Verifica se o grafo é euleriano"
    return matriz.eh_euleriano()

# Executa uma busca em profundidade no grafo a partir do vértice inicial
def busca_profundidade(vertice_inicial):
    "Executa uma busca em profundidade no grafo a partir do vértice inicial"
    return matriz.busca_em_profundidade(vertice_inicial)

# Executa uma busca em largura no grafo a partir do vértice inicial
def busca_largura(vertice_inicial):
    "Executa uma busca em largura no grafo a partir do vértice inicial"
    return matriz.busca_em_largura(vertice_inicial)

# Calcula a menor distância de todos os vértices para o vértice origem (Algoritmo de Dijkstra)
def dijkstra(origem):
    "Calcula a menor distância de todos os vértices para o vértice origem (Algoritmo de Dijkstra)"
    return matriz.dijkstra(origem)

# Calcula a menor distância de todos para todos (Floyd-Warshall)
def floyd_warshall():
    "Calcula a menor distância de todos para todos (Floyd-Warshall)"
    return matriz.floyd_warshall()

if __name__ == "__main__":
    main_menu()