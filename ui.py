import tkinter as tk
from tkinter import messagebox

from analyzer import analyzer
from utilis import utils

class SyntaxisAnalizerUI:
    def __init__(self) -> None:
        pass

    def analyze(self):
        input_text = self.text_area.get("1.0", "end-1c")
        input_list = utils(input_text)
        print(input_list)
        message = analyzer(input_list)

        temp_win = tk.Tk()

        if message["success"]:
            temp_win.title("Texto Valido")
            label = tk.Label(temp_win, text="El texto es valido")
            label.pack()

            text_area_title = tk.Label(temp_win, text="Historial")
            text_area_title.pack()

            text_area = tk.Text(temp_win, height=20, width=100)
            text_area.pack()

            text_area.insert(tk.END, message["history"])

            temp_win.mainloop()

        else:
            temp_win.title("Texto Invalido")
            text_msg = tk.Text(temp_win, height=20, width=100)
            text_msg.pack()

            text_msg.insert(tk.END, message["message"])

            text_area_title = tk.Label(temp_win, text="Historial")
            text_area_title.pack()

            text_area = tk.Text(temp_win, height=20, width=100)
            text_area.pack()

            text_area.insert(tk.END, message["history"])

            temp_win.mainloop()

    def show(self):
        window = tk.Tk()
        window.title("Tabla predictiva")

        self.text_area = tk.Text(window, height=20, width=100)
        self.text_area.pack()

        
        button = tk.Button(window, text="Validar", command=self.analyze, 
                           font=('Helvetica', 12),  
                           bg='#4169E1',  
                           fg='white')  
        button.pack()

        window.mainloop()
