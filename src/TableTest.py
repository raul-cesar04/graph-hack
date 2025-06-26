import pandas as pd
import pandas.plotting as pandpl
import matplotlib.pyplot as plt

class TableTest:
    def __init__(self):
        data = {
            "Passo": [0, 1, 2, 3, 4, 5, 6],
            "Conjunto S": ['', 'A', 'A, B', 'A, B, C', 'A, B, C, D', 'A, B, C, D, E', 'A, B, C, D, E, F'],
            "City": ["New York", "London", "Paris", "New York", "London", "Paris", 'OENIS']
        }
        df = pd.DataFrame(data)
        fix, ax = plt.subplots(1,1)
        ax.axis('off')
        plt.title("Algoritmo: Dijkstra - Grafo G2")
        ax.table(cellText=df.values, colLabels=df.keys(), loc='center')

        plt.show()
        pass