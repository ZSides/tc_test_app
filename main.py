import random
import time


print("Now I'm playing with myself!", end='')
x = random.randint(0, 20)
u = -1
msg = ""

while u != x:
    u = random.randint(0, 20)
    if x < u:
        msg = "My number is less than my number."
    elif x > u:
        msg = "My number is bigger than my number."
    else:
        msg = "I won."
    time.sleep(1)

print(msg)

