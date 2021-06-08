" Multiple Input Calculator (User-Friendly) "
" Made by Ameo Saha "
" Completed: 6/7/2021 9:40 PM "


# list_input asks the user for number inputs and validates if all the inputs are numbers. If a non-number
# is detected in the user's input through the isValidList function, then list_input is continuously called.
def list_input():
    numbers = list(input("Input the numbers you want to use!").split())
    while not isValidList(numbers):
        print("Invalid inputs. Make sure all inputs are numbers!")
        numbers = list(input("Input the numbers you want to use!").split())
    return numbers

# isValidList detects if a value in the user's input list is a non-number.
def isValidList(lst):
    if len(lst) != 2:
        return False
    for i in lst:
        if not i.isnumeric():
            return False
    return True

# addition adds all of the values from the user's input list
def addition():
    sum = 0
    nums = list_input()
    i = 0
    while i < len(nums):
        sum += float(nums[i])
        i += 1
    return sum

# subtraction subtracts all of the values from the user's input list
def subtraction():
    nums = list_input()
    difference = float(nums[0])
    i = 1
    while i < len(nums):
        difference -= float(nums[i])
        i += 1
    return difference

# multiplication multiplies all of the values from the user's input list
def multiplication():
    product = 1
    nums = list_input()
    i = 0
    while i < len(nums):
        product *= float(nums[i])
        i += 1
    return product

# division divides 2 inputs from the user's input list
def division():
    nums = list_input()
    try:
        if len(nums) == 2:
            quotient = float(nums[0]) / float(nums[1])
            return quotient
        else:
            print("More than 2 numbers! Try Again!")
            division()
    except ZeroDivisionError as ERROR:
        print("Divide by Zero Error! Try Again!")
        division()
        return

# main consists of a dictionary and once a key is called, the corresponding operation function is done. if the key isn't
# in the dictionary, then the operation is asked for repeatedly until a valid operation is inputted.
def main():
    cont = True
    opDict = {'+': addition,
              '-': subtraction,
              '*': multiplication,
              '/': division}
    print("Welcome to Ameo's Multi-Input Calculator!")
    print("For the division operation, only input 2 numbers please!")
    while cont:
        operation = input("What operation do you want to use (+, -, *, /)").strip()
        while operation not in opDict:
            print("Enter valid operation")
            operation = input("What operation do you want to use (+, -, *, /)").strip()
        print(opDict[operation]())
        cont = True if input("Do you want to continue? (y/n): ").lower() == 'y' else False


if __name__ == '__main__':
    main()
