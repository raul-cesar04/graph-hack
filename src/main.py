from App import App
from Graph import Graph
from TableTest import TableTest
from Dijkstra import Dijkstra
import threading

def main():

    g = Graph()

    g.addVertices(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])

    g.addAdjacency('a', ('b', 3))
    g.addAdjacency('a', ('c', 9))
    g.addAdjacency('a', ('d', 2))

    g.addAdjacency('b', ('c', 4))
    g.addAdjacency('c', ('d', 6))
    g.addAdjacency('c', ('e', 1))
    g.addAdjacency('c', ('f', 2))
    g.addAdjacency('b', ('e', 5))
    g.addAdjacency('g', ('d', 9))
    g.addAdjacency('f', ('g', 1))
    g.addAdjacency('f', ('h', 5))
    g.addAdjacency('e', ('h', 5))
    g.addAdjacency('h', ('j', 5))
    g.addAdjacency('f', ('j', 9))
    g.addAdjacency('f', ('i', 6))
    g.addAdjacency('g', ('i', 2))
    g.addAdjacency('i', ('j', 3))



    app = App(g)
    

    start = g.findVertice('a')
    tData = Dijkstra.run(g, start)
    TableTest(tData)
    app.start()

    
    pass

if __name__ == "__main__":
    main()