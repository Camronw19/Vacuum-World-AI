from tkinter import *
import TileFrame


class NavbarFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.configure(bg="#222831")
        self.rowconfigure(tuple(range(10)), weight=1)
        self.columnconfigure(0, weight=1)

        # Tool Menu===============================================
        self.options_list = ["Clean/Dirty tool", "Wall tool", "Vacuum tool"]
        self.value_inside = StringVar(self)
        self.value_inside.set("Cursor Tools")

        self.toolMenu = OptionMenu(self, self.value_inside, *
                                   self.options_list, command=self.setCursorMode)
        self.toolMenu.configure(font=('Calisto MT', 18),
                                bg="#222831", fg="white", border=0, highlightthickness=1, highlightbackground="#BBBFCA", activebackground="#393E46", activeforeground="white")
        self.toolMenu.grid(row=0, column=0, sticky=E+W, padx=10)

        self.cursorMode = "Null"
        # ========================================================

        # Start Button===========================================
        self.startButton = Button(self, text="Start",
                                  font=('Calisto MT', 18), fg="black", bg="#BBBFCA", activebackground="#BBBFCA", activeforeground="black", width=15, command=self.startAlgorithm)
        self.startButton.grid(row=10, column=0, sticky=E+W, padx=10, pady=10)

        self.start = False
        # =======================================================

    def getCursorMode(self):
        return self.cursorMode

    def setCursorMode(self, value):
        self.cursorMode = value

    def startAlgorithm(self):
        self.start = True

    def getStart(self):
        return self.start
