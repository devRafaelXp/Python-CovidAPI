from urllib.request import urlopen
from colorama import Fore
import urllib
import json
import datetime
import time
import os

os.system('clear')

class CoronaVirus:
    def __init__(self, country):
        self.country = country
        if self.verify_connection():
            self.get_cases()
        
    def verify_connection(self):
        try:
            self.url = urlopen(f'https://api.covid19api.com/dayone/country/{self.country}', timeout = 15)
        
        except urllib.error.HTTPError as err:
            print(err)
            return False
        
        except Exception as err:
            print(err)
            
        else:            
            self.source = json.loads(self.url.read())
            return True
        
    def get_cases(self):
        start = time.clock()
        for row in self.source: 
            for i in range(1):          
                date_time_obj = datetime.datetime.strptime(row["Date"][0:10], '%Y-%m-%d') 
                print(f'In {self.country.title().replace("-", " ")} on date {date_time_obj.date().strftime("%d/%m/%Y")}')
                print(f'{Fore.YELLOW}Confirmed{Fore.RESET}: {row["Confirmed"]}')
                print(f'{Fore.GREEN}Recovered{Fore.RESET}: {row["Recovered"]}')
                print(f'{Fore.RED}Deaths{Fore.RESET}: {row["Deaths"]}')
                print(f'{Fore.BLUE}Cases active{Fore.RESET}: {row["Active"]}')            
                print('--'*24)
            
            end = time.clock()
            click = str(input('Click to see next day: '))
            os.system('clear')

while True:
    print('Coronavirus in the world'.upper())
    country = str(input('Country: ')).lower().replace(' ', '-')
    c = CoronaVirus(country)    
