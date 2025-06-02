import turtle

ventana = turtle.Screen()

ventana.title("Colored Pong by Santiago Paris")
ventana.bgcolor("black")
ventana.setup(width=800, height=600)
ventana.tracer(0)

playerone = turtle.Turtle()
playerone.speed(0)
playerone.shape("square")
playerone.color("white")
playerone.penup()
playerone.goto(-350, 0)
playerone.shapesize(stretch_wid=5, stretch_len=1)

playertwo = turtle.Turtle()
playertwo.speed(0)
playertwo.shape("square")
playertwo.color("white")
playertwo.penup()
playertwo.goto(350, 0)
playertwo.shapesize(stretch_wid=5, stretch_len=1)


ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.dx = 0.1
ball.dy = 0.1

malla = turtle.Turtle()
malla.speed(0)
malla.color("white")
malla.goto(0,400)
malla.goto(0,-400)

def playerone_up():
    y = playerone.ycor()
    y = y + 20
    playerone.sety(y)

def playerone_down():
    y = playerone.ycor()
    y = y-20
    playerone.sety(y)


def playertwo_down():
    j = playertwo.ycor()
    j = j-20
    playertwo.sety(j)

def playertwo_up():
    j = playertwo.ycor()
    j = j + 20
    playertwo.sety(j)

ventana.listen()
ventana.onkeypress(playerone_up, "w")
ventana.onkeypress(playerone_down, "s")
ventana.listen()
ventana.onkeypress(playertwo_up, "Up")
ventana.onkeypress(playertwo_down, "Down")
while True:
    ventana.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    if ball.ycor() > 290:
        ball.dy = ball.dy * -1
    if ball.ycor() < -290:
        ball.dy = ball.dy * -1
    
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx = ball.dx * -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx = ball.dx * -1
        
