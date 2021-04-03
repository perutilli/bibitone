import tkinter as tk


def handle_btn_shots(event):
    pass


def handle_btn_drinks(event):
    pass


class MainPage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        btn_shots = tk.Button(
            text="SHOTS",
            height=10,
            master=self.master,
            command=self.pack_forget
        )

        btn_drinks = tk.Button(
            text="DRINKS",
            height=10,
            master=self.master
        )

        btn_shots.bind("<Button-1>", handle_btn_shots)
        # btn_drinks.bind("<Button-1>", handle_btn_drinks)

        btn_shots.pack(fill=tk.X)
        btn_drinks.pack(fill=tk.X)

    def delete_frame(self):
        self.pack_forget()
