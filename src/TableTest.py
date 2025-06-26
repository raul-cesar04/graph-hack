import pandas as pd
import pandas.plotting as pandpl
import matplotlib.pyplot as plt
import matplotlib
import csv

class TableTest:
    def __init__(self, tData: dict):
        df = pd.DataFrame(tData)
        df.to_csv('my_file.csv', index=False)
        # fix, ax = plt.subplots(figsize=(6,2), sharex=True, sharey=True)
        # ax.axis('off')
        # plt.title("Algoritmo: Dijkstra - Grafo G2")
        # table = ax.table(cellText=df.values, colLabels=df.keys(), loc='center')
        # table.auto_set_font_size(False)
        # table.set_fontsize(6)
        # table.scale(1.5, 1)
        # plt.show()
        
        

class TableData:
    def __init__(self, vertices):
        self.passo = 0
        self.Passos = []
        self.ConjuntoS = []
        self.vertices = {}

        for v in vertices:
            self.vertices[v.id] = []

    def step(self, conjuntoSStr: str, verticeId, currentDist: float):
        self.Passos.append(self.passo)
        self.ConjuntoS.append(conjuntoSStr)
        # if(not hasattr(self.vertices, verticeId)):
        #     self.vertices[verticeId] = []
        
        self.vertices[verticeId].append(currentDist)
        self.passo += 1

    def build(self):
        data = {
            'Passo': self.Passos,
            'Conjunto S': self.ConjuntoS
        }

        for v in self.vertices:
            data[v] = [0]*len(data['Passo'])

        
        return data