import turtle


wn =  turtle.Screen()
wn.bgcolor("black")


def draw_pattern(l, s, a, m, r, color):
  #
  t = turtle.Turtle()


  t.speed(1)
  t.shape("turtle")
  t.pencolor(color)

  t.forward(l)
  t.left(90)
  t.forward(l)
  t.left(90)
  t.forward(l)
  t.left(90)
  t.forward(200)






if __name__ == "__main__":
    draw_pattern(100,100,90,1,4,"orange")