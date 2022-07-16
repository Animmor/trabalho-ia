class SearchAlgorithms:
  def __init__(self, graph):
    self.graph = graph
    self.color = {}
    self.parent = {}
    self.level = {}
    self.queue = []
    self.stack = []

  def initializeSearch(self):
    # inicializa as variáveis
    for node in self.graph.keys():
      self.color[node] = 'black'
      self.parent[node] = None
      self.level[node] = -1

  def breadthFirst(self, value):
    # Nós visitados: red
    # Nós não visitados: black
    self.initializeSearch()
    output = []
    self.color[value] = 'red'
    self.level[value] = 0
    self.queue.insert(0, value)

    while self.queue: # enquanto a fila não estiver vazia
      currentVertex = self.queue.pop()
      output.append(currentVertex)

      for neighbour in self.graph[currentVertex]: # percorre todos os vizinhos desse nó atual
        if(self.color[neighbour] == 'black'):
          self.color[neighbour] = 'red'
          self.parent[neighbour] = currentVertex 
          self.level[neighbour] = self.level[currentVertex] + 1
          self.queue.insert(0, neighbour) # coloco na fila
        
    print('\nBusca em largura')
    print(f'Caminho percorrido comecando por {value}: {output}')
    print(f'Distancia entre os nós baseado no nó {value}: {self.level}')

  def depthFirst(self, value):
    self.initializeSearch()
    output = []
    self.color[value] = 'red'
    self.stack.append(value)

    while self.stack: # enquanto a pilha não estiver vazia
      currentVertex = self.stack.pop()
      output.append(currentVertex)

      for neighbour in self.graph[currentVertex]: # percorre todos os vizinhos desse nó atual

        if(self.color[neighbour] == 'black'):
          self.color[neighbour] = 'red'
          self.stack.append(neighbour) # coloco na pilha

    print('\nBusca em profundidade')
    print(f'Caminho percorrido comecando por {value}: {output}')
