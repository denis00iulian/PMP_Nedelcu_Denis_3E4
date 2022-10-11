import matplotlib.pyplot as plt
import random

def rollDice(dice):
    randValue = random.random()
    if dice == 'B':
        if randValue < 3/10:
            return 's'
        else:
            return 'b'
    else:
        if randValue < 1/2:
            return 's'
        else:
            return 'b'

def getStatsFrom10Throws():
    ss, bs, sb, bb = 0, 0, 0, 0
    for i in range(10):
        a = rollDice('A')
        b = rollDice('B')
        if a == 's' and b == 's':
            ss += 1
        elif a == 'b' and b == 's':
            bs += 1
        elif a == 's' and b == 'b':
            sb += 1
        elif a == 'b' and b == 'b':
            bb +=1
    return ss, bs, sb, bb

ss, bs, sb, bb = [], [], [], []
n = list(range(100))

for i in range(100):
    a, b, c, d = getStatsFrom10Throws()
    ss.append(a)
    bs.append(b)
    sb.append(c)
    bb.append(d)
    
fig, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4)
ax1.bar(n, ss)
ax1.set_title("ss")
ax2.bar(n, bs)
ax2.set_title("bs")
ax3.bar(n, sb)
ax3.set_title("sb")
ax4.bar(n, bb)
ax4.set_title("bb")
plt.show()