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

def write_file(path='data/card_data.json', file_format="json", card_data=card_dict):
    if os.path.exists(path):
        try:
            with open(path, "w", encoding="utf-8") as file:
                if file_format == "json":
                    json.dump(card_data, file, ensure_ascii=False, indent=4)
                elif file_format == "py":
                    format_list = [str(card) for card in card_data]
                    formatted_card_data = ",\n\t\t".join(format_list)
                    new_content = "CARD_DATA = [\n\t\t" + formatted_card_data + "\n]"
                    breakpoint()
                    file.write(new_content)
                else:
                    return "Error: file_format incorrect. use 'json' or 'py'"
            return "save successful"
        except:
            return "Error: open() or json.dump() failed"


if __name__ == "__main__":
    write_file()

