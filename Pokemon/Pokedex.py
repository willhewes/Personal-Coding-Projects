import tkinter as tk
from tkinter import simpledialog, messagebox
import random
from Pokedex_Utility import get_pokemon_by_id, display_pokemon

# Fetch and display Pokémon based on user input or random selection
def fetch_pokemon(pokemon_id=True):
    if pokemon_id is True:
        # Prompt user to enter a Pokémon ID
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
        # Generate a random Pokémon ID up to 1010 (didn't bother with those over 10000)
        pokemon_id = random.randint(1, 1010)

    # Retrieve Pokémon data and display it
    pokemon_data = get_pokemon_by_id(pokemon_id)
    if pokemon_data:
        display_pokemon(pokemon_data, display_frame)
    else:
        messagebox.showerror("Error", "No data found for the given Pokémon ID.")

# Initialize main Tkinter window
root = tk.Tk()
root.title("Pokédex")

# Header frame
header_frame = tk.Frame(root, bg="#d9e3f0")
header_frame.pack(side='top', fill='x', pady=20)

# Frame to hold action buttons
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(side='top', pady=20)

# Button to fetch random Pokémon
tk.Button(button_frame, text="Random Pokémon", command=lambda: fetch_pokemon(False), font=("Helvetica", 16)).pack(side='left', padx=20)
# Button to prompt user for specific Pokémon ID
tk.Button(button_frame, text="Enter Pokémon ID", command=lambda: fetch_pokemon(True), font=("Helvetica", 16)).pack(side='right', padx=20)

# Frame to display Pokémon details and image
display_frame = tk.Frame(root, bg="#f0f0f0")
display_frame.pack(expand=True, fill='both', pady=20)

# Run the Tkinter main event loop
root.mainloop()