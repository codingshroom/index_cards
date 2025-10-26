import json


with open('data/card_data.json', encoding="utf-8") as cards:
    data = json.load(cards)


print(data)

