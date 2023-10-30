import requests
from lxml import html
import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from PIL import Image, ImageTk
from io import BytesIO

# Define the URL of the website
url = 'https://retroachievements.org/gameList.php?c=2'

# Send an HTTP GET request to the URL
response = requests.get(url)

if response.status_code == 200:
    # Parse the HTML content of the page
    tree = html.fromstring(response.text)

    # Extract the table name
    table_name = tree.xpath('/html/body/div[2]/main/article/h2/span/text()')[0]

    # Extract the total number of rows to loop through
    total_rows_text = tree.xpath('/html/body/div[2]/main/article/div[1]/text()')[0]
    total_rows = int(total_rows_text.split()[0]) + 1

    # Initialize lists to store game IDs, game names, and image URLs
    game_ids = []
    game_names = []
    image_urls = []

    # Loop through rows and extract game IDs, game names, and image URLs
    for row_num in range(2, total_rows):
        # Game ID
        game_id_xpath = f'/html/body/div[2]/main/article/div[3]/table/tbody/tr[{row_num}]/td[1]/div/a'
        game_id_element = tree.xpath(game_id_xpath)[0]
        game_id = game_id_element.get('x-data').split("'")[-2].strip()

        # Game Name
        game_name_xpath = f'/html/body/div[2]/main/article/div[3]/table/tbody/tr[{row_num}]/td[1]/div/a/p'
        game_name = tree.xpath(game_name_xpath)[0].text_content().strip().replace('\n', '')

        # Image URL
        image_url_xpath = f'/html/body/div[2]/main/article/div[3]/table/tbody/tr[{row_num}]/td[1]/div/a/img'
        image_url = tree.xpath(image_url_xpath)[0].get('src')

        # Append cleaned game ID, game name, and image URL to lists
        game_ids.append(game_id)
        game_names.append(game_name)
        image_urls.append(image_url)

    # Create a DataFrame
    data = {
        'Game ID': game_ids,
        'Game Name': game_names,
        'Image URL': image_urls
    }

    df = pd.DataFrame(data)

    # Create a tkinter window
    root = tk.Tk()
    root.title("Scrollable Table with Images")

    # Create a canvas and a vertical scrollbar to scroll the canvas
    canvas = tk.Canvas(root)
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    canvas.grid(sticky='news')
    scrollbar.grid(row=0, column=1, sticky='ns')
    canvas.config(yscrollcommand=scrollbar.set)

    # Create a frame to hold the game names and images
    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor='nw')

    # Loop through the list of image URLs to download and display images
    for image_url, game_name in zip(image_urls, game_names):
        response = requests.get(image_url)
        if response.status_code == 200:
            # Open the image and convert it to an ImageTk.PhotoImage object
            img_data = BytesIO(response.content)
            img = Image.open(img_data)
            img_tk = ImageTk.PhotoImage(img)

            # Create a Label widget to hold the image
            img_label = tk.Label(frame, image=img_tk)
            img_label.image = img_tk  # Keep a reference to prevent garbage collection
            img_label.grid(row=game_names.index(game_name), column=0)

            # Create a Label widget to display the game name
            name_label = tk.Label(frame, text=game_name)
            name_label.grid(row=game_names.index(game_name), column=1)

    frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    # Start the tkinter main loop
    root.mainloop()

else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")
