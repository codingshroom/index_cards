import tkinter as tk

from cards import CARDS



class Card:
    def __init__(self, id: int, question: str, answer: str):
        self.id = id
        self.question = question
        self.answer = answer


class IndexCardApp:
    def __init__(self, root, cards):
        self.cards = []
        for card in cards:
            self.cards.append(Card(card[0], card[1], card[2]))
        self.current_card = 0
        self.is_revealed = False

        root.title("Index Card Learning System")

        self.question_label = tk.Label(
                root,
                text=self.cards[self.current_card].question,
                font=('Helvetica', 18),
                wraplength=600,
                justify='left'
                )
        self.question_label.pack(padx=20, pady=20, expand=True, fill='both')

        self.card_button = tk.Button(root, text="Flip", command=self.flip_card, font=('Helvetica', 16))
        self.card_button.pack()

        self.next_button = tk.Button(root, text="Next", command=self.next_card, font=('Helvetica', 16))
        self.next_button.pack()


    def flip_card(self):
        self.is_revealed = not self.is_revealed
        if self.is_revealed:
            self.question_label.config(text=self.cards[self.current_card].answer)
        else:
            self.question_label.config(text=self.cards[self.current_card].question)

    def next_card(self):
        self.current_card = (self.current_card + 1) % len(self.cards)
        self.is_revealed = False
        self.question_label.config(text=self.cards[self.current_card].question)



def main():
    window = tk.Tk()
    app = IndexCardApp(window, CARDS)
    window.mainloop()



if __name__ == "__main__":
    main()

