import turtle
import random

# Setup turtle environment
window = turtle.Screen()
window.bgcolor("black")
mandala = turtle.Turtle()
mandala.speed(0)  # Fastest drawing speed

# Function to draw a circle with a given radius, position, and color
def draw_circle(radius, position, color):
    mandala.penup()
    mandala.goto(position, -radius)  # Move to the starting position
    mandala.pendown()
    mandala.color(color)
    mandala.begin_fill()
    mandala.circle(radius)
    mandala.end_fill()

# Function to generate a mandala pattern
def generate_mandala(layers, max_radius):
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    for i in range(layers):
        radius = max_radius * (i + 1) / layers
        color = random.choice(colors)
        for j in range(i * 6):
            angle = 360 / (i * 6) * j
            mandala.setheading(angle)
            draw_circle(radius / 4, mandala.pos()[0], color)

# Generate a random mandala
layers = random.randint(5, 10)  # Number of layers
max_radius = 100  # Maximum radius of the circles
generate_mandala(layers, max_radius)

mandala.hideturtle()
turtle.done()

