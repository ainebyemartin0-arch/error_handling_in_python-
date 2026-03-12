#print(10/0)
try:
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))

    answer = num1/num2
except ZeroDivisionError:
    print("You can not divide a number by zero")
else:
    print(f"your answer is {answer}")
