import turtle as t
import math as m
import random as r
import time

# Screen
s = t.Screen()
s.setup(600, 600)
s.bgcolor("black")
s.tracer(0)

# Create stars
N = 500
stars = []

for i in range(N):
    a = 2 * m.pi * (i / N)

    # Heart equation
    base_x = 16 * (m.sin(a) ** 3) * 11
    base_y = (
        13 * m.cos(a)
        - 5 * m.cos(2 * a)
        - 2 * m.cos(3 * a)
        - m.cos(4 * a)
    ) * 11

    # Random starting position
    tx = base_x + r.uniform(-15, 15)
    ty = base_y + r.uniform(-15, 15)

    sx = r.randint(-320, 320)
    sy = r.randint(-320, 320)

    size = r.uniform(2.5, 5.5)

    stars.append((sx, sy, tx, ty, size))


# Turtle used to draw stars
p = t.Turtle()
p.hideturtle()
p.pencolor("#A855F7")
p.width(1.2)


def draw_star(x, y, size):
    for angle in (0, 45, 90, 135):
        rad = m.radians(angle)

        dx = size * m.cos(rad)
        dy = size * m.sin(rad)

        p.penup()
        p.goto(x - dx, y - dy)
        p.pendown()
        p.goto(x + dx, y + dy)


# Animation
steps = 50

for frame in range(steps + 1):
    p.clear()

    progress = frame / steps

    # Smooth animation
    ease = progress * progress * (3 - 2 * progress)

    for sx, sy, tx, ty, size in stars:
        x = sx + (tx - sx) * ease
        y = sy + (ty - sy) * ease

        draw_star(x, y, size)

    s.update()
    time.sleep(0.025)

s.update()
s.mainloop()