from tkinter import *
from enum import Enum


class Season(Enum):
    SPRING = 1
    SUMMER = 2
    AUTUMN = 3
    WINTER = 4


class Tiles(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.columnconfigure(tuple(range(10)), weight=1)
        self.rowconfigure(tuple(range(5)), weight=1)

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

        # Generate Tiles======================================
        self.tiles = []
        i = 0
        for x in range(10):
            for y in range(5):
                self.tiles.append(
                    Button(self,  image=self.Tile_Clean, text="clean", font=('Arial', 18),  bg="#eeeee4", borderwidth=1, command=lambda x=i: self.changeTileState(x)))
                self.tiles[i].grid(column=x, row=y, sticky="news")
                self.tiles[i].image = self.Tile_Clean
                i += 1
        # =====================================================

    def changeTileState(self, i):
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
