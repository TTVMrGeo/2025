import tkinter as tk
from tkinter import filedialog
import requests
from PIL import Image, ImageTk
from io import BytesIO
import re
import json
import base64

class GameLauncherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Game Launcher")
        self.root.geometry("800x600")

        # Variable to track dark/light mode (default is dark mode)
        self.dark_mode = True

        # List to store game information (with cached hero banners)
        self.games = []

        # Load cached games from file
        self.load_games()

        # Top Frame for Settings Button
        self.top_frame = tk.Frame(root, height=30, bg="gray20")
        self.top_frame.pack(side=tk.TOP, fill=tk.X)

        # Settings Button with Gear Icon
        self.settings_icon = tk.PhotoImage(file="gear_icon.png").subsample(20, 20)  # Resize the icon
        self.settings_button = tk.Button(self.top_frame, image=self.settings_icon, command=self.toggle_settings, bd=0, bg="gray20")
        self.settings_button.pack(side=tk.RIGHT, padx=10, pady=5)

        # Settings Widget Frame (initially hidden)
        self.settings_frame = tk.Frame(root, bg="gray20")
        self.settings_visible = False

        # Dark/Light Mode Toggle in Settings (default is dark mode)
        self.mode_var = tk.StringVar(value="Dark Mode")
        self.mode_toggle = tk.Checkbutton(self.settings_frame, text="Dark Mode", variable=self.mode_var, onvalue="Dark Mode", offvalue="Light Mode", command=self.toggle_dark_mode, bg="gray20", fg="white", selectcolor="black")
        self.mode_toggle.pack(pady=10, padx=10, anchor="w")

        # Left Frame for Game List
        self.left_frame = tk.Frame(root, width=200, height=570, bg="gray20")
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y)

        # Right Frame for Game Details
        self.right_frame = tk.Frame(root, width=600, height=570, bg="gray10")
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Add Game Button
        self.add_game_button = tk.Button(self.left_frame, text="Add Game", command=self.add_game, bg="gray30", fg="white")
        self.add_game_button.pack(pady=10)

        # Listbox to display games
        self.game_listbox = tk.Listbox(self.left_frame, width=25, height=30, bg="gray30", fg="white")
        self.game_listbox.pack(pady=10, padx=10)
        self.game_listbox.bind('<<ListboxSelect>>', self.on_game_select)

        # Label to display game details (initially empty)
        self.game_details_label = tk.Label(self.right_frame, bg="gray10")
        self.game_details_label.pack(pady=20, fill=tk.BOTH, expand=True)

        # Populate the listbox with cached games
        for game in self.games:
            self.game_listbox.insert(tk.END, game["name"])

        # Save games to file when the app closes
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def add_game(self):
        # Open file dialog to select .exe file
        file_path = filedialog.askopenfilename(filetypes=[("Executable files", "*.exe")])
        if file_path:
            # Extract the game name and remove the .exe extension
            game_name = file_path.split("/")[-1].replace(".exe", "")
            # Fetch the hero banner and cache it
            hero_banner = self.fetch_hero_banner(game_name)
            if hero_banner:
                # Add the game to the list with the cached banner
                self.games.append({"name": game_name, "path": file_path, "hero_banner": self.image_to_base64(hero_banner)})
                self.game_listbox.insert(tk.END, game_name)

    def on_game_select(self, event):
        # Get the selected game index
        selected_index = self.game_listbox.curselection()
        if selected_index:
            selected_game = self.games[selected_index[0]]
            # Display the cached hero banner
            hero_banner = self.base64_to_image(selected_game["hero_banner"])
            if hero_banner:
                self.display_hero_banner(hero_banner)
            else:
                self.game_details_label.config(text="Failed to load hero banner.", fg="white")

    def add_spaces_to_name(self, name):
        # Insert spaces into the game name (e.g., "BloonsTD6" -> "Bloons TD 6")
        name_with_spaces = re.sub(r"(?<=[a-z])(?=[A-Z0-9])", " ", name)  # Add space before uppercase letters or numbers
        name_with_spaces = re.sub(r"(?<=[0-9])(?=[A-Z])", " ", name_with_spaces)  # Add space between numbers and letters
        return name_with_spaces

    def search_game_id(self, game_name):
        # Add spaces to the game name for better search results
        game_name_with_spaces = self.add_spaces_to_name(game_name)
        print(f"Searching for: {game_name_with_spaces}")

        # Search for the game by name to get its numeric ID
        url = f"https://www.steamgriddb.com/api/v2/search/autocomplete/{game_name_with_spaces}"
        headers = {
            "Authorization": "Bearer 7943314451087e571d49014eaa3fbea8"  # Replace with your SteamGridDB API key
        }
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            if data["success"] and data["data"]:
                # Return the ID of the first matching game
                return data["data"][0]["id"]
        return None

    def fetch_hero_banner(self, game_name):
        # Search for the game ID
        game_id = self.search_game_id(game_name)
        if not game_id:
            return None

        # Fetch the hero banners for the game ID
        url = f"https://www.steamgriddb.com/api/v2/grids/game/{game_id}"
        headers = {
            "Authorization": "Bearer 7943314451087e571d49014eaa3fbea8"  # Replace with your SteamGridDB API key
        }
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            if data["success"] and data["data"]:
                # Filter for original assets (preferred style)
                original_assets = [
                    asset for asset in data["data"]
                    if asset.get("style") == "alternate" and asset.get("width") == 1920 and asset.get("height") == 620
                ]
                if not original_assets:
                    original_assets = data["data"]  # Fallback to all assets if no original assets are found

                # Get the first hero banner URL from the filtered list
                hero_banner_url = original_assets[0]["url"]
                # Fetch the image
                image_response = requests.get(hero_banner_url)
                if image_response.status_code == 200:
                    # Load the image using Pillow
                    image = Image.open(BytesIO(image_response.content))
                    image = image.resize((600, 300), Image.Resampling.LANCZOS)  # Corrected attribute name
                    return image
        return None

    def display_hero_banner(self, hero_banner):
        if hero_banner:
            # Convert the image to a PhotoImage
            photo = ImageTk.PhotoImage(hero_banner)
            # Update the game details label with the cached image
            self.game_details_label.config(image=photo)
            self.game_details_label.image = photo  # Keep a reference to avoid garbage collection
        else:
            self.game_details_label.config(text="No hero banner found.", fg="white")

    def image_to_base64(self, image):
        # Convert a PIL Image to a base64-encoded string
        with BytesIO() as buffer:
            image.save(buffer, format="PNG")
            return base64.b64encode(buffer.getvalue()).decode("utf-8")

    def base64_to_image(self, base64_str):
        # Convert a base64-encoded string to a PIL Image
        try:
            image_data = base64.b64decode(base64_str)
            return Image.open(BytesIO(image_data))
        except Exception as e:
            print(f"Error decoding image: {e}")
            return None

    def load_games(self):
        # Load cached games from a JSON file
        try:
            with open("games_cache.json", "r") as file:
                self.games = json.load(file)
        except FileNotFoundError:
            self.games = []

    def save_games(self):
        # Save cached games to a JSON file
        with open("games_cache.json", "w") as file:
            json.dump(self.games, file)

    def on_close(self):
        # Save games to file and close the app
        self.save_games()
        self.root.destroy()

    def toggle_settings(self):
        # Show or hide the settings frame
        if self.settings_visible:
            self.settings_frame.pack_forget()
            self.settings_visible = False
        else:
            self.settings_frame.pack(side=tk.TOP, fill=tk.X, pady=5)
            self.settings_visible = True

    def toggle_dark_mode(self):
        # Toggle dark/light mode
        self.dark_mode = not self.dark_mode

        # Update colors based on mode
        if self.dark_mode:
            self.root.configure(bg="black")
            self.top_frame.configure(bg="gray20")
            self.left_frame.configure(bg="gray20")
            self.right_frame.configure(bg="gray10")
            self.game_details_label.configure(bg="gray10", fg="white")
            self.add_game_button.configure(bg="gray30", fg="white")
            self.game_listbox.configure(bg="gray30", fg="white")
            self.settings_button.configure(bg="gray20")
            self.settings_frame.configure(bg="gray20")
            self.mode_toggle.configure(bg="gray20", fg="white", selectcolor="black")
        else:
            self.root.configure(bg="white")
            self.top_frame.configure(bg="lightgray")
            self.left_frame.configure(bg="lightgray")
            self.right_frame.configure(bg="white")
            self.game_details_label.configure(bg="white", fg="black")
            self.add_game_button.configure(bg="lightgray", fg="black")
            self.game_listbox.configure(bg="white", fg="black")
            self.settings_button.configure(bg="lightgray")
            self.settings_frame.configure(bg="lightgray")
            self.mode_toggle.configure(bg="lightgray", fg="black", selectcolor="white")

if __name__ == "__main__":
    root = tk.Tk()
    app = GameLauncherApp(root)
    root.mainloop()