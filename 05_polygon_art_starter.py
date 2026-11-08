import turtle
import random
from polygon_shape import Polygon

screen = turtle.Screen()
screen.setup(850, 600)
screen.title("My Colorful Polygon Art")
screen.bgcolor("black")
screen.tracer(0)

colors = [
    "cyan", "turquoise", "orange", "yellowgreen",
    "deepskyblue", "salmon", "plum", "lightgreen",
    "gold", "pink", "white", "magenta"
]

rng = random.Random(12)

polygons = []

for _ in range(25):
    sides = rng.randint(3, 7)
    side_length = rng.randint(35, 110)

    x = rng.randint(-350, 260)
    y = rng.randint(-225, 180)

    color = rng.choice(colors)
    pen_size = rng.randint(1, 6)
    angle = rng.randint(0, 359)

    polygon = Polygon(
        x, y, sides, side_length, color, pen_size, angle
    )

    polygon.draw()
    polygons.append(polygon)

screen.update()
screen.mainloop()