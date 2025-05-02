import tkinter as tk
from tkinter import simpledialog, messagebox
import random
from Pokedex_Utility import get_pokemon_by_id, display_pokemon

def fetch_pokemon(pokemon_id=True):
    if pokemon_id is True:
        user_input = simpledialog.askstring("Input", "Enter Pokémon ID:", parent=root)

        if user_input:
            try:
                pokemon_id = int(user_input)
                if pokemon_id <= 0:
                    raise ValueError("ID must be a positive integer.")
            except ValueError as e:
                messagebox.showerror("Invalid Input", f"Error: {e}")
                return
    else:
        pokemon_id = random.randint(1, 1010)

    pokemon_data = get_pokemon_by_id(pokemon_id)
    if pokemon_data:
        display_pokemon(pokemon_data, display_frame)
    else:
        messagebox.showerror("Error",  "No data found for the given Pokémon ID.")

root = tk.Tk()
root.title("Pokédex")

header_frame = tk.Frame(root, bg="#d9e3f0")
header_frame.pack(side='top', fill='x', pady=20)

button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(side='top', pady=20)

tk.Button(button_frame, text="Random Pokémon", command=lambda: fetch_pokemon(False), font=("Helvetica", 16)).pack(side='left', padx=20)
tk.Button(button_frame, text="Enter Pokémon ID", command=lambda: fetch_pokemon(True), font=("Helvetica", 16)).pack(side='right', padx=20)

display_frame = tk.Frame(root, bg="#f0f0f0")
display_frame.pack(expand=True, fill='both', pady=20)

root.mainloop()