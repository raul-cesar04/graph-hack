from Graph import Graph
class Dijkstra:
    def getMinDist(vertices: dict, queue: list):
        minDist, minKey = None, None
        for v in vertices:
            if(v not in queue):
                continue
            if minKey == None or vertices[v] < minDist:
                minKey = v
                minDist = vertices[v]

        return (minKey, minDist)
    def run(g: Graph, s: Graph.Vertice)->None:
        dist = {}
        S = []
        Q = []

        for v in g.vertices:
            dist[v.id] = float('inf')
            Q.append(v.id)

        dist[s.id] = 0  

        
        print('Le queue: ',Q)
        while len(Q) > 0:
            minKey, minDist = Dijkstra.getMinDist(dist, Q)
            S.append(minKey)
            Q.remove(minKey)

            current = g.findVertice(minKey)
            for v in current.neighbours:
                vDist, vData = v
                if(dist[vData.id] > dist[current.id] + vDist):
                    dist[vData.id] = dist[current.id] + vDist
            
        print('Final S: ',S)