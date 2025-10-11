import tkinter as tk


class Card:
    def __init__(self, id: int, question: str, answer: str):
        self.id = id
        self.question = question
        self.answer = answer


class IndexCardApp:
    def __init__(self, root):
        self.cards = [
                    Card(0, "Lagerwirtschaft", "Planung, Organisation und Kontrolle von Lagerbeständen um den Waren- und Materialfluss in einem Unternehmen effizient zu steuern"), 
                    Card(1, "Materialwirtschaft", "Planung, Steuerung und Verwaltung der Materialbewegungen eines Unternehmens"), 
                    Card(2, "KANO-Modell", "Werkzeug zur Analyse von Kundenbedürfnissen und zur Verbesserung von Produkten/Leistungen"), 
                    Card(3, "Teile des KANO-Modells", "Basismerkmale, Leistungsmerkmale, Begeisterungsmerkmale, unerhebliche Merkmale, Rückweisungsmerkmale"), 
                    ]
        self.current_card = 0
        self.is_revealed = False

        root.title("Index Card Learning System")

        self.question_label = tk.Label(root, text=self.cards[self.current_card].question, font=('Helvetica', 24), width=30, height=5)
        self.question_label.pack(pady=20)

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
    app = IndexCardApp(window)
    window.mainloop()



if __name__ == "__main__":
    main()

