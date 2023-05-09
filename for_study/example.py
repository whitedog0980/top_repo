h = int(input("Layers :"))
n = []
t = []

for i in range (h):
    n.append(1)
    t.append(1)
    print("  " * (h - i), end="")
    if i < 2:
        pass
    else:
        for j in range(1, len(n) - 1):
            t[j] = n[j - 1] + n[j]

    for j in range(len(n)):
        n[j] = t[j]
        if len(str(n[j])) == 3:
            print(" " + str(n[j]), end="")
        if len(str(n[j])) == 2:
            print("  " + str(n[j]), end="")
        if len(str(n[j])) == 1:
            print("   " + str(n[j]), end="")

    print("")