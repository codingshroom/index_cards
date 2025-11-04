from gui import App
from logic import Logic
from card import Card

from src.json_handler import write_file, read_file


def main():
    cards, start_bucket, learning_bucket, three_correct_bucket = read_file()
    logic = Logic(cards, start_bucket, learning_bucket, three_correct_bucket)
    app = App()
    app.create_left_frame()
    app.create_right_frame()
    app.create_middle_frame()
    app.mainloop()
    

if __name__ == "__main__":
    main()

