from turtle import Turtle, Screen
import pandas

ALIGNMENT = "center"
FONT = ("Courier", 10, "normal")


class States(Turtle):
    def __init__(self):
        super().__init__()
        self.states_ycor_list = []
        self.states_xcor_list = []
        self.states_file = None
        self.hideturtle()
        self.penup()
        self.csv_file = "50_states.csv"
        self.states_list = []

    def get_csv_data(self):
        self.states_file = pandas.read_csv(self.csv_file)

        self.states_list = self.states_file.state.to_list()
        self.states_xcor_list = self.states_file.x.to_list()
        self.states_ycor_list = self.states_file.y.to_list()
        # print(self.states_list)

    def write_state_name(self, x_cor, y_cor, state_name):
        self.goto(x_cor, y_cor)
        self.write(f"{state_name}", align=ALIGNMENT, font=FONT)