import tkinter as tk
from tkinter import ttk


def on_button_click():
    selected_country = combo_box.get()
    user_input = entry.get()
    result_label.config(text=f"Selected country : {selected_country}\nSent info: {user_input}")


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Accommodation Finder")
ventana.geometry("600x400")
ventana.resizable(False, False)
# color de fondo
ventana.config(bg="black")

# Crear una etiqueta
title_label = tk.Label(ventana, text="Accommodation Finder GUI", font=("Arial", 20))
title_label.config(fg="white", bg="black")
title_label.pack(pady=10)

# Crear un ComboBox con algunos países
paises = ["Netherlands", "United Kingdom", "France", "Spain", "Italy", "Austria"]
combo_box = ttk.Combobox(ventana, values=paises, state="readonly")
combo_box.set("¿Where are you going?")
combo_box.pack(pady=10)

# Crear un cuadro de texto
entry = tk.Entry(ventana, width=30)
entry.pack(pady=10)

# Crear un botón de aceptar
find_button = tk.Button(ventana, text="Find", command=on_button_click)
find_button.pack(pady=10)

# Crear una etiqueta para mostrar el resultado
result_label = tk.Label(ventana, text="")
result_label.pack(pady=10)

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()
