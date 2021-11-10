import random


print("Let's play a game.\nGuess my number!", end='')
x = random.randint(0, 20)
u = -1
msg = ""

while u != x:
    u = int(input(msg + "\n"))
    if x < u:
        msg = "My number is less than yours."
    elif x > u:
        msg = "My number is bigger than yours."
    else:
        msg = "You won."


print(msg)

