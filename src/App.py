from tkinter import *
from tkinter import ttk
from Graph import Graph
import math

class App:
    def __init__(self, graph: Graph):
        # Data
        self.graph = graph

        # Application
        self.root = Tk()
        self.frame = ttk.Frame(self.root, padding=10)
        self.frame.grid()
        self.canvas = Canvas(self.root, width=640, height=480, bg='white')
        self.canvas.grid()

    def generate_render_info(self)->list:
        render_info_vertices = []
        render_info_edges = []
        size = len(self.graph.vertices)
        angle_step = math.radians(int(360/size))
        center_x = 320
        center_y = 240
        distance = 8*size

        poses = {}

        for i in range(size):
            obj = {}
            obj['x'] = center_x + (distance * math.cos(angle_step*i))
            obj['y'] = center_y + (distance * math.sin(angle_step*i))
            v = self.graph.vertices[i]
            obj['id'] = v.id
            
            poses[v.id] = (obj['x'], obj['y'])
            render_info_vertices.append(obj)

        for i in range(len(self.graph.adjacencies)):
            ad = self.graph.adjacencies[i]
            (v1, v2, w) = ad
            pos_1 = poses[v1]
            pos_2 = poses[v2]

            render_info_edges.append(
                {
                    "x0": pos_1[0],
                    "y0": pos_1[1],
                    "x1": pos_2[0],
                    "y1": pos_2[1],
                    "w": w
                }
            )

        return (render_info_vertices, render_info_edges)
    def start(self):
        (self.render_info_vertices, self.render_info_edges) = self.generate_render_info() 
        self.update()
        self.root.mainloop()

    def update(self):
        self.canvas.delete('all')


        for e in self.render_info_edges:
            x0 = e['x0']
            x1 = e['x1']
            y0 = e['y0']
            y1 = e['y1']
            w  = e['w']

            tx = x0 + (x1 - x0)/2
            ty = y0 + (y1 - y0)/2
            
            self.canvas.create_line(x0, y0, x1, y1) 
            self.canvas.create_text(tx, ty, text=w)

        for o in self.render_info_vertices:
            oval_size = 24
            x = o['x']
            y = o['y']
            id = o['id']
            self.canvas.create_oval(x - (oval_size/2), y-(oval_size/2), x+(oval_size/2), y+(oval_size/2), fill='white')
            self.canvas.create_text(x, y, text=id)
        self.root.after(1, self.update)

