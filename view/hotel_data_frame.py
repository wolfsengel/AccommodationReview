import tkinter as tk
from tkinter import ttk

from src.hotel_model import get_worst_values_for_hotel, get_best_values_for_hotel
from src.data_loader import DataLoader
from src.hotel_model import create_hotel_objects


def update_results(event):
    search_query = search_var.get().lower()
    matching_hotels = [hotel.name for hotel in hotel_objects if search_query in hotel.name.lower()]
    results_listbox.delete(0, tk.END)
    for hotel in matching_hotels:
        results_listbox.insert(tk.END, hotel)


def on_select(event):
    selected_index_filtered = results_listbox.curselection()
    if selected_index_filtered:
        selected_index_filtered = selected_index_filtered[0]
        selected_hotel_name = results_listbox.get(selected_index_filtered)
        # Find the corresponding index in the original list
        selected_index_original = [i for i, hotel in enumerate(hotel_objects) if hotel.name == selected_hotel_name][0]
        selected_hotel = hotel_objects[selected_index_original]

        search_var.set(selected_hotel.name)
        update_results(None)

        # Display detailed info in the Text widget
        info_text.delete(1.0, tk.END)
        info_text.insert(tk.END, str(selected_hotel))
        info_text.insert(tk.END, f"Worst Features: {get_worst_values_for_hotel(data, selected_hotel.name)}\n")
        info_text.insert(tk.END, f"Best Features: {get_best_values_for_hotel(data, selected_hotel.name)}\n")


# Load the dataset
data = DataLoader().load_data()

# Create hotel objects using the provided function
hotel_objects = create_hotel_objects(data)

# Create the main window
root = tk.Tk()
root.title("Hotel Stats")
root.resizable(False, False)
root.geometry("600x400")
root.config(bg="black")

# Create variables
search_var = tk.StringVar()

# Create a title label
title_label = tk.Label(root, text="Hotel Stats", font=("Arial", 20))
title_label.config(fg="white", bg="black")
title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky=tk.W)

# Create GUI components
# Create a label
search_label = ttk.Label(root, text="Hotel name:")
search_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

# Create an entry box
search_entry = ttk.Entry(root, textvariable=search_var)
search_entry.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W + tk.E)
search_entry.bind("<KeyRelease>", update_results)

# Create a listbox
results_listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=10)
results_listbox.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)
results_listbox.bind("<ButtonRelease-1>", on_select)

# Create a scrollbar
results_scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=results_listbox.yview)
results_scrollbar.grid(row=1, column=2, rowspan=4, sticky=tk.N + tk.S)
results_listbox.configure(yscrollcommand=results_scrollbar.set)

# Create a Text widget for detailed information
info_text = tk.Text(root, height=10, width=40)
info_text.grid(row=0, column=3, rowspan=4, columnspan=3, padx=10, pady=10, sticky=tk.W)

# Start the main event loop
root.mainloop()
