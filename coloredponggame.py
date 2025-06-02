import turtle
import random
ventana = turtle.Screen()
colores = ["black", "blue", "red", "green", "yellow", "purple"]
fondo = random.choice(colores)

ventana.title("Colored Pong by Santiago Paris")
ventana.bgcolor(fondo)
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
ball.dx = 0.25
ball.dy = 0.25


# CONTADORES

playerone_score = 0
playertwo_score = 0

walter = turtle.Turtle()
walter.speed(0)
walter.color("white")
walter.penup()
walter.hideturtle()
walter.goto(0, 260)
walter.write(f"Playerone = {playerone_score}          Playertwo = {playertwo_score}", align="center", font=("Pixellari", 24, "normal"))

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
        playerone_score += 1
        walter.clear()
        walter.write(f"Playerone = {playerone_score}          Playertwo = {playertwo_score}", align="center", font=("Pixellari", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx = ball.dx * -1
        playertwo_score += 1
        walter.clear()
        walter.write(f"Playerone = {playerone_score}          Playertwo = {playertwo_score}", align="center", font=("Pixellari", 24, "normal"))

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < playertwo.ycor() + 50 and ball.ycor() > playertwo.ycor() - 50):
        ventana.bgcolor(random.choice(colores))
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < playerone.ycor() + 50 and ball.ycor() > playerone.ycor() - 50):
        ball.dx *= -1
        ventana.bgcolor(random.choice(colores))
        