import turtle
import random

# Made by Santiago Paris
def start_game(x, y):
    if -100 < x < 100 and -100 < y < -60:
        global menu_active
        menu_active = False
        menu.clear()
        walter.write(f"Playerone = {playerone_score}          Playertwo = {playertwo_score}", align="center", font=("Pixellari", 24, "normal"))
    elif -100 < x < 100 and -140 < y < -100:
        ventana.bye()

def draw_menu():
    menu.goto(0, 60)
    menu.write("COLORED PONG", align="center", font=("Pixellari", 36, "bold"))
    menu.goto(0, 20)
    menu.write("by Santiago Paris", align="center", font=("Pixellari", 18, "normal"))
    menu.goto(0, -80)
    menu.write("PLAY", align="center", font=("Pixellari", 24, "normal"))
    menu.goto(0, -120)
    menu.write("EXIT", align="center", font=("Pixellari", 24, "normal"))


ventana = turtle.Screen()
colores = ["black", "blue", "red", "green", "yellow", "purple"]
fondo = random.choice(colores)

ventana.title("Colored Pong by Santiago Paris")
ventana.bgcolor(fondo)
ventana.setup(width=800, height=600)
ventana.tracer(0)


menu = turtle.Turtle()
menu.hideturtle()
menu.penup()
menu.color("white")
menu_active = True

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
ball.goto(0, 0)
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.dx = 0.15
ball.dy = 0.15

playerone_score = 0
playertwo_score = 0

walter = turtle.Turtle()
walter.speed(0)
walter.color("white")
walter.penup()
walter.hideturtle()
walter.goto(0, 260)

malla = turtle.Turtle()
malla.speed(0)
malla.color("white")
malla.goto(0, 400)
malla.goto(0, -400)


def playerone_up():
    y = playerone.ycor()
    playerone.sety(y + 20)

def playerone_down():
    y = playerone.ycor()
    playerone.sety(y - 20)

def playertwo_up():
    y = playertwo.ycor()
    playertwo.sety(y + 20)

def playertwo_down():
    y = playertwo.ycor()
    playertwo.sety(y - 20)

def exit_game():
    ventana.bye()


ventana.listen()
ventana.onkeypress(playerone_up, "w")
ventana.onkeypress(playerone_down, "s")
ventana.onkeypress(playertwo_up, "Up")
ventana.onkeypress(playertwo_down, "Down")
ventana.onkeypress(exit_game, "Escape")
ventana.onscreenclick(start_game)


draw_menu()
while menu_active:
    ventana.update()


while True:
    ventana.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        playerone_score += 1
        walter.clear()
        walter.write(f"Playerone = {playerone_score}          Playertwo = {playertwo_score}", align="center", font=("Pixellari", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        playertwo_score += 1
        walter.clear()
        walter.write(f"Playerone = {playerone_score}          Playertwo = {playertwo_score}", align="center", font=("Pixellari", 24, "normal"))

    if (340 < ball.xcor() < 350) and (playertwo.ycor() - 50 < ball.ycor() < playertwo.ycor() + 50):
        ball.dx *= -1
        ventana.bgcolor(random.choice(colores))

    if (-350 < ball.xcor() < -340) and (playerone.ycor() - 50 < ball.ycor() < playerone.ycor() + 50):
        ball.dx *= -1
        ventana.bgcolor(random.choice(colores))
