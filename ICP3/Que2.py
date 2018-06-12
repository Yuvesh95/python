#icp-3

""" Que-2"""



import requests
from bs4 import BeautifulSoup

my_list=[] #used to store the links

my_link="https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
# our link which we want to print
link=requests.get(my_link)
# requesting the link

obj=BeautifulSoup(link.content,"html.parser")
 #print the title of the webpage
print(obj.title)
my_list.append(obj.find_all('a'))
# collecting data/links on to list
#goes through each  'a' to get the reference
for i in obj.find_all('a'):
    print(i.get('href'))

#c=finds the table and prints the table data.
table = obj.find("table", { "class" : "wikitable sortable plainrowheaders" })
for row in table.findAll("tr"):
    cells = row.findAll("td")
    heading = row.findAll("th")
    # we are checking all contents in tables
    print(cells,heading)