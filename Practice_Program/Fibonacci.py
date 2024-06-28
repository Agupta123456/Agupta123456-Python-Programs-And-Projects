# def fibo(n):
#     num1 = 0
#     num2 = 1
#     next_num = num2
#     count = 1
#
#     while count < n + 1:
#         print(next_num, end=" ")
#         count += 1
#         num1 , num2 = num2, next_num
#         next_num = num1 + num2
#
# print(fibo(5))

a, b = 0, 1
n = int(input("Enter number:  "))
print("Fibonacci series : ", a, b, end=" ")
for i in range(0, n):
    c = a + b
    a = b
    b = c
    print(c, end= " ")
print()

