import math 

def main():
    num1 = right_num1(input("First number: "))
    oper = right_oper(input("Operation: ").strip())
    num2 = right_num2(input("Second number: "))
    cal(num1, oper, num2)
    con()

def right_oper(oper):
    valid = ("+", "-", "*", "/", "^", "%")
    while oper not in valid:
        oper = input("Enter valid operation please e.g. (+ or - or * or / or ^ or %.): ").strip()
    return oper

def right_num1(num1):
    while True:
        try:
            return float(num1)
        except ValueError:
            num1 = input("Enter a valid number: ")
        
def right_num2(num2):
    while True:
        try:
            return float(num2)
        except ValueError:
            num2 = input("Enter a valid number: ")
        
def cal(num1, oper, num2):
    match oper:
        case "+":
            result = num1 + num2
            print(num1, "+", num2, "=", result)
        
        case "-":
            result = num1 - num2
            print(num1, "-", num2, "=", result)
        
        case "*":
            result = num1 * num2
            print(num1, "*", num2, "=", result)
        
        case "/":
            if num2 == 0:
                print("Math ERROR")
            else:
                result = num1 / num2
                print(num1, "/", num2, "=", result)
        
        case "^":
            result = pow(num1, num2)
            print(num1,"^",num2, "=", result)
        
        case "%":
            result = (num1 / 100) * num2
            print(num1,"% of", num2, "=", result)

def con():
    while True:
        Stop_Start = input("Quit or Continue? ").strip().lower()
        if Stop_Start == "continue":
            print("Continuing application")
            main()
            break

        elif Stop_Start == "quit":
            print("Quiting application")
            break
        else:
            print("Please enetr continue or quit.")
main()  