import string
import random
random_int = random.randint(0, 9)
print ("This is you random generated password: ")
for i in range(4):
    print (random.choice(string.ascii_letters), end="")
print (f"{random_int}-", end="")
for i in range(4):
    print (random.choice(string.ascii_letters), end="")
print (f"{random_int}-", end="")
for i in range(4):
    print (random.choice(string.ascii_letters), end="")
print (random_int, end="")