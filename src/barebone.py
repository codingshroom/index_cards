import tkinter
import tkinter.messagebox
import customtkinter as ctk

from src.json_handler import write_file, read_file


class Card:
    def __init__(self, index: int, streak: list, question: str, answer: str):
        self.index = index
        self.streak = streak  # holds three booleans, fifo - like queue
        self.question = question
        self.answer = answer


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


class App:
    def __init__(self):
        super().__init__()
        
    def create_left_frame():
        # buttons for buckets, show which one is selected (maybe radio buttons)
        # start_bucket
        # learning_bucket
        # three_correct_bucket

    def create_right_frame():
        # buttons for options and control
        # load data button
        # save data button
        # appearance mode selection

    def create_middle_frame():
        # card framwork
        # answer/question label in the middle
        # right/wrong button - disappear if card shows question
        # prev, flip, next buttons

    def press_prev_button():
        # Logic.prev_card()
        # show card
        # forget right/wrong buttons

    def press_flip_button():
        # Logic.flip_card()
        # show card
        # forget right/wrong buttons

    def press_next_button():
        # Logic.next_card()
        # show card
        # forget right/wrong buttons

    def press_right_button():
        # Logic.get_answer_right()

    def press_wrong_button():
        # Logic.get_answer_wrong()

    def press_load_button():
        # read_file()

    def press_save_button():
        # write_file()

    def press_start_bucket_button():
        # Logic.change_to_start_bucket()

    def press_learning_bucket_button():
        # Logic.change_to_learning_bucket()

    def press_three_correct_bucket_button():
        # Logic.change_to_three_correct_bucket()


