import os
import json

from data.card_data import CARD_DATA


key_list = ["index", "streak", "is_edited", "question", "answer"]
card_dict = { str(card[0]): dict(zip(key_list, card)) for card in CARD_DATA }


def read_file(path='data/card_data.json'):
    if os.path.exists(path):
        try:
            with open(path, encoding="utf-8") as data:
                data = json.load(data)
            return data
        except Exception as e:
            return f"Error: {e}"

def write_file(path='data/card_data.json', card_data=card_dict):
    if os.path.exists(path):
        try:
            with open(path, "w", encoding="utf-8") as data:
                json.dump(card_data, data, ensure_ascii=False, indent=4)
            return "save successful"
        except:
            return "Error: open() or json.dump() failed"


if __name__ == "__main__":
    write_file()

