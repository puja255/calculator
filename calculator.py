def add(n1, n2):
    return n1+n2


def subtract(n1, n2):
    return n1-n2


def multiply(n1, n2):
    return n1*n2


def divide(n1, n2):
    return n1/n2


while True:
    print("Please choose an operation to perform - \n"
          "1. Add\n"
          "2. Subtract\n"
          "3. Multiply\n"
          "4. Divide\n"
          "5. Exit\n")
    selected_option = int(input("Select operations (1-4) or 5 to exit: "))
    if selected_option!= 5:
        n1 = int(input("Enter first number: "))
        n2 = int(input("Enter second number: "))

    if selected_option == 1:
        print("{0} + {1} = {2}\n".format(n1, n2, add(n1,n2)))
    elif selected_option == 2:
        print("{0} - {1} = {2}\n".format(n1, n2, subtract(n1, n2)))
    elif selected_option == 3:
        print("{0} * {1} = {2}\n".format(n1, n2, multiply(n1, n2)))
    elif selected_option == 4:
        print("{0} / {1} = {2}\n".format(n1, n2, divide(n1, n2)))
    elif selected_option == 5:
        print("Exiting the operation")
        break
    else:
        print("Invalid input selected")
