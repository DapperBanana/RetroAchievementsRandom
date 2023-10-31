import requests
from bs4 import BeautifulSoup

# Create a session for making HTTP requests
session = requests.Session()

# Set up user credentials
UserName = 'TestUser9989'  # Replace with your username
Password = 'MailMan9989!'  # Replace with your password
User_API_Key = ''  # Initialize an empty API key

# Fetch the login page
login_url = 'https://retroachievements.org/login'
response = session.get(login_url)

# Parse the CSRF token from the login page
soup = BeautifulSoup(response.text, 'html.parser')
csrf_token = soup.find('input', {'name': '_token'})['value']

# Perform login
login_data = {
    '_token': csrf_token,
    'User': UserName,
    'password': Password
}
login_response = session.post(login_url, data=login_data, allow_redirects=True)

# Fetch the user profile page
profile_url = 'https://retroachievements.org/controlpanel.php'
profile_response = session.get(profile_url)

# Parse the user profile page
profile_soup = BeautifulSoup(profile_response.text, 'html.parser')

# Using a CSS selector to extract specific information
element = profile_soup.select_one("body > div:nth-child(5) > main > article > div > div:nth-child(4) > table > tbody > tr:nth-child(1) > td:nth-child(2) > input")
value = element['value'] if element else None

# Check if the login was successful
if value:
    print("Successful login!")
    User_API_Key = value
    print("Username: " + UserName)
    print("Password: " + Password)  # Note: Printing the password is not recommended in practice.
    print("Web API Key: " + User_API_Key)
else:
    print("Incorrect credentials...")
