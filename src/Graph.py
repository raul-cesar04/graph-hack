class Graph:
    class Vertice:
        def __init__(self, id: str):
            self.neighbours = []
            self.id = id
            
        def addNeighbour(self, neighbour, weight: int)->None:
            self.neighbours.append((
                weight, neighbour
            ))

    def __init__(self):
        self.vertices: list[Graph.Vertice] = []
        self.adjacencies: list[tuple[int, int, int]] = []

    def addVertices(self, vertices: list[str])->None:
        for v in vertices:
            self.vertices.append(Graph.Vertice(v))

    def findVertice(self, id: str) -> Vertice:
        filtered = list(filter(lambda x: x.id == id, self.vertices))
        
        if(len(filtered) == 0): return None

        return filtered[0]
    def addAdjacency(self, id: str, adjacency: tuple[str, int]):
        v = self.findVertice(id)

        if(v == None): 
            print('Failure in adding adjacencies. No such vertice: ',id)
            return
        
    
        (neighbourId, w) = adjacency
        newNeighbour = self.findVertice(neighbourId)
        
        if(newNeighbour == None):
            print('Deu erro aqui')
            return

        v.addNeighbour(newNeighbour, w)
        newNeighbour.addNeighbour(v, w)
        self.adjacencies.append((newNeighbour.id, v.id, w))

            
    pass