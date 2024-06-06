import turtle
import random

mbappe=turtle.Turtle()
mbappe.pensize(8)
mbappe.shape("turtle")
mbappe.color("blue")
messi=turtle.Turtle()
messi.pensize(8)
messi.shape("turtle")
messi.color("red")


mbappe.penup()
mbappe.goto(-350,250)
mbappe.pendown()
messi.penup()
messi.goto(-350,-250)
messi.pendown()


mbappe.penup()
mbappe.fd(700)
mbappe.pendown()
mbappe.circle(60)
mbappe.penup()
mbappe.bk(700)
messi.penup()
messi.fd(700)
messi.pendown()
messi.circle(60)
messi.penup()
messi.bk(700)

dice = (1,2,3,4,5,6)

while mbappe.pos() < (350,250) and messi.pos() < (350,-250):
      diceOutcome1 = random .choice(dice)
      print("result of dice roll:", diceOutcome1)
      print("Number of steps")
      print(10*diceOutcome1)
      mbappe.fd(10*diceOutcome1)

      diceOutcome2 = random.choice(dice)
      print("result of dice roll",diceOutcome2)
      print("Number of steps")
      print(10*diceOutcome2)
      messi.fd(10*diceOutcome2)

      if mbappe.pos() >= (300,250):
            print("Player 1 wins")
            break
      elif messi.pos() >= (300,-250):
            print("Player 2 wins")
            break

turtle.done()
