from src.card import Card
from src.json_handler import write_file


class Logic:
    def __init__(self, cards: dict, buckets: dict):
        self.all_cards = [Card(**data) for data in cards.values()]
        self.bucket_dict = buckets
        self.start_bucket = []
        self.learning_bucket = []
        self.three_correct_bucket = []
        self.update_buckets()
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

    def sort_cards(self):
        pass
        # self.all_cards.sort()

    def next_card(self):
        self.current_card_index += 1
        self.current_card_index %= len(self.current_bucket)
        self.is_answer_revealed = False
        self.update()
        self.deactivate_feedback_buttons()

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
        self.deactivate_feedback_buttons()

    def get_answer(self, answer):
        if not self.current_card.is_edited:
            if len(self.current_card.streak) == 3:
                self.current_card.streak.pop(0)
            self.current_card.streak.append(answer)
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

    def update_buckets(self):
        for card in self.all_cards:
            if card.index in set(self.bucket_dict["start_bucket"]):
                self.start_bucket.append(card)
            elif card.index in set(self.bucket_dict["learning_bucket"]):
                self.learning_bucket.append(card)
            elif card.index in set(self.bucket_dict["three_correct_bucket"]):
                self.three_correct_bucket.append(card)

    def update_bucket_dict(self):
        self.bucket_dict = {}
        key_list = ["start_bucket", "learning_bucket", "three_correct_bucket"]
        bucket_list = [self.start_bucket, self.learning_bucket, self.three_correct_bucket]
        empty_dict = dict(zip(key_list, bucket_list))
        self.bucket_dict = {bucket_name: [card.index for card in bucket] for bucket_name, bucket in empty_dict.items()}

    def update_data(self):
        self.card_data = [[card.index, card.streak, card.is_edited, card.question, card.answer] for card in self.all_cards]  # creates a list with cards, each card being a list with it's values
        self.card_dict = { str(card[0]): dict(zip(self.key_list, card)) for card in self.card_data }  # creates a json ready dictionary with cards and current values

    def save_card_data(self):
        self.update_data()
        self.update_bucket_dict()
        self.update_buckets()
        card_data = write_file(card_data=self.card_dict)
        bucket_data = write_file(path="data/buckets.json", card_data=self.bucket_dict)

    def new_card(self):
        max_index = -1
        for card in self.all_cards:
            max_index = card.index if card.index > max_index else max_index
        index = max_index + 1
        streak = []
        is_edited = False
        question = input("question: ")
        answer = input("answer: ")
        card = Card(index, streak, is_edited, question, answer)
        self.all_cards.append(card)
        self.start_bucket.append(card)
        self.update_bucket_dict()

