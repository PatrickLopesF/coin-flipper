import random

x = int(input("Number os coins: "))

randomlist = []
for i in range(0,x):
    n = random.randint(1,2)
    randomlist.append(n)
count_1 = 0
count_2 = 0
for n in randomlist:
    if n == 1:
        count_1 += 1
    else:
        count_2 += 1

y = (count_1/x)*100
z = (count_2/x)*100
print(str(y) + "% of the coins are tails.")
print(str(z) + "% of the coins are heads.")
print("Number of tails: " + str(count_1))
print("Number of heads: " + str(count_2))
