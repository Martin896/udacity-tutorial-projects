try:
    print("Enter two numbers")
    a = int(input())
    b = int(input())
    sum = a + b
    print("The sum is ", sum)
except ValueError:
    print("invalid input")
finally:
    print("if you get invalid input then you have not entered correcrt input")
    print("If you got a result move to the next section")