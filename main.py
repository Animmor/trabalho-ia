from graph.main import Graph
from search_algorithms.main import SearchAlgorithms

g = Graph()

# cria um novo grafo exemplo, com seus nós e vertices
g.addEdge("A", "B") 
g.addEdge("A", "D") 
g.addEdge("B", "A") 
g.addEdge("B", "C") 
g.addEdge("C", "B") 
g.addEdge("D", "A") 
g.addEdge("D", "E") 
g.addEdge("D", "F") 
g.addEdge("E", "D") 
g.addEdge("E", "F") 
g.addEdge("E", "G") 
g.addEdge("F", "D") 
g.addEdge("F", "E") 
g.addEdge("F", "H") 
g.addEdge("G", "E") 
g.addEdge("G", "H") 
g.addEdge("H", "G") 
g.addEdge("H", "F")

# cria um novo grafo exemplo cidade, com seus nós e vertices
# g.addEdge("Cuiaba", "Campo Grande") 
# g.addEdge("Campo Grande", "Sao Paulo") 
# g.addEdge("Campo Grande", "Brasilia") 
# g.addEdge("Campo Grande", "Cuiaba") 
# g.addEdge("Sao Paulo", "Rio de Janeiro") 
# g.addEdge("Sao Paulo", "Brasilia") 
# g.addEdge("Sao Paulo", "Campo Grande") 
# g.addEdge("Rio de Janeiro", "Sao Paulo") 
# g.addEdge("Rio de Janeiro", "Brasilia")
# g.addEdge("Brasilia", "Rio de Janeiro")
# g.addEdge("Brasilia", "Sao Paulo")
# g.addEdge("Brasilia", "Campo Grande")

searchAgent = SearchAlgorithms(g.graph)

searchAgent.breadthFirst("A")
searchAgent.depthFirst("A")

# searchAgent.breadthFirst("Rio de Janeiro")
# searchAgent.depthFirst("Rio de Janeiro")