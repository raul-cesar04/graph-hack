from App import App
from Graph import Graph
from TableTest import TableTest
from Dijkstra import Dijkstra
from Prim import Prim

def main():

    g = Graph()

    g.addVertices(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'])

    g.addAdjacency('a', ('b', 2))
    g.addAdjacency('a', ('c', 8))
    g.addAdjacency('a', ('k', 1))

    g.addAdjacency('b', ('c', 6))
    g.addAdjacency('b', ('d', 1))

    g.addAdjacency('c', ('d', 5))
    g.addAdjacency('c', ('e', 1))
    g.addAdjacency('c', ('f', 2))
    g.addAdjacency('c', ('k', 7))

    g.addAdjacency('k', ('f', 9))

    g.addAdjacency('f', ('e', 4))
    g.addAdjacency('f', ('h', 3))
    g.addAdjacency('f', ('i', 1))

    g.addAdjacency('e', ('h', 6))
    g.addAdjacency('e', ('d', 3))

    g.addAdjacency('d', ('g', 2))
    g.addAdjacency('d', ('h', 9))

    g.addAdjacency('g', ('h', 7))
    g.addAdjacency('g', ('j', 9))
    g.addAdjacency('h', ('j', 2))
    g.addAdjacency('h', ('i', 1))
    g.addAdjacency('i', ('j', 4))

    app = App(g)
    

    start = g.findVertice('a')

    dijkstraResult = Dijkstra.run(g, start)
    dijkstraResultTable = TableTest(dijkstraResult, 'G1_Dijkstra')

    primResult = Prim.run(g, start)
    primResultTable = TableTest(primResult, 'G1_Prim')

    app.start()

    
    pass

if __name__ == "__main__":
    main()