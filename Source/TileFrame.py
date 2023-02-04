from tkinter import *


class Tiles(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.columnconfigure(tuple(range(10)), weight=1)
        self.rowconfigure(tuple(range(5)), weight=1)

        self.tiles = []
        i = 0
        for x in range(10):
            for y in range(5):
                self.tiles.append(
                    Button(self,  text="clean", font=('Arial', 18), bg="#eeeee4", command=lambda x=i: self.changeTileState(x)))
                self.tiles[i].grid(column=x, row=y, sticky="news")
                i += 1

    def changeTileState(self, i):
        if (self.tiles[i]['text'] == "clean"):
            self.tiles[i]['text'] = "dirty"
            self.tiles[i]['bg'] = "#8c6d47"
        elif (self.tiles[i]['text'] == "dirty"):
            self.tiles[i]['text'] = "clean"
            self.tiles[i]['bg'] = "#eeeee4"
