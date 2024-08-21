import turtle
import pandas as pd
screen = turtle.Screen()
screen.title("US States")
image = "C:/Users/prane/OneDrive/Desktop/pythonprojects/day-25-us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pd.read_csv("C:/Users/prane/OneDrive/Desktop/pythonprojects/day-25-us-states-game-start/50_states.csv")
state=data['state'].to_list()
guessstate=[]
while len(guessstate)<50:
 answer_state=screen.textinput(title=f"{len(guessstate)}/50",prompt="what's another state names?").title()
 if answer_state=="Exit":
   missing_states = [st for st in state if st not in guessstate]     
   for st in missing_states:    
        statedata = data[data.state == st]
        t1 = turtle.Turtle()
        t1.hideturtle()
        t1.penup()
        t1.goto(statedata.x.item(), statedata.y.item())
        t1.write(statedata.state.item())
   break
 
 if answer_state in state and answer_state not in guessstate:
    guessstate.append(answer_state)
    t=turtle.Turtle()
    t.hideturtle()
    t.penup()
    statedata=data[data.state==answer_state]
    t.goto(statedata.x.item(),statedata.y.item())
    t.write(statedata.state.item())
screen.exitonclick()
