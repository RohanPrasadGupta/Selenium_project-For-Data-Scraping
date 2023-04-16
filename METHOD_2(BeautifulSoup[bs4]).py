#i am using BeautidulShoup for the webscraping

import requests
from bs4 import BeautifulSoup
import html5lib
import csv

url = "https://rohanprasadgupta.w3spaces.com/"


#Step 1 Get the HTML

r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

#step 2 Parse the HTML

soup = BeautifulSoup(htmlContent,'html.parser')
#pretiffy allign all the tags and data in prettier form or Redable form
#print(soup.prettify)

#step 3 HTML Tree Traversal

paras = soup.find_all('p') #here p or we can use a tag for the anchors tags to get find on the page and display
#print(paras)
#print(soup.find('p')) #to get the 1st element of the page where the tag start with P
#print(soup.find('P')['id']) #herer we can find the class name or id name as mention in the box as changed 

#Now getting the text from the tags/Soup
#print(soup.find('p').get_text())  #this is for the particular paragraph tags that come first from the search

#now getting all the text element of the page..
#print(soup.get_text())

#getting all the links in the page from anchor tags
anchors = soup.find_all('a')
# # print(anchors)

all_links = set()

# for link in anchors:
#     print(link.get('href'))

filename = 'links.csv'
# Storing all links in set or list as set is bettew cause it does not repeat the link if appeared twice
for link in anchors:
    link_text = (link.get('href'))
    all_links.add(link_text)
print(all_links)

#loading all the links in csv file
with open(filename,'w',newline='') as csvfile:
    writer = csv.writer(csvfile)
    for link in anchors:
        writer.writerow([link.get('href')])


#Getting all the paragraph in a csv file
paragraphs = soup.find_all('p')
filename = "output.csv"
with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    for paragraph in paragraphs:
        writer.writerow([paragraph.text])

csvfile.close()



