# imports

# from json_handler import read_file, write_file


class Card:
    id: int
    streak: list # holds three booleans, fifo, like queue
    question: str
    answer: str


class Logic:
    all_cards: list # all cards in all buckets, might not be needed
    start_bucket: set
    learning_bucket: set
    three_correct_bucket: set
    cards: list # those in the current bucket (with a random order)
    current_card_index: int
    current_card: object # not sure if needed - might be perfectly fine to use index
    is_answer_revealed: bool
    card_content: str # will either be question or answer, depending on state of logic, being called by App
    show_right_button: bool
    show_wrong_button: bool
    
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


class App:
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

