def fact(num1):
    sum=1
    while num1!=0:
        sum=sum*num1
        num1=num1-1

num1=int(input("Enter a number:"))
num2=int(input("Enter another number: "))
sum=num1+num2
subtraction=num1-num2
multiplication=num1*num2
division=num1/num2
factorial=fact(num1)
print("Sum: ", sum, "\nSubstraction: ", subtraction, "\nMultiplication: ", multiplication, "\nDivision: ", division,"\nFactorial: ", factorial)