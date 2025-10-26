import json
from data.card_data import CARD_DATA


key_list = ["index", "question", "answer"]
card_dict = { str(c[0]): dict(zip(key_list, c)) for c in CARD_DATA }


def writes():
    with open('data/card_data.json', "w", encoding="utf-8") as cards:
        json.dump(card_dict, cards, ensure_ascii=False, indent=4)

def reads():
    with open('data/card_data.json', encoding="utf-8") as cards:
        data = json.load(cards)


