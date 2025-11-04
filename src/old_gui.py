import tkinter
import tkinter.messagebox
import customtkinter as ctk

from src.json_handler import write_file, read_file


ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


class Card:
    def __init__(self, index: int, streak: list, question: str, answer: str):
        self.index = index
        self.question = question
        self.answer = answer
        self.streak = streak


class Logic:
    def __init__(self, cards: dict, start_bucket: set, learning_bucket: set, correct_bucket: set):
        self.cards = [Card(**data) for data in cards.values()]
        self.current_card_index = 0
        self.is_revealed = False
        self.show_card_content = ""
        self.show_right_button = False
        self.show_wrong_button = False
        self.start_bucket = ()
        self.learning_bucket = ()
        self.correct_bucket = ()

    def flip_card(self):
        # self.show = card.other_side
        return self.show_card_content

    def next_card(self):
        # self.show = cards[self.current_card_index + 1]
        return self.show_card_content

    def prev_card(self):
        # self.show = cards[self.current_card_index - 1]
        return self.show_card_content

    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Index Card Learning System")
        self.geometry(f"{940}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

    def create_sidebar_left(self):
        self.sidebar_left_frame = ctk.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_left_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_left_frame.grid_rowconfigure(4, weight=1)
        self.left_label = ctk.CTkLabel(self.sidebar_left_frame, text="Buckets", font=ctk.CTkFont(size=20, weight="bold"))
        self.left_label.grid(row=0, column=0, padx=20, pady=(20, 40))
        self.sidebar_left_button_1 = ctk.CTkButton(self.sidebar_left_frame, text="Start", command=self.start_bucket_button_event)
        self.sidebar_left_button_1.grid(row=1, column=0, padx=20, pady=40)
        self.sidebar_left_button_2 = ctk.CTkButton(self.sidebar_left_frame, text="Learning", command=self.learning_bucket_button_event)
        self.sidebar_left_button_2.grid(row=2, column=0, padx=20, pady=40)
        self.sidebar_left_button_3 = ctk.CTkButton(self.sidebar_left_frame, text="Three Correct", command=self.correct_bucket_button_event)
        self.sidebar_left_button_3.grid(row=3, column=0, padx=20, pady=40)

    def create_sidebar_right(self):
        self.sidebar_right_frame = ctk.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_right_frame.grid(row=0, column=3, rowspan=4, sticky="nsew")
        self.sidebar_right_frame.grid_rowconfigure(4, weight=1)
        self.left_label = ctk.CTkLabel(self.sidebar_right_frame, text="Menu", font=ctk.CTkFont(size=20, weight="bold"))
        self.left_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_right_button_1 = ctk.CTkButton(self.sidebar_right_frame, text="Options", command=self.option_button_event)
        self.sidebar_right_button_1.grid(row=1, column=0, padx=20, pady=10)

        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_right_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.sidebar_right_frame, 
                                                                       values=["Light", "Dark", "System"], 
                                                                       command=self.change_appearance_mode_event
                                                                       )
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 40))

    def create_middle_frame(self):
        self.middle_frame = ctk.CTkFrame(self, width=300, corner_radius=0)
        self.middle_frame.grid(row=0, rowspan=6, column=1, sticky="nsew", padx=20)
        self.middle_frame.grid_columnconfigure((0, 2), weight=1)
        self.middle_frame.grid_columnconfigure(1, weight=0)

        self.middle_frame.grid_rowconfigure(0, weight=1)

        self.card_frame = ctk.CTkFrame(self.middle_frame, width=220, corner_radius=0, fg_color="transparent") 
        self.card_frame.grid(row=0, column=1, sticky="nsew")
        self.card_frame.grid_columnconfigure(2, weight=0)
        for i in range(1, 6):
            self.card_frame.grid_rowconfigure(i, weight=1)

        self.card_label = ctk.CTkLabel(self.card_frame, text="Card", font=ctk.CTkFont(size=20, weight="bold"))
        self.card_label.grid(row=0, column=1, padx=20, pady=(20, 10))
        
        self.prev_button = ctk.CTkButton(self.card_frame, text="Prev", command=self.prev_button_event)
        self.prev_button.grid(row=6, column=0, padx=(40,10), pady=(10, 40))

        self.flip_button = ctk.CTkButton(self.card_frame, text="Flip", command=self.flip_button_event)
        self.flip_button.grid(row=6, column=1, padx=10, pady=(10, 40))

        self.next_button = ctk.CTkButton(self.card_frame, text="Next", command=self.next_button_event)
        self.next_button.grid(row=6, column=2, padx=(10,40), pady=(10, 40))

        self.question_answer_label = ctk.CTkLabel(
            self.card_frame, 
            text=self.cards[self.current_card].question,
            font=ctk.CTkFont(size=16),
            )
        self.question_answer_label.configure(wraplength=400, justify="center")
        self.question_answer_label.grid(row=2, column=0, columnspan=3)

        self.wrong_button = ctk.CTkButton(self.card_frame, height=28, width=220, text="Wrong", command=self.wrong_button_event, fg_color="#C0392B", hover_color="#9B2A1F")
        self.right_button = ctk.CTkButton(self.card_frame, height=28, width=220, text="Right", command=self.right_button_event, fg_color="#27AE60", hover_color="#1E8031")

        # set default values
        self.appearance_mode_optionemenu.set("Dark")

    def flip_card(self):
        self.is_revealed = not self.is_revealed
        if self.is_revealed:
            self.question_answer_label.configure(text=self.cards[self.current_card].answer)
            self.wrong_button.grid(row=5, column=0, columnspan=2, sticky="w", padx=(40, 10), pady=10)
            self.right_button.grid(row=5, column=1, columnspan=2, sticky="e", padx=(10, 40), pady=10)
        else:
            self.question_answer_label.configure(text=self.cards[self.current_card].question)
            self.wrong_button.grid_forget()
            self.right_button.grid_forget()
            
    def next_card(self):
        self.is_revealed = False
        self.current_card = (self.current_card + 1) % len(self.cards)
        self.question_answer_label.configure(text=self.cards[self.current_card].question)
        self.wrong_button.grid_forget()
        self.right_button.grid_forget()

    def prev_card(self):
        self.current_card = (self.current_card - 1) % len(self.cards)
        self.is_revealed = False
        self.question_answer_label.configure(text=self.cards[self.current_card].question)
        self.wrong_button.grid_forget()
        self.right_button.grid_forget()

    def prev_button_event(self):
        self.prev_card()

    def flip_button_event(self):
        self.flip_card()

    def next_button_event(self):
        self.next_card()

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


if __name__ == "__main__":
    cards = read_file()
    logic = Logic()
    app = App(cards)
    app.create_sidebar_left()
    app.create_sidebar_right()
    app.create_middle_frame()
    app.mainloop()

