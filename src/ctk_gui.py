import tkinter
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

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
        self.prev_button.grid(row=6, column=0, padx=(40,10), pady=(10,40))

        self.flip_button = customtkinter.CTkButton(self.card_frame, text="Flip", command=self.flip_button_event)
        self.flip_button.grid(row=6, column=1, padx=10, pady=(10,40))

        self.next_button = customtkinter.CTkButton(self.card_frame, text="Next", command=self.next_button_event)
        self.next_button.grid(row=6, column=2, padx=(10,40), pady=(10,40))

        self.question_label = customtkinter.CTkLabel(
            self.card_frame, 
            text="Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. ", 
            font=customtkinter.CTkFont(size=16),
            )
        self.question_label.configure(wraplength=400, justify="center")
        self.question_label.grid(row=2, column=0, columnspan=3)


        # set default values
        self.appearance_mode_optionemenu.set("Dark")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def prev_button_event(self):
        print("go to last card")

    def flip_button_event(self):
        print("flip card")

    def next_button_event(self):
        print("go to next card")

    def start_bucket_button_event(self):
        print("show start bucket")

    def learning_bucket_button_event(self):
        print("show learning bucket")

    def correct_bucket_button_event(self):
        print("show correct bucket")

    def option_button_event(self):
        print("show options")


if __name__ == "__main__":
    app = App()
    app.mainloop()

