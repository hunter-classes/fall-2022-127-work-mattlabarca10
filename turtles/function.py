import turtle

def square(t,x,y,w,color,sidelen):

  t.penup()
  t.goto(x,y)
  t.pendown()
  t.width(w)
  t.color(color)
  for i in range(4):
      t.forward(sidelen) 
      t.right(90)
  
def triangle(t,x,y,w,color,sidelen):

  t.penup()
  t.goto(x,y)
  t.pendown()
  t.width(w)
  t.color(color)
  for i in range(3):
      t.forward(sidelen) 
      t.right(120)

def hexagon(t,x,y,w,color,sidelen):
  t.penup()
  t.goto(x,y)
  t.pendown()
  t.width(w)
  t.color(color)
  for i in range(6):
      t.forward(sidelen) 
      t.right(60)

def ngon(t,x,y,w,color,sidelen,n):
  t.penup()
  t.goto(x,y)
  t.pendown()
  t.width(w)
  t.color(color)
  for i in range(n):
      t.forward(sidelen) 
      t.right(360/n)

wn = turtle.Screen()
crush = turtle.Turtle()

squirt=turtle.Turtle()
squirt.penup()
squirt.goto(100,100)
squirt.pendown()

square(crush,0,0,1,"red",50)
square(squirt,100,100,9,"green",30)
triangle(crush,-100,0,1,"purple",50)
triangle(squirt,0,100,9,"blue",30)
hexagon(crush,-50,0,1,"yellow",50)
hexagon(squirt,0,30,9,"orange",30)
ngon(crush,-50,-50,1,"brown",10,12)
ngon(squirt,-30,30,9,"pink",30,8)

wn.exitonclick()
wn.mainloop()