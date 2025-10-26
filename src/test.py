import json
from cards import CARDS


key_list = ["index", "question", "answer"]
card_dict = { str(c[0]): dict(zip(key_list, c)) for c in CARDS }


with open('src/cards.json', "w", encoding="utf-8") as cards:
    json.dump(card_dict, cards, ensure_ascii=False, indent=4, sort_keys=True)

