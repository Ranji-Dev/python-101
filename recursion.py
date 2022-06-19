#`factorial of an number using recursion

def factorial(n):
    assert n>=0 and int(n)==n,'Enter an positive integer'
    if n == 0 or n== 1:
        return 1
    else:
        return n *factorial(n-1)
print(f"factorial is {factorial(9)}")