#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 23:06:49 2020

@author: daviesb
"""

#%% import modules
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random as rand

#%% scrape metacritic

### set up dictionary for storing scraped data
games_dict = { 'game':[], 'score':[], 'platform':[], 'release_date':[] }

### loop through first X pages
pages = 10 # how many pages to loop through
for page in range(0, pages):
    url = 'https://www.metacritic.com/browse/games/score/metascore/all/all/filtered?view=condensed&page=' + str(page)
    user_agent = {'User-agent': 'Mozilla/5.0'} # required to prevent 403 error
    response = requests.get(url, headers=user_agent)
    soup = BeautifulSoup(response.text, 'html.parser')
    time.sleep(rand.randint(3,6))
    ### loop through each game on page, extracting relevant details
    for game in soup.find_all('tr', class_='expand_collapse'):
        games_dict['game'].append(game.find('h3').text)
        games_dict['score'].append(game.find('td', class_='score').text.strip())
        games_dict['platform'].append(game.find('span', class_='data').text.strip())
        games_dict['release_date'].append(game.find('td', class_='details').find_all('span')[3].text)
    
### convert to table and export
df_games = pd.DataFrame(games_dict)
# df_games.to_csv('data/games.csv', index=False)
