from tkinter import *
from enum import Enum
from collections import defaultdict
import time


class CursorMode(Enum):
    NO_STATE = 1
    C_D_State = 2
    V_STATE = 3
    W_STATE = 4


class Tiles(Frame):
    def __init__(self, parent, control):
        Frame.__init__(self, parent)

        self.ROWS = 3
        self.COLS = 3
        self.graph = defaultdict(list)

        self.columnconfigure(tuple(range(self.ROWS)), weight=1)
        self.rowconfigure(tuple(range(self.COLS)), weight=1)

        self.cursorMode = CursorMode.NO_STATE

        self.controller = control
        self.lock = False
        self.VacuumTile = 0
        self.dirtTile = 7
        # Assets============================================
        self.Tile_Clean = PhotoImage(
            file=r"C:\Users\camro\Documents\Development\Python Projects\Vacuum World\Assets\TileClean.png")
        self.Tile_Dirty = PhotoImage(
            file=r"C:\Users\camro\Documents\Development\Python Projects\Vacuum World\Assets\TileDirty.png")
        self.Vacuum_Clean = PhotoImage(
            file=r"C:\Users\camro\Documents\Development\Python Projects\Vacuum World\Assets\VacuumClean.png")
        self.Vacuum_dirty = PhotoImage(
            file=r"C:\Users\camro\Documents\Development\Python Projects\Vacuum World\Assets\VaccumDirty.png")
        self.Wall = PhotoImage(
            file=r"C:\Users\camro\Documents\Development\Python Projects\Vacuum World\Assets\Wall.png")
        # ===================================================

        # Generate Tiles=====================================
        self.tiles = []
        i = 0
        for x in range(self.ROWS):
            for y in range(self.COLS):
                self.tiles.append(
                    Button(self,  image=self.Tile_Clean, text="clean", font=('Arial', 18),  bg="#eeeee4", borderwidth=1, command=lambda x=i: self.changeTileState(x)))
                self.tiles[i].grid(column=y, row=x, sticky="news")
                self.tiles[i].image = self.Tile_Clean
                i += 1
        self.tiles[self.VacuumTile]['image'] = self.Vacuum_Clean
        self.tiles[self.VacuumTile]['text'] = "vacuum"

        self.tiles[self.dirtTile]['image'] = self.Tile_Dirty
        self.tiles[self.dirtTile]['text'] = "dirty"
        # ====================================================

        # generate search graph================================
        self.addEdge(self.graph, 0, 1)
        self.addEdge(self.graph, 0, 3)

        self.addEdge(self.graph, 1, 0)
        self.addEdge(self.graph, 1, 2)
        self.addEdge(self.graph, 1, 4)

        self.addEdge(self.graph, 2, 1)
        self.addEdge(self.graph, 2, 5)

        self.addEdge(self.graph, 3, 0)
        self.addEdge(self.graph, 3, 4)
        self.addEdge(self.graph, 3, 6)

        self.addEdge(self.graph, 4, 1)
        self.addEdge(self.graph, 4, 3)
        self.addEdge(self.graph, 4, 5)
        self.addEdge(self.graph, 4, 7)

        self.addEdge(self.graph, 5, 2)
        self.addEdge(self.graph, 5, 4)
        self.addEdge(self.graph, 5, 8)

        self.addEdge(self.graph, 6, 3)
        self.addEdge(self.graph, 6, 7)

        self.addEdge(self.graph, 7, 4)
        self.addEdge(self.graph, 7, 6)
        self.addEdge(self.graph, 7, 8)

        self.addEdge(self.graph, 8, 5)
        self.addEdge(self.graph, 8, 7)

        # =====================================================

    def setCursorMode(self):
        if self.controller.getCursorMode() == "Clean/Dirty tool":
            self.cursorMode = CursorMode.C_D_State

        elif self.controller.getCursorMode() == "Wall tool":
            self.cursorMode = CursorMode.W_STATE

        elif self.controller.getCursorMode() == "Vacuum tool":
            self.cursorMode = CursorMode.V_STATE

    def changeTileState(self, i):
        self.setCursorMode()
        if (self.lock == False):
            if (self.cursorMode == CursorMode.C_D_State):  # changes the location of the dirty tile
                if (self.tiles[i]['text'] != "vacuum" and self.tiles[i]['text'] != "wall" and self.tiles[i]['text'] != "dirty"):
                    self.tiles[i]['text'] = "dirty"
                    self.tiles[i]['image'] = self.Tile_Dirty
                    if self.dirtTile != -1:
                        self.tiles[self.dirtTile]['image'] = self.Tile_Clean
                        self.tiles[self.dirtTile]['text'] = "clean"
                    self.dirtTile = i
            elif (self.cursorMode == CursorMode.V_STATE):  # changes the location of the vacuum
                if (self.tiles[i]['text'] != "vacuum" and self.tiles[i]['text'] != "wall" and self.tiles[i]['text'] != "dirty"):
                    self.tiles[i]['text'] = "vacuum"
                    self.tiles[i]['image'] = self.Vacuum_Clean
                    self.tiles[self.VacuumTile]['image'] = self.Tile_Clean
                    self.tiles[self.VacuumTile]['text'] = "clean"
                    self.VacuumTile = i
            # changes tiles into walls and vice verca
            elif (self.cursorMode == CursorMode.W_STATE):
                if (self.tiles[i]['text'] != "wall" and self.tiles[i]['text'] != "vacuum" and self.tiles[i]['text'] != "dirty"):
                    self.tiles[i]['text'] = "wall"
                    self.tiles[i]['image'] = self.Wall
                elif (self.tiles[i]['text'] != "vacuum"):
                    self.tiles[i]['text'] = "clean"
                    self.tiles[i]['image'] = self.Tile_Clean

    def dfs(self):
        self.lock = True
        visitedTiles = set()
        path = []
        tos = self.VacuumTile
        path.append(self.VacuumTile)
        visitedTiles.add(self.VacuumTile)

        for n in range(len(self.tiles)):
            if self.tiles[n]['text'] == "wall":
                visitedTiles.add(n)

        while len(path) != 0:
            if (self.tiles[tos]['text'] == "vacuumDirty"):
                self.tiles[tos]['text'] = "vacuum"
                self.dirtTile = -1
                self.lock = False
                return path
            else:
                options = len(self.graph[tos])
                for n in self.graph[tos]:
                    if n not in visitedTiles:
                        path.append(n)
                        visitedTiles.add(n)
                        tos = n
                        self.changeVacuumState(self.VacuumTile, tos)
                        self.update()
                        time.sleep(1)
                        break
                    elif n == self.graph[tos][options - 1]:
                        path.pop()
                        if len(path) != 0:
                            tos = path[len(path) - 1]
                        self.changeVacuumState(self.VacuumTile, tos)
                        self.update()
                        time.sleep(1)
        self.lock = False

    def bfs(self):
        self.lock = True
        visitedTiles = set()
        frontiers = []
        nextf = []

        for n in range(len(self.tiles)):
            if self.tiles[n]['text'] == "wall":
                visitedTiles.add(n)
        visitedTiles.add(self.VacuumTile)

        for n in self.graph[self.VacuumTile]:
            frontiers.append(n)

        while len(frontiers) > 0:
            print(frontiers)
            for i in frontiers:
                if i not in visitedTiles:
                    self.changeVacuumState(self.VacuumTile, i)
                    visitedTiles.add(self.VacuumTile)
                    self.update()
                    time.sleep(1)
                    if (self.tiles[i]['text'] == "vacuumDirty"):
                        self.tiles[i]['text'] = "vacuum"
                        self.dirtTile = -1
                        self.lock = False
                        print("here")
                        return
                    for n in self.graph[i]:
                        if n not in visitedTiles and n not in nextf:
                            nextf.append(n)
            frontiers = nextf[:]
            nextf.clear()
        self.lock = False

    def changeVacuumState(self, old, new):
        if self.tiles[new]['text'] == "dirty":
            self.tiles[old]['image'] = self.Tile_Clean
            self.tiles[old]['text'] = 'clean'
            self.tiles[new]['image'] = self.Vacuum_Clean
            self.tiles[new]['text'] = 'vacuumDirty'
            self.VacuumTile = new
        else:
            self.tiles[old]['image'] = self.Tile_Clean
            self.tiles[old]['text'] = 'clean'
            self.tiles[new]['image'] = self.Vacuum_Clean
            self.tiles[new]['text'] = 'vacuum'
            self.VacuumTile = new

    def addEdge(self, graph, u, v):
        graph[u].append(v)

    # definition of function
    def generate_edges(graph):
        edges = []

        # for each node in graph
        for node in graph:

            # for each neighbour node of a single node
            for neighbour in graph[node]:

                # if edge exists then append
                edges.append((node, neighbour))
        return edges
