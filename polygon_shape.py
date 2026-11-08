"""Regular polygon drawing with the turtle module."""
import turtle


class Polygon:
    def __init__(self, x, y, sides, side_length, color, pen_size=3, angle=0):
        """Create a polygon, rejecting invalid side counts and dimensions."""
        if sides < 3:
            raise ValueError("A polygon must have at least 3 sides.")

        if side_length <= 0:
            raise ValueError("Side length must be positive.")

        if pen_size <= 0:
            raise ValueError("Pen size must be positive.")

        self.x = x
        self.y = y
        self.sides = sides
        self.side_length = side_length
        self.color = color
        self.pen_size = pen_size
        self.angle = angle

        self.pen = turtle.Turtle()

    def draw(self):
        """Draw the regular polygon from its first vertex."""
        self.pen.penup()
        self.pen.goto(self.x, self.y)
        self.pen.setheading(self.angle)
        self.pen.color(self.color)
        self.pen.pensize(self.pen_size)
        self.pen.pendown()

        for _ in range(self.sides):
            self.pen.forward(self.side_length)
            self.pen.left(360 / self.sides)

        self.pen.penup()

    def move_to(self, x, y):
        """Move this polygon by clearing and redrawing it at the new vertex."""
        self.x = x
        self.y = y

        self.pen.clear()
        self.draw()
