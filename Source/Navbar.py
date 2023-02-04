from tkinter import *


class NavbarFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.configure(bg="#222831")
        self.rowconfigure(tuple(range(10)), weight=1)
        self.columnconfigure(0, weight=1)

        # Tool Menu===============================================
        options_list = ["Clean/Dirty tool", "Option 2"]
        value_inside = StringVar(self)
        value_inside.set("Cursor Tools")

        toolMenu = OptionMenu(self, value_inside, *options_list)
        toolMenu.configure(font=('Calisto MT', 18),
                           bg="#222831", fg="white", border=0, highlightthickness=1, highlightbackground="#BBBFCA", activebackground="#393E46", activeforeground="white")
        toolMenu.grid(row=0, column=0, sticky=E+W, padx=10)
        # ========================================================

        # Start Button===========================================
        startButton = Button(self, text="Start",
                             font=('Calisto MT', 18), fg="black", bg="#BBBFCA", activebackground="#BBBFCA", activeforeground="black", width=15)
        startButton.grid(row=10, column=0, sticky=E+W, padx=10, pady=10)
        # =======================================================
