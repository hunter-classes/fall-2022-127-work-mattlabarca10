import turtle

def hexagon(t,x,y,w,color,sidelen):
  t.penup()
  t.goto(x,y)
  t.pendown()
  t.width(w)
  t.color(color)
  for i in range(6):
      t.forward(sidelen) 
      t.right(60)

def ngon(t,numsides,x,y,w,color,sidelen):
  t.penup()
  t.goto(x,y)
  t.pendown()
  t.width(w)
  t.color(color)
  for i in range(numsides):
      t.forward(sidelen) 
      t.right(360/numsides)

wn = turtle.Screen()
crush = turtle.Turtle()
squirt=turtle.Turtle()


hexagon(crush,-50,0,1,"yellow",50)
hexagon(squirt,0,30,9,"orange",30)
ngon(crush,12,-50,-50,1,"brown",10)
ngon(squirt,8,-30,30,9,"pink",30)

wn.exitonclick()
wn.mainloop()