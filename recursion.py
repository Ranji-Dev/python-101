#`factorial of an number using recursion

# def factorial(n):
#     assert n>=0 and int(n)==n,'Enter an positive integer'
#     if n == 0 or n== 1:
#         return 1
#     else:
#         return n *factorial(n-1)
# print(f"factorial is {factorial(9)}")

# fibonacci number using recursion

# def fibonacci(n):
#     assert  n >= 0 and int(n)==n, ' Enter an valid interger'
#     if n in [0,1]:
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
# print(f"The Fibonacci value is {fibonacci(8)}")

#Sum of digits of an numberusing recursion

def sum(n):
    assert n>=0 and int(n)== n, 'print valid number'
    if n==0:
        return 0
    else:
        return int(n%10)+sum(int(n/10))
print(sum(127))