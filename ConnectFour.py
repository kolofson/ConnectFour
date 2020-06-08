import turtle

def colorSlot():
  pointer.fillcolor(player.lower())
  pointer.penup()
  counted = spotsTaken.count(list_value)
  spotsTaken.append(list_value)
  y = yCor[counted]
  pointer.goto(col, y)
  pointer.pendown()
  # Start Coloring for pieces
  pointer.begin_fill()
  pointer.circle(10)
  # End Coloring for pieces
  pointer.end_fill()  
  
def writePlayerTurn():
  text_turtle.clear()
  text_turtle.penup()
  text_turtle.goto(0, -80)
  text_turtle.pendown()
  text_turtle.write(player + "'s turn", align="center")
  text_turtle.penup()

win = turtle.Screen()
pointer = turtle.Turtle()
text_turtle = turtle.Turtle()
text_turtle.hideturtle()
pointer.color("black")
pointer.speed(3000)
pointer.penup()
pointer.goto(-100,100)

# Declaration
player = "Red"
list_value = 0
y = -55
xCor = [-75, -50, -25, 0, 25, 50, 75]
yCor = [-55, -30, -5, 20, 45, 70]
spotsTaken = []

# Set Up Board
pointer.pendown()
for i in range(4):
  pointer.fd(200)
  pointer.right(90)
  
pointer.penup()
# Add Slots
pointer.goto(-75, 70)
for i in range(6):
  pointer.setx(-75)
  for i in range(7):
    pointer.pendown()
    pointer.circle(10)
    pointer.penup()
    pointer.fd(25)
  pointer.sety(pointer.ycor() - 25)
# Display Player Turn  
pointer.hideturtle()

#Begin Game
while True:
  writePlayerTurn()
  while True:
    col = int(input("Which column?\n"))
    list_value = col
    if col >= 0 and col <= 6:
      col = xCor[col]
      colorSlot()
      if player.lower() == "red":
        player = "Yellow"
      else:
        player = "Red"
      break
    else:
      print("Non - Existant")
      
