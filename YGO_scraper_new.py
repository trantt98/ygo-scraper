from bs4 import BeautifulSoup
import requests
import json

url = "https://yugioh.fandom.com/wiki/Special:AllPages"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


table_body = soup.find_all(class_='mw-redirect', href=lambda x: x and '/wiki/' in x)
link_to_cards = ["https://yugioh.fandom.com" + link['href'] for link in table_body]


# ====================================================================================


def scrape_link(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')

    card_name = soup.find('h1', class_='page-header__title').find('span', class_='mw-page-title-main').text.strip()

    english_name_element = soup.select_one('tr.cardtablerow th.cardtablerowheader:contains("English") + td.cardtablerowdata')
    card_name_english = english_name_element.text.strip() if english_name_element else None

    german_name_element = soup.select_one('tr.cardtablerow th.cardtablerowheader:contains("German") + td.cardtablerowdata')
    card_name_german = german_name_element.text.strip() if german_name_element else None
    # card_name_german = card_name_german.replace("Check translation", "")

    japanese_name_element = soup.select_one('tr.cardtablerow th.cardtablerowheader:contains("Japanese") + td.cardtablerowdata')
    card_name_japanese = japanese_name_element.text.strip() if japanese_name_element else None
    # card_name_japanese = card_name_japanese.replace("Check translation", "")


    ############ card type does not work (it returns None) -> tbd: try to adapt it better
    # card_type_element = soup.select_one('tr.cardtablerow th.cardtablerowheader:contains("Card Type") + tdcardtablerowdata')
    # card_type_element = soup.select_one('th.cardtablerowheader:contains("Card Type") + td.cardtablerowdata')
    card_type_element = soup.select_one('th.cardtablerowheader:contains("Card Type") + td.cardtablerowdata')
    card_type = card_type_element.text.strip() if card_type_element else None

    attribute_element = soup.select_one('tr.cardtablerow th.cardtablerowheader:contains("Attribute") + td.cardtablerowdata')
    attribute = attribute_element.text.strip() if attribute_element else None

    property_element = soup.select_one('tr.cardtablerow th.cardtablerowheader:contains("Property") + td.cardtablerowdata')
    property = property_element.text.strip() if property_element else None

    types_element = soup.select_one('tr.cardtablerow th.cardtablerowheader:contains("Types") + td.cardtablerowdata')
    types = types_element.text.strip() if types_element else None

    level_element = soup.select_one('tr.cardtablerow th.cardtablerowheader:contains("Level") + td.cardtablerowdata')
    level = level_element.text.strip() if level_element else None

    attk_def = None # tbd

    passcode_element = soup.select_one('tr.cardtablerow th.cardtablerowheader:contains("Passcode") + td.cardtablerowdata')
    passcode = passcode_element.text.strip() if passcode_element else None

    card_effect_types_element = soup.select_one('tr.cardtablerow th.cardtablerowheader:contains("Card effect types") + td.cardtablerowdata')
    card_effect_types = card_effect_types_element.text.strip() if card_effect_types_element else None

    statuses_element = soup.select_one('tr.cardtablerow th.cardtablerowheader:contains("Statuses") + td.cardtablerowdata')
    statuses = statuses_element.text.strip() if statuses_element else None

    # card_descriptions_element = soup.select_one('tr.cardtablerow th.cardtablerowheader:contains("Statuses") + td.cardtablerowdata')
    # card_descriptions = card_descriptions


    return {"card_name": card_name, "card_name_english": card_name_english, "card_name_german":card_name_german,
            "card_name_japanese": card_name_japanese, "card_type": card_type, "attribute": attribute,
            "property": property, "types": types, "level": level, "passcode": passcode, "card_effect_types": card_effect_types,
            "statuses": statuses}





scraped_data = []

for link in link_to_cards:
    data = scrape_link(link)
    scraped_data.append(data)

with open('./Dataset/scraped_data.json', 'w') as json_file:
    json.dump(scraped_data, json_file, indent=4)

print("Scraping and saving to JSON file complete")










print(scrape_link('https://yugioh.fandom.com/wiki/Red_Cocoon'))