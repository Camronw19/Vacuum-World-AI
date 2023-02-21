from tkinter import *
from enum import Enum
from collections import defaultdict
import time
import random


class CursorMode(Enum):
    NO_STATE = 1
    C_D_State = 2
    V_STATE = 3
    W_STATE = 4


class Tiles(Frame):
    def __init__(self, parent, control):
        Frame.__init__(self, parent)

        self.ROWS = 4
        self.COLS = 4
        self.ANIMATIONSPEED = 6/10
        self.columnconfigure(tuple(range(self.ROWS)), weight=1)
        self.rowconfigure(tuple(range(self.COLS)), weight=1)

        self.cursorMode = CursorMode.NO_STATE

        self.controller = control
        self.lock = False
        self.VacuumTile = 0
        self.dirtTile = 7
        self.visitedTiles = []

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
        self.Tile_Visited = PhotoImage(
            file=r"C:\Users\camro\Documents\Development\Python Projects\Vacuum World\Assets\TileVisited.png")
        # ===================================================

        # Generate Tiles=====================================
        self.tiles = []
        i = 0
        for x in range(self.ROWS):
            for y in range(self.COLS):
                self.tiles.append(
                    Button(self,  image=self.Tile_Clean, text="clean", font=('Arial', 18),  bg="#eeeee4", borderwidth=1, command=lambda x=i: self.changeTileState(x)))
                self.tiles[i].grid(column=y, row=x, sticky="news")
                i += 1
        self.tiles[self.VacuumTile]['image'] = self.Vacuum_Clean
        self.tiles[self.VacuumTile]['text'] = "vacuum"

        self.tiles[self.dirtTile]['image'] = self.Tile_Dirty
        self.tiles[self.dirtTile]['text'] = "dirty"
        # ====================================================

        # generate search graph================================
        self.graph = defaultdict(list)
        self.initializeGraph(self.graph, self.ROWS, self.COLS)
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
                elif (self.tiles[i]['text'] != "vacuum" and self.tiles[i]['text'] != "dirty"):
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
                        time.sleep(self.ANIMATIONSPEED)
                        break
                    elif n == self.graph[tos][options - 1]:
                        path.pop()
                        if len(path) != 0:
                            tos = path[len(path) - 1]
                        self.changeVacuumState(self.VacuumTile, tos)
                        self.update()
                        time.sleep(self.ANIMATIONSPEED)
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
                    time.sleep(self.ANIMATIONSPEED)
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
            self.tiles[old]['image'] = self.Tile_Visited
            self.tiles[old]['text'] = 'clean'
            self.tiles[new]['image'] = self.Vacuum_Clean
            self.tiles[new]['text'] = 'vacuumDirty'
            self.VacuumTile = new
            self.visitedTiles.append(old)
        else:
            self.tiles[old]['image'] = self.Tile_Visited
            self.tiles[old]['text'] = 'clean'
            self.tiles[new]['image'] = self.Vacuum_Clean
            self.tiles[new]['text'] = 'vacuum'
            self.VacuumTile = new
            self.visitedTiles.append(old)

    def initializeGraph(self, graph, ROWS, COLS):
        i = 0
        for r in range(0, ROWS):
            for c in range(0, COLS):
                if r > 0 and r < ROWS - 1 and c > 0 and c < COLS - 1:  # middle tiles
                    graph[i].append(i - 1)
                    graph[i].append(i + 1)
                    graph[i].append(i - COLS)
                    graph[i].append(i + COLS)
                elif r == 0 and c == 0:  # top left corner
                    graph[i].append(i + 1)
                    graph[i].append(i + COLS)
                elif r == 0 and c == COLS - 1:  # top right corner
                    graph[i].append(i - 1)
                    graph[i].append(i + COLS)
                elif r == 0:  # top row
                    graph[i].append(i - 1)
                    graph[i].append(i + 1)
                    graph[i].append(i + COLS)
                elif r == ROWS - 1 and c == 0:  # bottom left corner
                    graph[i].append(i - COLS)
                    graph[i].append(i + 1)
                elif r == ROWS - 1 and c == COLS - 1:  # bottom right corner
                    graph[i].append(i - COLS)
                    graph[i].append(i - 1)
                elif r == ROWS - 1:  # bottom row
                    graph[i].append(i - 1)
                    graph[i].append(i + 1)
                    graph[i].append(i - COLS)
                elif c == 0:  # left col
                    graph[i].append(i + 1)
                    graph[i].append(i - COLS)
                    graph[i].append(i + COLS)
                elif c == COLS - 1:  # right col
                    graph[i].append(i - 1)
                    graph[i].append(i - COLS)
                    graph[i].append(i + COLS)
                i += 1
        for n in range(len(graph)):
            graph[n].sort()

    def resetVisitedTiles(self):
        if self.lock == False:
            for t in self.visitedTiles:
                if self.tiles[t]['text'] != "vacuum":
                    self.tiles[t]['image'] = self.Tile_Clean
            self.visitedTiles.clear()

            dirtyTileSet = False
            while dirtyTileSet == False and self.dirtTile == -1:
                x = random.randint(0, (self.ROWS * self.COLS) - 1)
                if self.tiles[x]['text'] != "vacuum" and self.tiles[x]['text'] != "wall":
                    self.tiles[x]['text'] = "dirty"
                    self.tiles[x]['image'] = self.Tile_Dirty
                    self.dirtTile = x
                    dirtyTileSet = True
