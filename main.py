from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.support.ui import Select


website = 'https://www.adamchoi.co.uk/teamgoals/detailed'
path = 'C:/Users/rohg5/OneDrive/Desktop/WEB_SCRAPPING/chromedriver'


#Chrome we used cause u have Chrome driver if i have donload other broswer then should be change, But Chrome works better so we are using this

driver = webdriver.Chrome(path)
driver.get(website)

#clicking the buttion to get the specific page to scrap the data
all_matches_button = driver.find_element_by_xpath("//label[@analytics-event = 'All matches']")
all_matches_button.click()

#Finding the element with tag names of the table data
#if multiple rows have the same Id so use elements not element so it will detect all te rows
matches = driver.find_elements_by_tag_name('tr')

date = []
home_team = []
score = []
away_team = []

for match in matches:
    date.append(match.find_element_by_xpath('./td[1]').text)
    home =match.find_element_by_xpath('./td[2]').text
    home_team.append(home)
    print(home) # we can use this too see if the data is scraping or not it is used as it make easier to debug the code faster
    score.append(match.find_element_by_xpath('./td[3]').text)
    away_team.append(match.find_element_by_xpath('./td[4]').text)

#it quit the web page after the scraping so use it after the code when u have fullay scraped the data from the web
driver.quit()

#Now creating a data frame using pandas

df = pd.DataFrame({'date':date,
              "home_team": home_team,
              "Score": score,
              "away_team":away_team})

#now sending the file in csv form
df.to_csv('football_data.csv', index= False)

print(df)