import requests
from bs4 import BeautifulSoup
import pandas as pd
  
# URL of the webpage to scrape
URL = "https://www.cricbuzz.com/cricket-match-squads/66278/rcb-vs-csk-24th-match-indian-premier-league-2023"

# Send a GET request to the URL and store the response in 'r'
r = requests.get(URL)
  
# Parse the HTML content using BeautifulSoup and store it in 'soup'
soup = BeautifulSoup(r.content, 'html5lib')

# Find the div containing the left team's players and store it in 'left_team_box'
left_team_box = soup.find('div', attrs={'class':'cb-col cb-col-50 cb-play11-lft-col'})

# Find the div containing the right team's players and store it in 'right_team_box'
right_team_box = soup.find('div', attrs={"class":"cb-col cb-col-50 cb-play11-rt-col"})

# Lists to store the players and their roles for the left team
left_players = []


# Extract the player names and roles for the left team
for row in left_team_box.find_all('div', attrs={'class': 'cb-col cb-col-100'}):
    main_div = row.find('div', attrs={'class':'cb-player-name-left'})
    all_text = main_div.text
    role = main_div.find('span').text.strip()
    player = all_text.replace(role, "").strip()

    left_players.append(player)


# Lists to store the players and their roles for the right team
right_players = []


# Extract the player names and roles for the right team
for row in right_team_box.find_all('div', attrs={'class': 'cb-col cb-col-100'}):
    main_div = row.find('div', attrs={'class':'cb-player-name-right'})
    all_text = main_div.text
    role = main_div.find('span').text
    player = all_text.replace(role, "").strip()

    right_players.append(player)


# Create a pandas DataFrame for the left team's players and roles
left_team_df = pd.DataFrame({
    'player': left_players,
})

# Create a pandas DataFrame for the right team's players and roles
right_team_df = pd.DataFrame({
    'player': right_players,
})


# Creating csv file from the data frames
left_team_df.to_csv('left_gang.csv', index=False)
right_team_df.to_csv('right_gang.csv', index=False)