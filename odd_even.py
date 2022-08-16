#Program to find whether a number is even or odd
#Defining a function
def evenOdd(num):
    #check the condition for even number
    if num%2==0:
        return 'Even'
    #condition for odd number
    elif number%2!=0:
        return 'Odd'
#Taking input from user
number=int(input("Enter any number:"))
#calling the function
result=evenOdd(number)
#Printing the result
print(result)
