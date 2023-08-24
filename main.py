# This is a sample Python script.
import requests
from bs4 import BeautifulSoup as bs
from jproperties import Properties
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def get_map_site_popularity():
    configs = Properties()
    with open('resources/vars.properties', 'rb') as config_file:
        configs.load(config_file)
        urlll = configs.get("url").data
        print(urlll)
        wr = requests.get(urlll)
        print(wr.status_code)
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    r = requests.get("https://habr.com/ru/articles/568334/")
    print(r.status_code)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_map_site_popularity()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


