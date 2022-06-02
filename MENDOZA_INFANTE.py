import random

correctAnswer = 0
j = 0


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


while True:
    print("Hi! This is your friendly Math Tutor, CalcuSensei.")
    choice1 = input(
        "First, indicate the number of problems you would like to solve: ")
    choice = input(
        "Enter the type of operation you would like to use (1 - Add, 2 - Sub, 3 - mult, 4 - divide): ")
    if choice in ('1', '2', '3', '4'):
        if choice == '1':
            while j < int(choice1):
                num1 = float(random.randint(0, 99))
                num2 = float(random.randrange(2, 98, 2))
                num3 = add(num1, num2)
                print("What is the sum of " + str(num1) + " and " + str(num2))
                answer = float(input("Enter your answer: "))
                if num3 == answer:
                    print("Correct")
                    correctAnswer += 1
                else:
                    print("Wrong! the correct answer is", num3)
                j += 1
        elif choice == '2':
            while j < int(choice1):
                num1 = float(random.randint(0, 9))
                num2 = float(random.randrange(2, 10, 2))
                num3 = subtract(num1, num2)
                print("What is the difference of " +
                      str(num1) + " and " + str(num2))
                answer = float(input("Enter your answer: "))
                if num3 == answer:
                    print("Correct")
                    correctAnswer += 1
                else:
                    print("Wrong! the correct answer is", num3)
                j += 1
        elif choice == '3':
            while j < int(choice1):
                num1 = float(random.randint(0, 9))
                num2 = float(random.randrange(2, 10, 2))
                num3 = multiply(num1, num2)
                print("What is the product of " +
                      str(num1) + " and " + str(num2))
                answer = float(input("Enter your answer: "))
                if num3 == answer:
                    print("Correct")
                    correctAnswer += 1
                else:
                    print("Wrong! the correct answer is", num3)
                j += 1
        else:
            while j < int(choice1):
                num1 = float(random.randint(0, 9))
                num2 = float(random.randrange(2, 10, 2))
                num3 = divide(num1, num2)
                print("What is the quotient of " +
                      str(num1) + " and " + str(num2))
                answer = float(input("Enter your answer: "))
                if num3 == answer:
                    print("Correct")
                    correctAnswer += 1
                else:
                    print("Wrong! the correct answer is", num3)
                j += 1
        if correctAnswer >= (1/2)*int(choice1):
            print("Congratulations! You got " + str(correctAnswer) +
                  " out of " + str(choice1) + " item/s")
        else:
            print("Unfortunately you got " + str(correctAnswer) +
                  " out of " + str(choice1) + " item/s")
    else:
        print("Invalid Input")

    try_again = input("Want to try again? (yes/no): ")
    if try_again == "no":
        break
    elif try_again == "yes":
        j = 0
        correctAnswer = 0
    else:
        print("Invalid Input")
