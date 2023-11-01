<h1>
  <img src="https://static.retroachievements.org/assets/images/ra-icon.webp" width="100" alt="Banner">
  RetroAchievements Scripts
</h1>

Assortment of random scripts to automate information extraction from [retroachievements.org](https://retroachievements.org/).

## :key: user-login.py

This script logs a user into [retroachievements.org](https://retroachievements.org/), fetches the user's profile page, and extracts the Web API Key.

1. **Libraries**: `requests` for HTTP requests, `BeautifulSoup` for HTML parsing.
2. **Steps**:
   - Create a session.
   - Fetch the login page to get the CSRF token.
   - Perform login with a POST request.
   - Fetch the profile page.
   - Parse the profile page to extract the Web API Key.
   - Print success message or error based on the result.

## :video_game: game-icon-extract.py

This script fetches a list of games and their icons from [retroachievements.org](https://retroachievements.org/), and displays them in a scrollable table using a Tkinter GUI.

1. **Libraries**: `requests`, `lxml` for HTTP requests and HTML parsing, `pandas` for data handling, `tkinter` for GUI rendering.
2. **Steps**:
   - Send an HTTP GET request to fetch the page content.
   - Parse the HTML to extract game IDs, names, and icon URLs.
   - Create a DataFrame to organize the data.
   - Set up a Tkinter window with a canvas, scrollbar, and frame.
   - Loop through image URLs to download images and display them alongside game names in the Tkinter window.
   - Start the Tkinter main loop to render the GUI.

Upon failure in fetching the page, an error message is printed to the console.

## :joystick: game-info-extract.py

This script scrapes detailed game information from a specific game page on [retroachievements.org](https://retroachievements.org/). It fetches and displays the game's basic details, achievements, and similar games in a scrollable window using the Tkinter GUI.

1. **Libraries**: `requests` and `lxml` for HTTP requests and HTML parsing, `tkinter` for GUI rendering.
2. **Steps**:
   - Construct the URL using the provided game ID.
   - Send an HTTP GET request to fetch the game page content.
   - Parse the HTML to extract game details, including name, system, developer, publisher, genres, release date, achievements, and similar games.
   - Organize the extracted data into dictionaries.
   - Set up a Tkinter window with a text widget and scrollbar.
   - Populate the text widget with the game details in a formatted manner.
   - Start the Tkinter main loop to render the GUI.

If the request fails or the page content cannot be parsed as expected, an error message is printed to the console.

