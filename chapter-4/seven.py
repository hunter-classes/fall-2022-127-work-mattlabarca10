import turtle
wn = turtle.Screen()
pirate = turtle.Turtle()
for ang in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
  pirate.left(ang)
  pirate.forward(100)
print("The pirate's last heading was", pirate.heading())