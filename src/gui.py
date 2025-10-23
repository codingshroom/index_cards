import tkinter
import tkinter.messagebox
import customtkinter

from cards import CARDS


customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


class Card:
    def __init__(self, id: int, question: str, answer: str):
        self.id = id
        self.question = question
        self.answer = answer


class App(customtkinter.CTk):
    def __init__(self, cards):
        super().__init__()
        self.cards = [Card(card[0], card[1], card[2]) for card in cards]
        self.current_card = 0
        self.is_revealed = False

        # configure window
        self.title("Index Card Learning System")
        self.geometry(f"{940}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar_left frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Buckets", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 40))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Start", command=self.start_bucket_button_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=40)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Learning", command=self.learning_bucket_button_event)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=40)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, text="Three Correct", command=self.correct_bucket_button_event)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=40)

        # create sidebar_right
        self.sidebar_right_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_right_frame.grid(row=0, column=3, rowspan=4, sticky="nsew")
        self.sidebar_right_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_right_frame, text="Menu", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_right_button_1 = customtkinter.CTkButton(self.sidebar_right_frame, text="Options", command=self.option_button_event)
        self.sidebar_right_button_1.grid(row=1, column=0, padx=20, pady=10)

        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_right_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_right_frame, 
                                                                       values=["Light", "Dark", "System"], 
                                                                       command=self.change_appearance_mode_event
                                                                       )
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 40))

        # create middle_frame
        self.middle_frame = customtkinter.CTkFrame(self, width=300, corner_radius=0)
        self.middle_frame.grid(row=0, rowspan=6, column=1, sticky="nsew", padx=20)
        self.middle_frame.grid_columnconfigure((0, 2), weight=1)
        self.middle_frame.grid_columnconfigure(1, weight=0)

        self.middle_frame.grid_rowconfigure(0, weight=1)
        
        self.card_frame = customtkinter.CTkFrame(self.middle_frame, width=220, corner_radius=0, fg_color="transparent") 
        self.card_frame.grid(row=0, column=1, sticky="nsew")
        self.card_frame.grid_columnconfigure(2, weight=0)
        for i in range(1, 6):
            self.card_frame.grid_rowconfigure(i, weight=1)

        self.card_label = customtkinter.CTkLabel(self.card_frame, text="Card", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.card_label.grid(row=0, column=1, padx=20, pady=(20, 10))
        
        self.prev_button = customtkinter.CTkButton(self.card_frame, text="Prev", command=self.prev_button_event)
        self.prev_button.grid(row=6, column=0, padx=(40,10), pady=(10, 40))

        self.flip_button = customtkinter.CTkButton(self.card_frame, text="Flip", command=self.flip_button_event)
        self.flip_button.grid(row=6, column=1, padx=10, pady=(10, 40))

        self.next_button = customtkinter.CTkButton(self.card_frame, text="Next", command=self.next_button_event)
        self.next_button.grid(row=6, column=2, padx=(10,40), pady=(10, 40))

        self.question_label = customtkinter.CTkLabel(
            self.card_frame, 
            text="ready?", 
            font=customtkinter.CTkFont(size=16),
            )
        self.question_label.configure(wraplength=400, justify="center")
        self.question_label.grid(row=2, column=0, columnspan=3)

        self.wrong_button = customtkinter.CTkButton(self.card_frame, height=28, width=220, text="Wrong", command=self.wrong_button_event, fg_color="#C0392B", hover_color="#9B2A1F")
        self.wrong_button.grid(row=5, column=0, columnspan=2, sticky="w", padx=(40, 10), pady=10)

        self.right_button = customtkinter.CTkButton(self.card_frame, height=28, width=220, text="Right", command=self.right_button_event, fg_color="#27AE60", hover_color="#1E8031")
        self.right_button.grid(row=5, column=1, columnspan=2, sticky="e", padx=(10, 40), pady=10)

        # set default values
        self.appearance_mode_optionemenu.set("Dark")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def prev_button_event(self):
        self.prev_card()
        print("go to last card")

    def flip_button_event(self):
        self.flip_card()
        print("flip card")

    def next_button_event(self):
        self.next_card()
        print("go to next card")

    def right_button_event(self):
        print("right button")

    def wrong_button_event(self):
        print("wrong button")

    def start_bucket_button_event(self):
        print("show start bucket")

    def learning_bucket_button_event(self):
        print("show learning bucket")

    def correct_bucket_button_event(self):
        print("show correct bucket")

    def option_button_event(self):
        print("show options")

    def flip_card(self):
        self.is_revealed = not self.is_revealed
        if self.is_revealed:
            self.question_label.configure(text=self.cards[self.current_card].answer)
        else:
            self.question_label.configure(text=self.cards[self.current_card].question)

    def next_card(self):
        self.current_card = (self.current_card + 1) % len(self.cards)
        self.is_revealed = False
        self.question_label.configure(text=self.cards[self.current_card].question)

    def prev_card(self):
        self.current_card = (self.current_card - 1) % len(self.cards)
        self.is_revealed = False
        self.question_label.configure(text=self.cards[self.current_card].question)


if __name__ == "__main__":
    app = App(CARDS)
    app.mainloop()


