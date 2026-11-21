#zadanie 16
import figures
import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

pen = turtle.Turtle()
pen.speed(5)

# Kwadraty
figures.draw_square(pen, 80)
pen.penup()
pen.goto(-150, 150)
pen.pendown()
figures.draw_square(pen, 60)

# Trójkąty
pen.penup()
pen.goto(100, 100)
pen.pendown()
figures.draw_trangle(pen, 90)
pen.penup()
pen.goto(-150, -100)
pen.pendown()
figures.draw_trangle(pen, 70)

# Prostokąty
pen.penup()
pen.goto(50, -100)
pen.pendown()
figures.draw_rectangle(pen, 120, 60)
pen.penup()
pen.goto(-50, 200)
pen.pendown()
figures.draw_rectangle(pen, 80, 40)

pen.hideturtle()
window.mainloop()