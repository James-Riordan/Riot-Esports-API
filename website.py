import requests
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from pprint import pprint

from typing import List
from typing import Dict


# go to https://lolesports.com/

pages = []


class RiotTournamentBot:
    def __init__(self) -> None:
        self.url = 'https://lolesports.com/'
        self.leagues = [
    {
        'name': 'LCS',
        'region': 'NORTH AMERICA',
        'url': 'lcs'
    },
    {
        'name': 'LEC',
        'region': 'EUROPE',
        'url': 'lec'

    },
    {
        'name': 'LCK',
        'region': 'KOREA',
        'url': 'lck'

    },
    {
        'name': 'LPL',
        'region': 'CHINA',
        'url': 'lpl'

    },
    {
        'name': 'LCS Academy',
        'region': 'NORTH AMERICA',
        'url': 'lcs-academy'

    },
    {
        'name': 'TCL',
        'region': 'TURKEY',
        'url': 'turkiye-sampiyonluk-ligi'

    },
    {
        'name': 'CBLOL',
        'region': 'BRAZIL',
        'url': 'cblol-brazil'

    },
    {
        'name': 'LLA',
        'region': 'LATIN AMERICA',
        'url': 'lla'

    },
    {
        'name': 'OPL',
        'region': 'OCEANIA',
        'url': 'oce-opl'

    },
    {
        'name': 'LJL',
        'region': 'JAPAN',
        'url': 'ljl-japan'

    },
    {
        'name': 'Worlds',
        'region': 'INTERNATIONAL',
        'url': 'worlds'

    },
    {
        'name': 'MSI',
        'region': 'INTERNATIONAL',
        'url': 'msi'

    },
    {
        'name': 'All-Star Event',
        'region': 'INTERNATIONAL',
        'url': 'all-star'

    },
    {
        'name': 'European Masters',
        'region': 'EUROPE',
        'url': 'european-masters'

    },
    {
        'name': 'TAL',
        'region': 'TURKEY',
        'url': 'turkey-academy-league'

    },
    {
        'name': 'PCS',
        'region': ['HONG KONG', 'MACAU', 'TAIWAN'],
        'url': 'pcs'
        
    }
]       
        self.is_website_up(self.url)

    def is_website_up(self, url: str) -> bool:

        code = urllib.request.urlopen(url).getcode()

        if code == 200:
            print(f'Success! Connected to {url}')
            return True
        else: 
            print(f"Error code: {code}")
            return False

    def league_schedule(self, league: str) -> str:
        url = self.url + 'schedule' + '?' + 'leagues=' + f'{league}'
        print(url)
        return url

    def league_schedules(self, leagues: list):

        leagueurl = self.url

        for league in leagues:
            if league in self.league_names:
                leagueurl += f'{league},'
            else:
                print(f'League: {league} not found')
        return leagueurl

    @property
    def league_names(self) -> List:
        league_names = []
        for league in self.leagues:
            league_names.append(league['name'])
        return league_names
            
    def getData(self, url):
        driver = webdriver.Chrome('./chromedriver')
        driver.get(url)
        page = driver.execute_script('return document.body.innerHTML')
        soup = BeautifulSoup(''.join(page), 'html.parser')
        print(soup.prettify())
        return soup

    def set_time_frame(self, start_date, end_date):
        pass

    def event_match_data(self, eventmatch: str):
        pass

    def event_date(self, eventdate: str):
        pass

    def event_data(self, url='https://lolesports.com/schedule?leagues=lcs'):
        data = self.getData(url).find_all('div', {'class': 'EventMatch'})
        pprint(data)

r1 = RiotTournamentBot()
lcs = r1.league_schedule('LCS')
r1.event_data()
