import turtle

import winsound
wn = turtle.Screen()
wn.screensize(400,400)
wn.bgcolor("black")
wn.title("dhanwanth")
score_a=0
score_b = 0
#paddle
p = turtle.Turtle()
p.penup()
p.goto(-250,0)
p.shape("square")
p.shapesize(4)
p.pensize(8)
p.color("white")



m = turtle.Turtle()
m.penup()
m.goto(250,0)
m.shape("square")
m.shapesize(4)
m.pensize(8)
m.color("white")


ball=turtle.Turtle()
ball.speed(100)
ball.shape("circle")
ball.shapesize(1)
ball.color("red")
ball.penup()
ball.goto(0,0)

ball.dx = 2
ball.dy = -2


pen=turtle.Turtle()
pen.color("white")
pen.speed(0)
pen.hideturtle()
pen.penup()
pen.goto(0,200)
pen.write("a=0 , b=0",align="center",font=("bold",24,"normal"))
def p_up():
 y = p.ycor()
 y += 20
 p.sety(y)

def p_d():
     y = p.ycor()
     y -= 20
     p.sety(y)


def m_r():
    y = m.ycor()
    y -= 20
    m.sety(y)
def m_l():
    y = m.ycor()
    y += 20
    m.sety(y)

wn.listen()
wn.onkeypress(p_up,"w")
wn.onkeypress(p_d,"s")
wn.onkeypress(m_r, "j")
wn.onkeypress(m_l,"u")

while True:
    wn.update()


    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dx)

    if ball.ycor() > 200:
        ball.sety(200)
        ball.dy*=-1
        winsound.PlaySound("rugd",winsound.SND_ASYNC)
    if ball.ycor() < -200:
        ball.sety(-200)
        ball.dy*=-1
    if ball.xcor() >190:
        ball.goto(0,0)
        ball.dx*=-1
        score_b+=1
        pen.clear()
        pen.write("a={} , b={}".format(score_a,score_b), align="center", font=("bold", 24, "normal"))

    if ball.xcor() < -190:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("a={} , b={}".format(score_a, score_b), align="center", font=("bold", 24, "normal"))
    if (ball.xcor()> 120 and ball.xcor()<-120)and (ball.ycor()< m.ycor()+50,  ball.ycor()>m.ycor()-50):
        ball.setx(120)
        ball.dx*= -1
    if (ball.xcor() < -120 and ball.xcor()>120) and (ball.ycor() < p.ycor() + 50, ball.ycor() > p.ycor() - 50):
        ball.setx(-120)
        ball.dx *= -1



