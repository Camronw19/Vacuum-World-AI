from tkinter import *
import TileFrame


class NavbarFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.configure(bg="#222831")
        self.rowconfigure(tuple(range(20)), weight=1)
        self.columnconfigure(2, weight=1)

        self.controlledWindow = TileFrame.Tiles

        # Tool Menu===============================================
        self.options_list = ["Clean/Dirty tool", "Wall tool", "Vacuum tool"]
        self.value_inside = StringVar(self)
        self.value_inside.set("Cursor Tools")

        self.toolMenu = OptionMenu(self, self.value_inside, *
                                   self.options_list, command=self.setCursorMode)
        self.toolMenu.configure(font=('Calisto MT', 18),
                                bg="#222831", fg="white", border=0, width=15, highlightthickness=1, highlightbackground="#BBBFCA", activebackground="#393E46", activeforeground="white")
        self.toolMenu.grid(row=0, column=0, sticky=E+W, padx=10)

        self.cursorMode = "Null"
        # ========================================================

        # algorithm  Menu ===============================================
        self.options_list = ["Depth First", "Breadth First"]
        self.value_inside = StringVar(self)
        self.value_inside.set("Algorithm")

        self.toolMenu = OptionMenu(self, self.value_inside, *
                                   self.options_list, command=self.setAlgorithm)
        self.toolMenu.configure(font=('Calisto MT', 18),
                                bg="#222831", fg="white", border=0, width=15, highlightthickness=1, highlightbackground="#BBBFCA", activebackground="#393E46", activeforeground="white")
        self.toolMenu.grid(row=2, column=0, sticky=E+W, padx=10)

        self.algorithm = "Null"
        # ========================================================

        # Start Button===========================================
        self.startButton = Button(self, text="Start",
                                  font=('Calisto MT', 18), fg="black", bg="#BBBFCA", activebackground="#BBBFCA", activeforeground="black", width=15,  command=self.startAlgorithm)
        self.startButton.grid(row=18, column=0, sticky=E+W+N+S,
                              padx=10, pady=10, columnspan=3)

        self.start = False
        # =======================================================
        # Reset Button===========================================
        self.resetButton = Button(self, text="Reset",
                                  font=('Calisto MT', 18), fg="black", bg="#BBBFCA", activebackground="#BBBFCA", activeforeground="black",  command=self.resetTiles)
        self.resetButton.grid(row=17, column=0, sticky=W,  padx=10, pady=10)

        self.start = False
        # =======================================================

    def getCursorMode(self):
        return self.cursorMode

    def setCursorMode(self, value):
        self.cursorMode = value

    def setAlgorithm(self, value):
        self.algorithm = value

    def startAlgorithm(self):
        if self.algorithm == "Depth First":
            self.controlledWindow.dfs()
        elif self.algorithm == "Breadth First":
            self.controlledWindow.bfs()

    def mainWindow(self, controlled):
        self.controlledWindow = controlled

    def resetTiles(self):
        self.controlledWindow.resetVisitedTiles()
