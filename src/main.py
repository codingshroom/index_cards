import tkinter
import tkinter.messagebox
import customtkinter as ctk

from src.gui import App
from src.logic import Logic
from src.card import Card
from src.json_handler import write_file, read_file


ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


def main():
    cards, start_bucket, learning_bucket, three_correct_bucket = read_file()
    logic = Logic(cards, start_bucket, learning_bucket, three_correct_bucket)
    app = App()
    app.create_left_frame()
    app.create_right_frame()
    app.create_middle_frame()
    app.mainloop()
    

if __name__ == "__main__":
    main()

