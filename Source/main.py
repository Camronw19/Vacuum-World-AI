import tkinter as tk
import TileFrame
import Navbar

# constants==========================================
PADDING = 3
# ===================================================

window = tk.Tk()
window.geometry("1600x700")
window.configure(bg="black")

# navbar frame======================================
navbar = Navbar.NavbarFrame(window)
navbar.pack(side="left", fill="y", padx=(PADDING, 0), pady=PADDING)

# tile frame========================================
body = tk.Frame(window, bg="black")
body.rowconfigure(0, weight=1)
body.columnconfigure(0, weight=1)
body.pack(side="right", fill="both", expand="true")

tileWindow = TileFrame.Tiles(body)
tileWindow.grid(row=0, column=0, sticky="news", padx=PADDING, pady=PADDING)


window.mainloop()
