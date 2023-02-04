import tkinter as tk
import TileFrame

window = tk.Tk()
window.geometry("1500x800")
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)


# Assets============================================
Tile_Clean = tk.PhotoImage(
    file=r"C:\Users\camro\Documents\Development\Python Projects\Vacuum World\Assets\ScaledTile.png")


# navbar frame=====================================
navbar = tk.Frame(window, bg="red")
navbar.grid(row=0, column=0, sticky="news")

tileWindow = TileFrame.Tiles(window)
tileWindow.grid(row=0, column=1, sticky="news", padx=10, pady=10)

window.mainloop()
