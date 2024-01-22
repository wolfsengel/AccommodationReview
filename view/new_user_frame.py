import tkinter as tk
from tkinter import ttk

from src.data_loader import DataLoader
from src.data_preprocessor import preprocess_data
from src.model import recommend_hotel

# Load data
data_loader = DataLoader()
data = data_loader.load_data()

# preprocess data
processed_data = preprocess_data(data)


def on_button_click(combo_box, entry, result_label):
    """
    Function to handle the button click event.

    :param combo_box:
    :param entry:
    :param result_label:
    :return:
    """
    # recommendation system
    selected_country = combo_box.get()
    user_input = entry.get()

    # filter the hotel name and the score
    result_label.config(text="Loading...")
    result = recommend_hotel(processed_data, selected_country, user_input)
    result_label.config(text=result)


def show_frame_nu():
    """
    Function to show the recommendation tool frame.
    :return:
    """
    # Create the main window
    ventana = tk.Tk()
    ventana.title("Accommodation Finder")
    ventana.geometry("600x400")
    ventana.resizable(False, False)
    # background color
    ventana.config(bg="black")

    # Create a label
    title_label = tk.Label(ventana, text="Accommodation Finder GUI", font=("Arial", 20))
    title_label.config(fg="white", bg="black")
    title_label.pack(pady=10)

    # Create a combo box
    paises = ["Netherlands", "UK", "France", "Spain", "Italy", "Austria"]
    combo_box = ttk.Combobox(ventana, values=paises, state="readonly")
    combo_box.set("¿Where are you going?")
    combo_box.pack(pady=10)

    # Create a text box
    entry = tk.Entry(ventana, width=30)
    entry.pack(pady=10)

    # Create a button
    find_button = tk.Button(ventana, text="Find", command=lambda: on_button_click(combo_box, entry, result_label))
    find_button.pack(pady=10)

    # Create a label to show the result
    result_label = tk.Label(ventana, text="")
    result_label.pack(pady=10)

    # Start the main loop of the GUI
    ventana.mainloop()


# main
if __name__ == "__main__":
    show_frame_nu()
