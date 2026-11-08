import turtle
import random
import math
import time
from polygon_shape import Polygon


screen = turtle.Screen()
screen.setup(850, 600)
screen.title("Animated Polygon Art")
screen.bgcolor("black")
screen.tracer(0)

rng = random.Random(17)

colors = [
    "cyan",
    "springgreen",
    "orange",
    "deepskyblue",
    "plum",
    "yellow",
    "hotpink",
    "white"
]

shapes = []

for _ in range(18):
    x = rng.randint(-290, 210)
    y = rng.randint(-170, 120)

    shape = Polygon(
        x,
        y,
        rng.randint(3, 7),
        rng.randint(35, 90),
        rng.choice(colors),
        rng.randint(2, 5),
        rng.randint(0, 359)
    )

    shape.draw()

    phase = rng.random() * 6.28

    shapes.append((shape, x, y, phase))


for frame in range(150):
    for shape, home_x, home_y, phase in shapes:

        x = home_x + 45 * math.cos(frame * 0.07 + phase)
        y = home_y + 35 * math.sin(frame * 0.07 + phase)

        shape.move_to(x, y)

    screen.update()
    time.sleep(0.035)


screen.mainloop()