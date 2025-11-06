
class Logic:
    def __init__(self, cards: dict, start_bucket: set, learning_bucket: set, three_correct_bucket: set):
        self.all_cards = [Card(**data) for data in cards.values(self)]
        self.start_bucket = start_bucket
        self.learning_bucket = learning_bucket
        self.three_correct_bucket = three_correct_bucket
        self.current_bucket = start_bucket
        self.cards = list(self.current_bucket)
        self.current_card_index = 0
        self.current_card = self.cards[current_card_index]
        self.is_answer_revealed = False
        self.card_content = self.current_card.answer if self.is_answer_revealed else self.current_card.question
        self.show_right_button = False
        self.show_wrong_button = False

    def update(self):
        self.cards = list(self.current_bucket)
        self.current_card = self.current_card[current_card_index]
        self.card_content = self.current_card.answer if self.is_answer_revealed else self.current_card.question

    def next_card(self):
        self.current_card_index += 1
        self.current_card_index %= len(self.current_bucket)
        return self.current_card

    def flip_card(self):
        self.is_answer_revealed = not self.is_answer_revealed

    def prev_card(self):
        self.current_card_index -= 1
        self.current_card_index %= len(self.current_bucket)
        return self.current_card

    def get_answer_right(self):
        card.streak.pop(0)
        card.streak.append(True)
        self.deactivate_feedback_buttons()

    def get_answer_wrong(self):
        card.streak.pop(0)
        card.streak.append(False)
        self.deactivate_feedback_buttons()

    def activate_feedback_buttons(self):
        if not current_card.is_edited:
            self.show_right_button = True
            self.show_wrong_button = True

    def deactivate_feedback_buttons(self):
        if current_card.is_edited:
            self.show_right_button = False
            self.show_wrong_button = False

    def change_to_start_bucket(self):
        self.current_bucket = self.start_bucket

    def change_to_learning_bucket(self):
        self.current_bucket = self.learning_bucket

    def change_to_three_correct_bucket(self):
        self.current_bucket = self.three_correct_bucket

