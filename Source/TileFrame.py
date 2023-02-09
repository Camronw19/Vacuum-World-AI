from tkinter import *
from enum import Enum
import Navbar


class CursorMode(Enum):
    C_D_State = 1
    V_STATE = 2
    W_STATE = 3


class Tiles(Frame):
    def __init__(self, parent, control):
        Frame.__init__(self, parent)

        self.columnconfigure(tuple(range(10)), weight=1)
        self.rowconfigure(tuple(range(5)), weight=1)

        self.cursorMode = CursorMode.C_D_State

        self.controller = control

        # Assets============================================
        self.Tile_Clean = PhotoImage(
            file=r"C:\Users\camro\Documents\Development\Python Projects\Vacuum World\Assets\TileClean.png")
        self.Tile_Dirty = PhotoImage(
            file=r"C:\Users\camro\Documents\Development\Python Projects\Vacuum World\Assets\TileDirty.png")
        self.Vacuum_Clean = PhotoImage(
            file=r"C:\Users\camro\Documents\Development\Python Projects\Vacuum World\Assets\VacuumClean.png")
        self.Vacuum_dirty = PhotoImage(
            file=r"C:\Users\camro\Documents\Development\Python Projects\Vacuum World\Assets\VaccumDirty.png")
        # ===================================================

        # Generate Tiles=====================================
        self.tiles = []
        i = 0
        for x in range(10):
            for y in range(5):
                self.tiles.append(
                    Button(self,  image=self.Tile_Clean, text="clean", font=('Arial', 18),  bg="#eeeee4", borderwidth=1, command=lambda x=i: self.changeTileState(x)))
                self.tiles[i].grid(column=x, row=y, sticky="news")
                self.tiles[i].image = self.Tile_Clean
                i += 1
        # ====================================================

    def setCursorMode(self):
        print(self.controller.getCursorMode())
        if self.controller.getCursorMode() == "Clean/Dirty tool":
            self.cursorMode = CursorMode.C_D_State
            print("here")
        else:
            self.cursorMode = CursorMode.V_STATE

    def changeTileState(self, i):
        # changes tiles from clean to dirty and vice versa
        self.setCursorMode()
        if (self.cursorMode == CursorMode.C_D_State):
            if (self.tiles[i]['text'] == "clean"):
                self.tiles[i]['text'] = "dirty"
                self.tiles[i]['image'] = self.Tile_Dirty

                # self.tiles[i]['bg'] = "#3C2A21"
                # self.tiles[i]['fg'] = "white"
            elif (self.tiles[i]['text'] == "dirty"):
                self.tiles[i]['text'] = "clean"
                self.tiles[i]['image'] = self.Tile_Clean
                # self.tiles[i]['bg'] = "#eeeee4"
                # self.tiles[i]['fg'] = "black"
        elif (self.cursorMode == CursorMode.V_STATE):  # changes the location of the vacuum
            pass
        elif (self.cursorMode == CursorMode.W_STATE):  # changes tiles into walls and vice verca
            pass
