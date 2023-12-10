import random 
stay = 0
switch = 0
for count in range(0,1000):
    x = random.randint(1,3)
    y = random.randint(1,3)
    for i in range(0,4):
        if x == i:
            if y == x:
                stay += 1
            else:
                switch += 1
print(f'stay: {stay}')
print(f'switch: {switch}')