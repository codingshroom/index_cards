import os
import json


def read_file(path='data/card_data.json'):
    if os.path.exists(path):
        try:
            with open(path, encoding="utf-8") as data:
                data = json.load(data)
            return data
        except Exception as e:
            return f"Error: {e}"

def write_file(path='data/card_data.json', card_data=None):
    if card_data is None:
        return "Error: no card_data. action aborted"
    if os.path.exists(path):
        try:
            with open(path, "w", encoding="utf-8") as file:
                json.dump(card_data, file, ensure_ascii=False, indent=4)
            return "save successful"
        except:
            return "Error: open() or json.dump() failed"


if __name__ == "__main__":
    pass

