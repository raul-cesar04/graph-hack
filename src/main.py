from App import App
from Graph import Graph

def main():
    g = Graph()
    g.addVertices(['A', 'B', 'C', 'D', 'E'])

    g.addAdjacency('A', ('B', 3))
    g.addAdjacency('A', ('C', 2))
    g.addAdjacency('A', ('D', 8))

    g.addAdjacency('D', ('C', 4))
    g.addAdjacency('D', ('B', 7))

    g.addAdjacency('E', ('D', 6))
    g.addAdjacency('E', ('C', 9))

    app = App(g)

    app.start()
    pass

if __name__ == "__main__":
    main()