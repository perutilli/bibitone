import tkinter as tk
from MainPage import *

root = tk.Tk()

app = MainPage(master=root)
app.mainloop()


# window = tk.Tk()

# btn_shots = tk.Button(
#     text="SHOTS",
#     height=10,
#     master=window
# )

# btn_drinks = tk.Button(
#     text="DRINKS",
#     height=10,
#     master=window
# )


# def handle_btn_shots(event):
#     pass


# def handle_btn_drinks(event):
#     pass


# btn_shots.bind("<Button-1>", handle_btn_shots)
# btn_drinks.bind("<Button-1>", handle_btn_drinks)

# btn_shots.pack(fill=tk.X)
# btn_drinks.pack(fill=tk.X)
# window.mainloop()
