import tkinter as tk
from tkinter import ttk

from src.data_loader import DataLoader
from src.data_preprocessor import preprocess_data
from src.evaluation import get_recommendations

# Load data
data_loader = DataLoader()
data = data_loader.load_data()


def on_button_click(entry, result_label):

    user_input = entry.get()
    # filter the hotel name and the score
    result = get_recommendations(data, user_input)
    result_label.config(text=result)


def show_frame_ru():
    # Crear la ventana principal
    ventana = tk.Toplevel()
    ventana.title("Accommodation Finder")
    ventana.geometry("600x400")
    ventana.resizable(False, False)
    # color de fondo
    ventana.config(bg="black")

    # Crear una etiqueta
    title_label = tk.Label(ventana, text="Accommodation Finder GUI", font=("Arial", 20))
    title_label.config(fg="white", bg="black")
    title_label.pack(pady=10)

    # Crear un cuadro de texto
    entry = tk.Entry(ventana, width=30)
    entry.pack(pady=10)

    # Crear una etiqueta para mostrar el resultado
    result_label = tk.Label(ventana, text="")

    # Crear un botón de aceptar
    find_button = tk.Button(ventana, text="Find", command=lambda: on_button_click(entry, result_label))
    find_button.pack(pady=10)

    result_label.pack(pady=10)

    # Iniciar el bucle principal de la interfaz gráfica
    ventana.mainloop()
