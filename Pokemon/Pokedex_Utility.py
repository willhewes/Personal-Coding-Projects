import requests
from PIL import Image, ImageTk
import io
import tkinter as tk

# Fetch Pokémon data indexed by Pokémon ID
def get_pokemon_by_id(pokemon_id):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}'
    response = requests.get(url)

    if response.status_code == 200:  # Check if request was successful
        pokemon_data = response.json()
        return pokemon_data
    else:
        return None

# Download and process the Pokémon image from a given URL
def process_pokemon_image(image_url):
    if image_url:
        response = requests.get(image_url)
        img = Image.open(io.BytesIO(response.content))
        img = img.resize((200, 200), Image.LANCZOS)  # Resize for display
        return img
    return None

# Display Pokémon details and image in the provided Tkinter frame
def display_pokemon(pokemon_data, display_frame):
    # Extract and format Pokémon details
    name = pokemon_data['name'].capitalize()
    poke_id = pokemon_data['id']
    height = pokemon_data['height'] * 10  # Convert to centimeters
    weight = pokemon_data['weight'] / 10  # Convert to kilograms
    types = ", ".join([type_info['type']['name'].capitalize() for type_info in pokemon_data['types']])
    abilities = ", ".join([ability_info['ability']['name'].capitalize() for ability_info in pokemon_data['abilities']])
    stats = "\n".join([f"{stat_info['stat']['name'].capitalize()}: {stat_info['base_stat']}" for stat_info in pokemon_data['stats']])

    # Get Pokémon image
    image_url = pokemon_data['sprites']['front_default']
    img = process_pokemon_image(image_url)

    # Clear existing widgets in the frame
    for widget in display_frame.winfo_children():
        widget.destroy()

    # Define styles
    title_font = ("Helvetica", 20, "bold")
    label_font = ("Helvetica", 14)
    stats_font = ("Helvetica", 12)
    background_color = "#f0f0f0"
    text_color = "#333333"

    # Add Pokémon details as labels
    tk.Label(display_frame, text=f"Name: {name}", font=title_font, bg=background_color, fg=text_color).pack(pady=5)
    tk.Label(display_frame, text=f"ID: {poke_id}", font=label_font, bg=background_color, fg=text_color).pack(pady=5)
    tk.Label(display_frame, text=f"Height: {height}cm", font=label_font, bg=background_color, fg=text_color).pack(pady=5)
    tk.Label(display_frame, text=f"Weight: {weight}kg", font=label_font, bg=background_color, fg=text_color).pack(pady=5)
    tk.Label(display_frame, text=f"Types: {types}", font=label_font, bg=background_color, fg=text_color).pack(pady=5)
    tk.Label(display_frame, text=f"Abilities: {abilities}", font=label_font, bg=background_color, fg=text_color).pack(pady=5)
    tk.Label(display_frame, text="Stats:", font=label_font, bg=background_color, fg=text_color).pack(pady=5)
    tk.Label(display_frame, text=stats, font=stats_font, bg=background_color, fg=text_color).pack(pady=5)

    # Add Pokémon image if available
    if img:
        img = ImageTk.PhotoImage(img)
        tk.Label(display_frame, image=img).pack(pady=10)
        display_frame.img = img  # Prevent image from being garbage collected

    display_frame.update()  # Refresh frame display