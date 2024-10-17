def main():
    A = range(0, 11)
    B = range(65, 1000000)
    C = range(12, 64)
    ST = input("Are you a student? ").strip().lower()
    Age = int(input("What is your age? "))
    DC(A, B, C, ST, Age)

def DC(A, B, C, ST, Age):
    if Age in A and ST == "no":
        print("Ticket is £5")
    elif Age in B and ST == "no":
        print("Ticket is £5")
    elif Age in C and ST == "yes":
        print("Ticket is £8")
    elif Age in C and ST == "no":
        print("Ticket is £10")
    else:
        print("Error")
main()
