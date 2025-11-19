from src.card import Card
from src.json_handler import write_file


class Logic:
    def __init__(self, cards: dict, start_bucket: set, learning_bucket: set, three_correct_bucket: set):
        self.all_cards = [Card(**data) for data in cards.values()]
        self.start_bucket = []
        self.learning_bucket = []
        self.three_correct_bucket = []
        for card in self.all_cards:
            if card.index in start_bucket:
                self.start_bucket.append(card)
            elif card.index in learning_bucket:
                self.learning_bucket.append(card)
            elif card.index in three_correct_bucket:
                self.three_correct_bucket.append(card)
        self.current_bucket = self.start_bucket
        self.cards_list = list(self.current_bucket)
        self.current_card_index = 0
        self.current_card = self.cards_list[self.current_card_index]
        self.is_answer_revealed = False
        self.card_content = self.current_card.question
        self.show_right_button = False
        self.show_wrong_button = False
        self.card_data = []
        self.key_list = ["index", "streak", "is_edited", "question", "answer"]
        self.card_dict = {}

    def update(self):
        self.cards_list = list(self.current_bucket)
        self.current_card = self.cards_list[self.current_card_index]
        self.card_content = self.current_card.answer if self.is_answer_revealed else self.current_card.question

    def next_card(self):
        self.current_card_index += 1
        self.current_card_index %= len(self.current_bucket)
        self.is_answer_revealed = False
        self.update()

    def flip_card(self):
        self.is_answer_revealed = not self.is_answer_revealed
        if self.is_answer_revealed:
            self.activate_feedback_buttons()
        else:
            self.deactivate_feedback_buttons()
        self.update()

    def prev_card(self):
        self.current_card_index -= 1
        self.current_card_index %= len(self.current_bucket)
        self.is_answer_revealed = False
        self.update()

    def get_answer_right(self):
        if not self.current_card.is_edited:
            if len(self.current_card.streak) == 3:
                self.current_card.streak.pop(0)
            self.current_card.streak.append(True)
        self.current_card.is_edited = True
        self.deactivate_feedback_buttons()

    def get_answer_wrong(self):
        if not self.current_card.is_edited:
            if len(self.current_card.streak) == 3:
                self.current_card.streak.pop(0)
            self.current_card.streak.append(False)
        self.current_card.is_edited = True
        self.deactivate_feedback_buttons()

    def activate_feedback_buttons(self):
        if not self.current_card.is_edited:
            self.show_right_button = True
            self.show_wrong_button = True

    def deactivate_feedback_buttons(self):
        if self.current_card.is_edited:
            self.show_right_button = False
            self.show_wrong_button = False

    def change_to_bucket(self, bucket):
        if bucket:
            self.current_bucket = bucket
            self.update()
        else:
            print("Bucket couldn't be selected because it is empty. ")

    def update_card_data(self):
        self.card_data = [[card.index, card.streak, card.is_edited, card.question, card.answer] for card in self.all_cards]

    def update_card_dict(self):
        self.update_card_data()
        self.card_dict = { str(card[0]): dict(zip(self.key_list, card)) for card in self.card_data }

    def save_card_data(self):
        self.update_card_dict()
        write_file(path='data/card_data.py', card_data=self.card_data)

