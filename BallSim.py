import pgzrun
from random import randint

TITLE = "Bouncy_Balls_Simulation"

WIDTH = 800
HEIGHT = 675

R = randint(0,255)
G = randint(0,255)
B = randint(0,255)
CLR = R,G,B

R2 = randint(0,255)
G2 = randint(0,255)
B2 = randint(0,255)
CLR2 = R2,G2,B2

GRAVITY = 2000.0

class Ball:
    def __init__(self, inital_x, initial_y):
        self.x = inital_x
        self.y = initial_y
        self.vx = 200
        self.vy = 0
        self.radius = 40

    def draw(self):
        pos = (self.x, self.y)
        screen.draw.filled_circle(pos,self.radius, CLR)


class Ball2:
    def __init__(self, inital_x2, initial_y2):
        self.x = inital_x2
        self.y = initial_y2
        self.vx = 200
        self.vy = 0
        self.radius2 = 40

    def draw(self):
        pos2 = (self.x, self.y)
        screen.draw.filled_circle(pos2,self.radius2, CLR2)


ball = Ball(50,100)
ball2 = Ball2(50,500)

def draw():
    screen.clear()
    ball.draw()
    ball2.draw()
    

def update(dt):
    uy = ball.vy
    ball.vy += GRAVITY * dt
    ball.y += (uy + ball.vy) * 0.5 * dt

    if ball.y > HEIGHT - ball.radius:
        ball.y = HEIGHT - ball.radius
        ball.vy = -ball.vy * 0.9

    ball.x += ball.vx * dt
    if ball.x > WIDTH - ball.radius or ball.x < ball.radius:
        ball.vx = -ball.vx

def on_key_down(key):
    if key == key.SPACE:
        ball.vy = -500
        ball2.vy = -500

def update2(dt2):
    uy2 = ball2.vy
    ball2.vy += GRAVITY * dt2
    ball2.y += (uy2 + ball2.vy) * 0.5 * dt2

    if ball2.y > HEIGHT - ball2.radius2:
        ball2.y = HEIGHT - ball2.radius2
        ball2.vy = -ball2.vy * 0.9

    ball2.x += ball2.vx * dt2
    if ball2.x > WIDTH - ball2.radius2 or ball2.x < ball2.radius2:
        ball2.vx = -ball2.vx

pgzrun.go()        

  
