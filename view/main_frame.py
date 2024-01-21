import tkinter as tk
from tkinter import ttk
from view.new_user_frame import show_frame_nu
from view.registered_user import show_frame_ru


def show_main_frame():
    main_frame = tk.Tk()
    main_frame.title("Accommodation Finder")
    main_frame.geometry("600x400")
    main_frame.resizable(False, False)
    # color de fondo
    main_frame.config(bg="black")

    # Crear una etiqueta
    title_label = tk.Label(main_frame, text="Accommodation Finder GUI", font=("Arial", 20))
    title_label.config(fg="white", bg="black")
    title_label.pack(pady=10)

    button1 = ttk.Button(main_frame, text="Get a Recommendation", command=show_frame_nu)
    button1.pack(pady=20)

    button2 = ttk.Button(main_frame, text="Registered User", command=show_frame_ru)
    button2.pack(pady=20)
    main_frame.mainloop()

