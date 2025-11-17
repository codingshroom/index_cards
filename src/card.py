class Card:
    def __init__(self, index: int, streak: list, is_edited: bool, question: str, answer: str):
        self.index = index
        self.streak = streak # holds three booleans, fifo - like queue
        self.is_edited = False # tracks whether bool has been added to self.streak in this session
        self.question = question
        self.answer = answer

    def __repr__(self):
        return f"{self.index=}\n{self.streak=}\n{self.is_edited=}\n{self.question=}\n"

