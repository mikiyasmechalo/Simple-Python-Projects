import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. states game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
names = data['state'].to_list()
coordinates_x = data['x']
coordinates_y = data['y']

correct_guesses = []

while len(correct_guesses) < 50:
    answer = screen.textinput(f"{len(correct_guesses)}/50 States Correct", "What's another state name?").title()
    if answer:
        if answer == 'Exit':
            missing_states = [item for item in names if item not in correct_guesses]
            # missing_states = []  # above uses list comprehension
            # for state in names:
            #     if state not in correct_guesses:
            #         missing_states.append(state)
            new_data = pandas.DataFrame(missing_states)
            new_data.to_csv('not_answered_states.csv')
            break
        if answer in names:
            timmy = turtle.Turtle()
            timmy.penup()
            timmy.hideturtle()
            state = data[data.state == answer]
            timmy.goto(int(state.x), int(state.y))
            timmy.write(answer)
            # timmy.write(state.state.item()) optional
            correct_guesses.append(answer)

print(correct_guesses)
screen.exitonclick()

# code to get the coordinates of states from the turtle screen
# def get_mouse_click_coordinates(x, y):
#     print(x, y)
#
#
# turtle.onclick(get_mouse_click_coordinates)
# turtle.mainloop()
