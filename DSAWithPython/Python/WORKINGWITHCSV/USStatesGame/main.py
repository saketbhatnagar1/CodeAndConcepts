# import turtle
# import pandas
# screen = turtle.Screen()

# screen.title("US STATES GAME")
# image = "blank_states_img.gif"
# screen.addshape(image)
# turtle.shape(image)

# # def get_coordinates(x,y):
# #     print(x,y) #Code to get the x and y values of the states coordinate son the background image
# # turtle.onscreenclick(get_coordinates)

# states_data = pandas.read_csv("50_states.csv")
# states = states_data["state"].to_list()
# states_dict = {}
# coordinates = states_data["x"]
# score = 0

# for state in states:
#     states_dict[state] = False
# def checkAnswer(answer_state):
#     answer_state = answer_state.title()
#     if answer_state in states_dict:
#           if not states_dict[answer_state]:
#                states_dict[answer_state] = True
#                return True
#     return False  
# def main_game():
#         global score
#         def game_logic(answer_state):
#             answer = checkAnswer(answer_state=answer_state)
#             if answer:
#                 score+=1
#                 screen.textinput(title=f"{score}/50",prompt="What is another state")
#             if score == 50:
#                 return 
#             else:
#                 answer_state = screen.textinput(title=f"{score}/50",prompt="invalid response")
#                 game_logic(answer_state=answer_state)
#         answer_state = screen.textinput(title="Welcome",prompt="Enter the states name")
#         game_logic(answer_state=answer_state)
# main_game() 

# turtle.mainloop()









# print("EG")













###############################################################################################

import pandas
import turtle
screen = turtle.Screen()
screen.title("US STATES GAME")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_state = []
while len(guessed_state)<50:
    answer_state = screen.textinput(title="Guess the State",prompt="Enter the states name")
    print(answer_state)

    if answer_state in all_states and answer_state not in guessed_state :
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(answer_state)


    turtle.mainloop()
