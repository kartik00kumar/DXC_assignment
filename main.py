#script starts here
'''
statement="sello ji"
print("The statement is - ",statement,"and its lenght is" , len(statement))

print(statement[0])

print(statement[1])
print(statement[2])

print(statement.capitalize())
print(statement.upper())
print(statement.lower())
print(statement.center(30))
print(statement.find('ji'))
print(statement.split())
print(statement.casefold())
'''
#Simple Calculator

first_number=int(input("Enter first Number\n"))
second_number=int(input("Enter Second Number\n"))
#print(first_number)
#print(second_number)
count=1
#print(operand)
while(count==1):

    operand = int(input("Select operation to be performed \n "
                        "1. Addition \n 2. Subtraction \n 3. Multiply \n 4. Divison \n 5. Remainder\n"))
    if (operand == 1):
        result = first_number + second_number
        print("The Answer is ", result)
    elif (operand == 2):
        result = first_number - second_number
        print("The Answer is ", result)
    elif (operand == 3):
        result = first_number * second_number
        print("The Answer is ", result)
    elif (operand == 4):
        result = first_number / second_number
        print("The Answer is ", result)
    elif (operand == 5):
        result = first_number % second_number
        print("The Answer is ", result)
    else:
        print("You can only select No. From 1 to 5 \n")

    count = int(input("Do you wish to continue ?\n 1. Yes \n 2. No \n"))







