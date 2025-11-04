class Logic:
    def __init__(self, cards: dict, start_bucket: set, learning_bucket: set, three_correct_bucket: set):
        self.all_cards = [Card(**data) for data in cards.values()]
        self.start_bucket = start_bucket
        self.learning_bucket = learning_bucket
        self.three_correct_bucket = three_correct_bucket
        self.current_bucket = start_bucket
        self.cards = list(self.current_bucket)
        self.current_card_index = 0
        self.current_card = self.cards[current_card_index]
        self.is_answer_revealed = False
        self.card_content = ""
        self.show_right_button = False
        self.show_wrong_button = False

    def next_card():
        # increase current_card_index by one, looping around if at last index previously

    def flip_card():
        # switch bool on is_answer_revealed, change card_content accordingly

    def prev_card():
        # decrease current_card_index by one, looping around if at index 0 previously

    def get_answer_right():
        # add bool: right to card.streak
        # self.deactivate_feedback_buttons()

    def get_answer_wrong():
        # add bool: wrong to card.streak
        # self.deactivate_feedback_buttons()

    def deactivate_feedback_buttons():
        # if right or wrong button was clicked for current card and run
        # double or multi insertion should be prevented

    def change_to_start_bucket():
        # self.current_bucket = self.start_bucket

    def change_to_learning_bucket():
        # self.current_bucket = self.learning_bucket

    def change_to_three_correct_bucket():
        # self.current_bucket = self.three_correct_bucket

