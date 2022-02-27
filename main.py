import turtle
from states import States
from scoreboard import Scoreboard
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
csv_file = "50_states.csv"
turtle.shape(image)
turtle.penup()

# Initializing classes
states = States()
scoreboard = Scoreboard()

# print(answer_state)

# Working with csv file
states.get_csv_data()
player_guesses = []

while len(player_guesses) < 50:

    # TODO: Get the input/Guess from user and change it to Title Case
    answer_state = screen.textinput(title=f"{len(player_guesses)}/50 States correct", prompt="What's another state's name?").title()

    # Checking the guess with States list.
    if answer_state == "Exit":
        missing_states = [state for state in states.states_list if state not in player_guesses]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in states.states_list:
        # Adding the correct guesses in the list.
        if answer_state not in player_guesses:
            player_guesses.append(answer_state)

            answer_state_index = states.states_list.index(answer_state)
            answer_state_xcor = states.states_xcor_list[answer_state_index]
            answer_state_ycor = states.states_ycor_list[answer_state_index]

            states.write_state_name(answer_state_xcor, answer_state_ycor, answer_state)

