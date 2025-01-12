import requests , re
from bs4 import BeautifulSoup
from datetime import datetime

current_year = datetime.now().year

while True:
    year = input("==> Which year do you want the best-selling "
                 "movie at the box office? (from 1977)\n")

    if int(year) > current_year :
        print(f"==> your number is out of the range.\nwe're in {current_year}!")
    elif int(year)<1977:
        print('==>There is no information available before 1977!')
    else:
        break

address = f"https://www.boxofficemojo.com/year/world/{year.strip()}/"
page = requests.get(address)
soup = BeautifulSoup( page.text, 'html.parser')

movie_name = soup.find_all('td',
                     class_='a-text-left mojo-field-type-release_group')
movie_sold_price = soup.find_all('td',
                                 class_='mojo-field-type-money')

title = soup.find('h1' , class_='mojo-gutter')

RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
ORANGE = "\033[35m"
BLUE = "\033[33m"

print(f"\033[1m\033[4m{title.text}:\033[0m")
for i in range(0,25):
    if i%2==1 :
        print(f" {i+1}. {BLUE}{movie_name[i].text}{RESET} - Worldwide: {BLUE}{movie_sold_price[i].text}{RESET}")
    else:
        print(f" {i+1}. {ORANGE}{movie_name[i].text}{RESET} - Worldwide: {ORANGE}{movie_sold_price[i].text}{RESET}")
