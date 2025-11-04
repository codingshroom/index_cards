class Card:
    def __init__(self, index: int, streak: list, question: str, answer: str):
        self.index = index
        self.streak = streak  # holds three booleans, fifo - like queue
        self.question = question
        self.answer = answer

