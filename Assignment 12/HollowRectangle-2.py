m=int(input())
n=int(input())
row="+" + ("-" * n) + "+"
print(row)
for i in range(m):
    space = " " * n
    print("|" + space +"|")
print(row)