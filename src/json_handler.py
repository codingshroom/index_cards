import os
import json

from data.card_data import CARD_DATA


key_list = ["index", "question", "answer"]
card_dict = { str(c[0]): dict(zip(key_list, c)) for c in CARD_DATA }


def write_file(path='data/card_data.json'):
    if os.path.exists(path):
        try:
            with open(path, "w", encoding="utf-8") as cards:
                json.dump(card_dict, cards, ensure_ascii=False, indent=4)
            return "save successful"
        except:
            return "Error: open() or json.dump() failed"

def read_file(path='data/card_data.json'):
    if os.path.exists(path):
        try:
            with open(path, encoding="utf-8") as cards:
                data = json.load(cards)
            return data
        except Exception as e:
            return f"Error: {e}"


if __name__ == "__main__":
    write_file()

