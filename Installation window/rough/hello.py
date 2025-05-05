import turtle
#amul = turtle.Turtle()

wn = turtle.Screen()
#wn.bgcolor("Red")

wn.bgpic("background.jpg")

i = 1
num = int(input("Enter A Number Which You Want To Print It's Table: "))
final = int(input("Enter A range How many times You Want To Multiply: "))
total = 1
for i in range(1, final+1):
    total = num * i
    print(f"{num} * {i} = {total}")
    i = i + 1
