import tkinter as tk
import TileFrame
import Navbar

window = tk.Tk()
window.geometry("1500x800")

window.configure(bg="#112139")

# Assets============================================
Tile_Clean = tk.PhotoImage(
    file=r"C:\Users\camro\Documents\Development\Python Projects\Vacuum World\Assets\ScaledTile.png")
# ===================================================

# navbar frame======================================
navbar = Navbar.NavbarFrame(window)
navbar.pack(side="left", fill="y")

# tile frame========================================
body = tk.Frame(window)
body.rowconfigure(0, weight=1)
body.columnconfigure(0, weight=1)
body.pack(side="right", fill="both", expand="true")

tileWindow = TileFrame.Tiles(body)
tileWindow.grid(row=0, column=0, sticky="news", padx=10, pady=10)


window.mainloop()
