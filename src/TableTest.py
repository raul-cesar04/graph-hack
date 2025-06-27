import pandas as pd
import pandas.plotting as pandpl
import matplotlib.pyplot as plt
import matplotlib
import csv

class TableTest:
    def __init__(self, tData: dict, title: str):
        df = pd.DataFrame(tData)
        df.to_csv(f'{title}.csv', index=False)
        
        
        

class TableData:
    def __init__(self, vertices):
        self.passo = 0
        self.Passos = []
        self.ConjuntoS = []
        self.vertices = {}

        for v in vertices:
            self.vertices[v] = [vertices[v]]

    def step(self, conjuntoSStr: str, verticeId, currentDist: dict):
        self.Passos.append(self.passo)
        self.ConjuntoS.append(conjuntoSStr)
        
        for v in currentDist:
            self.vertices[v].append(currentDist[v])
        self.passo += 1

    def build(self):
        data = {
            'Passo': self.Passos,
            'Conjunto S': self.ConjuntoS
        }

        for v in self.vertices:
            data[v] = (self.vertices[v])[1:]

        
        return data