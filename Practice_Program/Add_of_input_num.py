# Program for addition of number
n = int(input("Enter number:  "))
s = 0
for _ in str(n):
    s = s + n % 10
    n = n // 10


print(s)