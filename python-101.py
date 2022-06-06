#Give number is even or odd
#number = int(input("Enter the number: "))
#if number%2 ==0 :
#    print("The number is even ", number)
#else:
#    print("The number is odd ", number)


#Given number is positive or negative
#number = int(input("Enter the number: "))
#if number>0 :
#    print("The number is positive ", number )
#elif number == 0:
#    print("Zero")
#else:
#    print("The number is negative ", number)

#Given number is prime or not
#num = int(input("Enter a number: "))

# prime numbers are greater than 1
#if num > 1:
    # check for factors
#    for i in range(2, num):
#       if (num % i) == 0:
#            print(num, "is not a prime number")
#           print(i, "times", num // i, "is", num)
#           break
#   else:
#        print(num, "is a prime number")

# if input number is less than
# or equal to 1, it is not prime
#else:
#    print(num, "is not a prime number")

# Factorial of a number
#num = int(input("Enter a number: "))
#factorial = 1
#if num < 0:
#    print("No factorial")
#elif num ==0:
#    print("Factorial of 0 is 1")
#else:
#    for i in range(1,num + 1):
#        factorial = factorial *i
#        print("Factorial of ",num ,"is", factorial)

# Python program to find the factorial of a number provided by the user
# using recursion

#def factorial(x):
#    """This is a recursive function
#    to find the factorial of an integer"""

#    if x == 1:
#        return 1
#    else:
#        # recursive call to the function
#        return (x * factorial(x-1))


# change the value for a different result


# to take input from the user
#num = int(input("Enter a number: "))

# call the factorial function
#result = factorial(num)
#print("The factorial of", num, "is", result)

#factorial of a number(working method)

#num = int(input("Enter a number: "))

#factorial = 1

# check if the number is negative, positive or zero
#if num < 0:
#   print("Sorry, factorial does not exist for negative numbers")
#elif num == 0:
#   print("The factorial of 0 is 1")
#else:
#   for i in range(1,num + 1):
#       factorial = factorial*i
#   print("The factorial of",num,"is",factorial)

#list[] and tuples()
#lists are ordered
#lists can contain any arbitrary objects
#lists can be accessed by index
#lists can be nested
#lists are mutable
#lists are dynamic
#list

#family = ['amma','appa','anna','kids']
#print(family[0])
#print(family[1:3])
#print(family[::-1])
#print(family[-4:-1])
#print(family[:-1:2])

#nested listed indexing
#x = ['a',['bb',['ccc','ddd'],'ee','ff'],'g',['hh','ii'],'j']
#print(x[3][0])
#print(x[1][1][0])
#print(x[1][1:3])
#print(x[3][::-1])
#print(x[3],x[2])
#print(x[3][::-1][0])
#print(x[1][1][-2])

#list modifying

#x=['a','b','c','d','e','f']
#x[1:4]=[1,2,3,4,5,]
#print(len(x))
#print(x)

#x=['a','b','c','d','e','f']
#x[1]=[1,2,3,4,5]
#print(len(x))
#print(x)

#list prepending & appending
#x=['a','b','c','d','e','f']
#x+=['j','k']     #or x= x+['j','k'] appending
#print(x)

#x=['a','b','c','d','e','f']
#x=[1,2]+x    #prepending
#x += 'g'     #can add single string to the list
#x += [20]    # cannot add int like this x += 20
#print(x)
#print(x[2])
#x += 'xyz'
#print(x)

#x =['a','b']
#y= [1,2,3]
#print(len(x+y))
#print(x+y)      #or x.append(y)
#x.append(y)
#print(len(x))
#print(x)

#x=['a','b','c','d','e','f']
#x.insert(4,[25,'x','y','z'])
#print(x)

#TUPLES() execution is faster than list and safegaurd from changes which is unintended
## Indexing, slicing , range, reverse works like list
#a = 'ranjith'
#b = 25
#c = [1, 'a',5]
#print(a,b,c)

#magicswap
#a=2
#b=3
#a,b=b,a
#print(a)

# a=20
# b=5.5
# c=3+2j
# d='Hello'
# l= [a,b,c,d]
# print(l)
# print(len(l))
# l.append(100)
# print(l)
# print(len(l))
# l.insert(2,['india',[25,[min,'apple']]])
# print(l)
# print(len(l))
# l.extend([1,2,3])
# print(l)
# print(len(l))