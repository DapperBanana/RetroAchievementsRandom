# Import necessary libraries for web scraping and GUI.
import requests
from lxml import html
import tkinter as tk
from tkinter import ttk, Text

# Function to extract game details from retroachievements.org.
def extract_game_details(game_id):
    # Construct URL using the provided game_id.
    url = f'https://retroachievements.org/game/{game_id}'
    response = requests.get(url)

    # Ensure the request was successful.
    if response.status_code == 200:
        tree = html.fromstring(response.content)

        # Extract basic game details using XPath queries.
        game_name = tree.xpath('/html/body/div[2]/main/article/div/h1/span/text()')[0].strip()
        game_system = tree.xpath('/html/body/div[2]/main/article/div/h1/div/div/span/text()')[0].strip()
        developer = tree.xpath('/html/body/div[2]/main/article/div/div[2]/div/div[1]/p[2]/a/text()')[0].strip()
        publisher = tree.xpath('/html/body/div[2]/main/article/div/div[2]/div/div[2]/p[2]/a/text()')[0].strip()
        genre_elements = tree.xpath('/html/body/div[2]/main/article/div/div[2]/div/div[3]/p[2]/a')
        game_genres = [{'ID': idx + 1, 'Genre': genre.text_content().strip()} for idx, genre in enumerate(genre_elements)]
        release_date = tree.xpath('/html/body/div[2]/main/article/div/div[2]/div/div[4]/p[2]/text()')[0].strip()

        # Extract achievement details.
        achievements_list = []
        achievement_elements = tree.xpath('/html/body/div[2]/main/article/div/ul/li')
        for idx, achievement in enumerate(achievement_elements):
            achievements_list.append({
                'ID': idx + 1,
                'Achievement Name': achievement.xpath('.//div[2]/div[1]/div/div/a/text()')[0],
                'Achievement Description': achievement.xpath('.//div[2]/div[1]/p/text()')[0],
                'Achievement Unlock Rate': achievement.xpath('.//div[2]/div[2]/p[1]/text()')[0]
            })

        # Extract details of similar games.
        similar_games_list = []
        similar_game_elements = tree.xpath('/html/body/div[2]/main/aside/div[3]/table/tbody/tr')
        for idx, similar_game in enumerate(similar_game_elements):
            similar_games_list.append({
                'ID': idx + 1,
                'Similar Game Name': similar_game.xpath('./td[1]/div/div/p/text()')[0],
                'Similar Game System': similar_game.xpath('./td[1]/div/div/div/span/text()')[0]
            })

        # Aggregate all extracted details.
        game_details = {
            'Game Name': game_name,
            'Game System': game_system,
            'Developer': developer,
            'Publisher': publisher,
            'Game Genres': game_genres,
            'Release Date': release_date,
            'Achievements': achievements_list,  # Corrected variable name.
            'Similar Games': similar_games_list  # Corrected variable name.
        }

        return game_details

    # Handle unsuccessful requests.
    else:
        print(f"Failed to fetch the page for game ID {game_id}. Status code: {response.status_code}")
        return None

# Function to display extracted details in a tkinter GUI.
def display_in_gui(details):
    # Initialize main tkinter window.
    root = tk.Tk()
    root.title("Game Details")

    # Create main frame inside the window.
    frame = ttk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True)

    # Add scrollbar to the frame.
    scrollbar = ttk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Create a text widget for displaying game details.
    text_widget = Text(frame, wrap=tk.WORD, yscrollcommand=scrollbar.set, padx=10, pady=10)
    text_widget.pack(expand=True, fill=tk.BOTH)

    # Populate the text widget with game details.
    if details:
        for key, value in details.items():
            text_widget.insert(tk.END, f"{key}:\n")
            if isinstance(value, list):
                for item in value:
                    for sub_key, sub_value in item.items():
                        text_widget.insert(tk.END, f"    {sub_key}: {sub_value}\n")
                    text_widget.insert(tk.END, "\n")
            else:
                text_widget.insert(tk.END, f"    {value}\n")
            text_widget.insert(tk.END, "\n")

    # Make the text widget read-only.
    text_widget.config(state=tk.DISABLED)
    
    # Attach scrollbar to the text widget.
    scrollbar.config(command=text_widget.yview)

    # Start the tkinter main loop.
    root.mainloop()

if __name__ == "__main__":
    game_id = 10135
    details = extract_game_details(game_id)
    
    #If you want to display in the terminal...
    #if details:
    #    for key, value in details.items():
    #        if isinstance(value, list):
    #            print(key)
    #            for item in value:
    #                for sub_key, sub_value in item.items():
    #                    print(f"    {sub_key}: {sub_value}")
    #        else:
    #            print(f"{key}: {value}")

    # Display the details in a GUI window.
    if details:
        display_in_gui(details)
