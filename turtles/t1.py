import turtle

wn = turtle.Screen()

crush = turtle.Turtle()

for i in range(4):
  crush.forward(50)
  crush.right(90)


#second turtle to draw triangle
man = turtle.Turtle()
man.color("purple")
man.left(90)
man.forward(100)
man.right(120)
man.forward(100)
man.right(120)
man.forward(100)
man.right(120)

wn.exitonclick
wn.mainloop()