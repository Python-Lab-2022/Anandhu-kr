rows=int(input("enter the no.of steps:"))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        a = i * j
        print(a, end='  ')
    print()
