import tkinter
import tkinter.messagebox
import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self, logic: object):
        super().__init__()
        self.logic = logic

        # configure window
        self.title("Index Card Learning System")
        self.geometry(f"{940}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)
        
    def create_left_frame(self):
        self.left_frame = ctk.CTkFrame(self, width=140, corner_radius=0)
        self.left_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.left_frame.grid_rowconfigure(4, weight=1)
        self.left_label = ctk.CTkLabel(self.left_frame, text="Buckets", font=ctk.CTkFont(size=20, weight="bold"))
        self.left_label.grid(row=0, column=0, padx=20, pady=(20, 40))
        self.left_button_1 = ctk.CTkButton(self.left_frame, text="Start", command=self.press_start_bucket_button)
        self.left_button_1.grid(row=1, column=0, padx=20, pady=40)
        self.left_button_2 = ctk.CTkButton(self.left_frame, text="Learning", command=self.press_learning_bucket_button)
        self.left_button_2.grid(row=2, column=0, padx=20, pady=40)
        self.left_button_3 = ctk.CTkButton(self.left_frame, text="Three Correct", command=self.press_three_correct_bucket_button)
        self.left_button_3.grid(row=3, column=0, padx=20, pady=40)

    def create_right_frame(self):
        self.right_frame = ctk.CTkFrame(self, width=140, corner_radius=0)
        self.right_frame.grid(row=0, column=3, rowspan=4, sticky="nsew")
        self.right_frame.grid_rowconfigure(4, weight=1)
        self.left_label = ctk.CTkLabel(self.right_frame, text="Menu", font=ctk.CTkFont(size=20, weight="bold"))
        self.left_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.right_button_1 = ctk.CTkButton(self.right_frame, text="Options", command=self.option_button)
        self.right_button_1.grid(row=1, column=0, padx=20, pady=10)

        self.appearance_mode_label = ctk.CTkLabel(self.right_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.right_frame, 
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
        
        self.prev_button = ctk.CTkButton(self.card_frame, text="Prev", command=self.press_prev_button)
        self.prev_button.grid(row=6, column=0, padx=(40,10), pady=(10, 40))

        self.flip_button = ctk.CTkButton(self.card_frame, text="Flip", command=self.press_flip_button)
        self.flip_button.grid(row=6, column=1, padx=10, pady=(10, 40))

        self.next_button = ctk.CTkButton(self.card_frame, text="Next", command=self.press_next_button)
        self.next_button.grid(row=6, column=2, padx=(10,40), pady=(10, 40))

        self.question_answer_label = ctk.CTkLabel(
            self.card_frame, 
            text=self.logic.card_content,
            font=ctk.CTkFont(size=16),
            )
        self.question_answer_label.configure(wraplength=400, justify="center")
        self.question_answer_label.grid(row=2, column=0, columnspan=3)

        self.wrong_button = ctk.CTkButton(self.card_frame, height=28, width=220, text="Wrong", command=self.press_wrong_button, fg_color="#C0392B", hover_color="#9B2A1F")
        self.right_button = ctk.CTkButton(self.card_frame, height=28, width=220, text="Right", command=self.press_right_button, fg_color="#27AE60", hover_color="#1E8031")

        # set default values
        self.appearance_mode_optionemenu.set("Dark")

    def press_prev_button(self):
        self.logic.prev_card()
        self.question_answer_label.configure(text=self.logic.card_content)
        self.wrong_button.grid_forget()
        self.right_button.grid_forget()

    def press_flip_button(self):
        self.logic.flip_card()
        self.question_answer_label.configure(text=self.logic.card_content)
        self.wrong_button.grid_forget()
        self.right_button.grid_forget()

    def press_next_button(self):
        self.logic.next_card()
        self.question_answer_label.configure(text=self.logic.card_content)
        self.wrong_button.grid_forget()
        self.right_button.grid_forget()

    def press_right_button(self):
        self.logic.get_answer_right()

    def press_wrong_button(self):
        self.logic.get_answer_wrong()

    def press_load_button(self):
        read_file()

    def press_save_button(self):
        write_file()

    def press_start_bucket_button(self):
        self.logic.change_to_start_bucket()

    def press_learning_bucket_button(self):
        self.logic.change_to_learning_bucket()

    def press_three_correct_bucket_button(self):
        self.logic.change_to_three_correct_bucket()

    def option_button(self):
        print("option button")





