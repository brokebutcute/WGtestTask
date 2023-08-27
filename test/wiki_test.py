import requests
from bs4 import BeautifulSoup as bs
from jproperties import Properties
import pytest
import re

from test.model.WebsitePopularity import WebsitePopularity
from test.utils.SoftAsssert import SoftAssert


def get_wiki_table():
    configs = Properties()
    with open('test/resources/vars.properties', 'rb') as config_file:
        configs.load(config_file)
        url = configs.get('url').data
        response = requests.get(url)
        response.raise_for_status()
        soup = bs(response.content, 'html.parser')
        table = soup.find('table', {'class': 'wikitable'})
    return table


def format_test_data(scientific_notation):
    parts = scientific_notation.split('*')
    if len(parts) == 1:
        coefficient = parts[0].strip()
        exponent = 0
    else:
        coefficient = parts[0].strip()
        exponent = parts[1].strip()
    if '10^' in coefficient:
        coefficient = float(coefficient.replace('10^', ''))
        return 10 ** coefficient
    coefficient_value = float(coefficient)
    exponent_value = float(exponent.replace('10^', ''))
    decimal_value = coefficient_value * 10 ** exponent_value
    return decimal_value


def get_website_popularity_info_list(table):
    rows = table.find_all('tr')[1:]  # Skip the header row
    website_info_list = []
    for row in rows:
        columns = row.find_all('td')
        website_name = (columns[0].text.strip().split('[')[0])
        popularity_column = columns[1].text.strip()
        frontend_lang = columns[2].text.strip()
        backend_lang = columns[3].text.strip()
        cleaned_string = re.sub(r'\D', '', popularity_column)
        # Remove any trailing non-digit characters
        cleaned_string = re.match(r'\d+', cleaned_string).group()
        websites_count = int(cleaned_string)
        website_info = WebsitePopularity(website_name, websites_count, frontend_lang, backend_lang)
        website_info_list.append(website_info)
    return website_info_list


soft_assert = SoftAssert()

testdata = ['10^7', '1.5 * 10^7', '5 * 10^7', '10^8', '5 * 10^8', '10^9', '1.5 * 10^9']


@pytest.mark.parametrize('expected', testdata)
def test_get_map_site_popularity(expected):
    table = get_wiki_table()
    expected_decimal_number = format_test_data(expected)
    websites = get_website_popularity_info_list(table)
    for website in websites:
        soft_assert.assert_more(expected_decimal_number, website.popularity,
                                (f'{website.website_name} (Frontend:{website.frontend_language}'
                                 f'|Backend:{website.backend_language}) 'f'has {website.popularity} '
                                 f'unique visitors per month. (Expected more than {expected_decimal_number})'))
    soft_assert.assert_all()
