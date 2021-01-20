def calculator(first_num, second_num, operation):
    
    if operation == "+":
        return first_num + second_num

    elif operation == "-":
        return first_num - second_num

    elif operation == "/":
        return first_num / second_num

    elif operation == "*":
        return first_num * second_num

    elif operation == "^":
        return first_num ** second_num

    else:
        print("Invalid operation. Please try again.")
        exit()

first_num = float(input("Pick first number: "))
second_num = float(input("Pick second number: "))
operation = input("Pick an operation: +, -, *, / or ^: ")
print("The answer is: " + str(calculator(first_num, second_num, operation)))
