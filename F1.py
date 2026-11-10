n = int(input("Enter a number: "))
p = len(str(n))
s = 0
t = n

while t > 0:
    d = t % 10
    s += d ** p
    t //= 10

if s == n:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
