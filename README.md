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
