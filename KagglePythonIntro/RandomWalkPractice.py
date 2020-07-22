import random

def randomWalk(n):
    """Return coordinates after 'n' block random walk."""
    x = 0
    y = 0
    for i in range(n):
        step = random.choice(['N', 'S', 'E', 'W'])
        if step == 'N':
            y += 1
        elif step == 'S':
            y -= 1
        elif step == 'E':
            x += 1
        else:
            x -= 1
    return (x,y)
for i in range(25):
    walk = randomWalk(10)
    print(walk, "Distance from home = ", abs(walk[0]) + abs(walk[1]))

def randomWalk2(n):
    x, y = 0, 0
    for i in range(n):
        (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x += dx
        y += dy
    return (x,y)
for i in range(25):
    walk = randomWalk2(10)
    print(walk, "Distance from home with second walk = ", abs(walk[0]) + abs(walk[1]))

#Apply Monte Carlo Method
numberWalks = 10000
for walkLength in range(1, 31):
    noTransport = 0
    for i in range (numberWalks):
        (x, y) = randomWalk2(walkLength)
        distance = abs(x) + abs(y)
        if distance <= 4:
            noTransport += 1
    noTransportPercent = float(noTransport) / numberWalks
    print("Walk size = ", walkLength, " / % of no transport = ", 100 * noTransportPercent)