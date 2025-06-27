from App import App
from Graph import Graph
from TableTest import TableTest
from Dijkstra import Dijkstra
from Prim import Prim

def main():

    g = Graph()

    g.addVertices(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'])

    g.addAdjacency('a', ('b', 1))
    g.addAdjacency('a', ('c', 5))
    g.addAdjacency('a', ('d', 4))
    g.addAdjacency('a', ('e', 8))
   
    g.addAdjacency('b', ('c', 2))
    g.addAdjacency('c', ('d', 6))
    g.addAdjacency('d', ('e', 7))

    g.addAdjacency('b', ('f', 2))
    g.addAdjacency('c', ('f', 6))
    g.addAdjacency('c', ('g', 4))
    g.addAdjacency('d', ('f', 1))
    g.addAdjacency('d', ('g', 2))
    g.addAdjacency('d', ('h', 8))
    g.addAdjacency('e', ('h', 10))

    g.addAdjacency('f', ('g', 6))
    g.addAdjacency('g', ('h', 1))

    g.addAdjacency('f', ('i', 8))
    g.addAdjacency('f', ('k', 5))
    g.addAdjacency('g', ('i', 5))
    g.addAdjacency('g', ('k', 9))
    g.addAdjacency('h', ('i', 3))
    g.addAdjacency('h', ('k', 7))

    g.addAdjacency('i', ('k', 3))
    g.addAdjacency('i', ('j', 2))
    g.addAdjacency('k', ('j', 4))

    app = App(g)
    

    start = g.findVertice('a')

    dijkstraResult = Dijkstra.run(g, start)
    dijkstraResultTable = TableTest(dijkstraResult, 'G3_Dijkstra')

    primResult = Prim.run(g, start)
    primResultTable = TableTest(primResult, 'G3_Prim')

    app.start()

    
    pass

if __name__ == "__main__":
    main()