from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.common.by import By

# Initialize dataframe with necessary columns
df = pd.DataFrame(columns=['Player', 'Salary', 'Year', 'Link', 'Born'])  # creates master dataframe

# Set the path to ChromeDriver
driver = webdriver.Chrome('E:\İndirilenler\chromedriver_win32')

counter = 0  # initialize counter variable

# Loop through specified range of years
for yr in range(2020, 2021):
    # Construct URL for each year
    page_num = str(yr) + '-' + str(yr + 1) + '/'
    url = 'https://hoopshype.com/salaries/players/' + page_num
    
    # Open the constructed URL in the browser controlled by Selenium
    driver.get(url)
    
    # Find player names and salaries using XPATH
    players = driver.find_elements(by=By.XPATH, value='//td[@class="name"]/a')
    salaries = driver.find_elements(by=By.XPATH, value='//td[@class="hh-salaries-sorted"]')
    # Initialize lists to store players and salaries data
    players_list = []
    for p in range(len(players)):
        players_list.append(players[p].text)# Add each player's name to the list

    salaries_list = []
    for s in range(len(salaries)):
        salaries_list.append(salaries[s].text) # Add each player's salary to the list
    
    # Initialize list to store player profile links
    links_list = []
    for p in players:
        links_list.append(p.get_attribute('href'))  # Add each player's profile link to the list

    # Initialize list to store player birth dates
    born_list = []
    for link in links_list:
        driver.get(link)
        try:
             # Attempt to find and add player's birth date
            born = driver.find_element(by=By.XPATH, value='//b[text()="Born:"]/following-sibling::span').text
        except:
            born = 'Not Found'
        born_list.append(born)

        counter += 1  # increment counter

        if counter == 100:  # stop after scraping 100 records
            break

    # Combine the lists into a dataframe
    data_tuples = list(zip(players_list, salaries_list, links_list, born_list))
    temp_df = pd.DataFrame(data_tuples, columns=['Player', 'Salary', 'Link', 'Born'])
    temp_df['Year'] = yr    # Add year to the temporary dataframe
    df = df.append(temp_df)     # Append the temporary dataframe to the master dataframe

    if counter == 100:  # break out of the outer loop
        break

driver.close()

# Save the dataframe to a CSV file
df.to_csv(r'D:\Users\Onur\Desktop\ders\web scrapping\player_salaries.csv', index=False)
