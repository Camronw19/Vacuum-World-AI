from tkinter import *


class NavbarFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.configure(width=700)
        self.configure(bg="#386e6b")
        self.rowconfigure(tuple(range(5)), weight=1)
        self.columnconfigure(0, weight=1)

        # Tool Menu===============================================
        options_list = ["Clean/Dirty tool", "Option 2"]
        value_inside = StringVar(self)
        value_inside.set("Select an Option")

        toolMenu = OptionMenu(self, value_inside, *options_list)
        toolMenu.grid(row=0, column=0, sticky=E+W, padx=10)
        # ========================================================

        # Start Button===========================================
        startButton = Button(self, text="Start",
                             font=('Arial', 18), bg="#eeeee4")
        startButton.grid(row=5, column=0, sticky=E+W, padx=10, pady=10)
        # =======================================================
