import requests
from bs4 import BeautifulSoup

session = requests.Session()

# Step 0: Set up the user credentials
UserName = 'TestUser9989'
Password = 'MailMan9989!'
User_API_Key = ''

# Step 1: Fetch the login page
login_url = 'https://retroachievements.org/login'
response = session.get(login_url)

# Step 2: Parse the CSRF token
soup = BeautifulSoup(response.text, 'html.parser')
csrf_token = soup.find('input', {'name': '_token'})['value']

# Step 3: Perform login
login_data = {
    '_token': csrf_token,
    'User': UserName,
    'password': Password
}
login_response = session.post(login_url, data=login_data, allow_redirects=True)

# Step 4: Fetch the profile page
profile_url = 'https://retroachievements.org/controlpanel.php'
profile_response = session.get(profile_url)

# Step 5: Parse the profile page
profile_soup = BeautifulSoup(profile_response.text, 'html.parser')

# Using the CSS selector from the JS path
element = profile_soup.select_one("body > div:nth-child(5) > main > article > div > div:nth-child(4) > table > tbody > tr:nth-child(1) > td:nth-child(2) > input")
value = element['value'] if element else None



if value:
    print("Successful login!")
    User_API_Key = value
    print("Username: " + UserName)
    print("Password: " + Password)
    print("Web API Key: " + User_API_Key)
else:
    print("Incorrect credentials...")
