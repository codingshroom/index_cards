import json


with open('src/cards.json', encoding="utf-8") as cards:
    data = json.load(cards)


print(data)

