import time
import requests
from bs4 import BeautifulSoup
import pandas as pd

df = pd.DataFrame(columns=['Player', 'Salary', 'Year', 'Link', 'Born'])

counter = 0  # Counter variable to keep track of scraped players

for yr in range(2020, 2021):
    page_num = str(yr) + '-' + str(yr + 1) + '/'
    url = 'https://hoopshype.com/salaries/players/' + page_num
    response = requests.get(url)
    print(f"Response status code: {response.status_code}")  # Let's see if we get a successful response (200)

    soup = BeautifulSoup(response.text, 'html.parser')

    salary_table = soup.find('table', class_='hh-salaries-table-sortable')
    rows = salary_table.find_all('tr') if salary_table else []

    for row in rows[1:]:  # Skip the header row
        if counter >= 100:
            break  # Stop the loop if 100 players are scraped

        player = row.find('td', class_='name')
        if player and player.a:
            link = player.a['href'] if 'https://' in player.a['href'] else 'https://hoopshype.com' + player.a['href']
            name = player.a.text.strip()
        else:
            link, name = None, None

        df = df.append({
            'Player': name,
            'Salary': None,  # Will be filled later
            'Year': yr,
            'Link': link,
            'Born': None  # Will be filled later
        }, ignore_index=True)

        counter += 1  # Increment the counter

        if counter >= 100:
            break  # Stop the loop if 100 players are scraped

    if counter >= 100:
        break  # Stop the loop if 100 players are scraped

for i, row in df.iterrows():
    if row['Link'] is not None:
        print(f"Scraping details for player {i}: {row['Player']}")  # Print out the player being processed
        player_response = requests.get(row['Link'])
        player_soup = BeautifulSoup(player_response.text, 'html.parser')

        # Get Salary or Earnings
        salary = player_soup.find('b', text='Salary:')
        if salary is None:
            salary = player_soup.find('b', text='Earnings:')
        salary = salary.find_next('span', class_='player-bio-text-line-value').text.strip() if salary else 'N/A'

        # Get Born date
        born = player_soup.find('b', text='Born:')
        born = born.find_next('span', class_='player-bio-text-line-value').text.strip() if born else 'N/A'

        df.at[i, 'Salary'] = salary
        df.at[i, 'Born'] = born

        time.sleep(1)  # sleep for 1 second before next request

print(df)
df.to_csv('player_salaries_bs.csv', index=False)
