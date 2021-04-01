import random
numStreaks = 0
test = 0


#running the experiment 10000 times

for exp in range(10000):
    flip = []
    for i in range(100): #list of 100 random heads/tails

        if random.randint(0,1) == 0:
            flip.append('H')
        else:
            flip.append('T')

    for j in range(100): #checking for streaks of 6 heads/tails

        if flip[j:j+6] == ['H','H','H','H','H','H']:
            numStreaks += 1
        elif flip[j:j+6] == ['T','T','T','T','T','T']:
            numStreaks += 1
        else:
            test += 1 #just to test the prog
            continue
print (test)
chance = numStreaks / 10000
print("chance of streaks of 6: %s %%" % chance )
