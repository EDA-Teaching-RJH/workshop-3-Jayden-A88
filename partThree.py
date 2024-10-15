def main():
    Grade = float(input("What is your grade?: "))
    cal(Grade)
    
def cal(Grade):
    if Grade >= 90 and Grade <= 100:
        print("Grade A")
    elif Grade >= 80 and Grade <= 89:
        print("Grade B")
    elif Grade >= 70 and Grade <= 79:
        print("Grade C")
    elif Grade >= 60 and Grade <= 69:
        print("Grade D")
    elif Grade >= 0 and Grade <= 59:
        print("Grade F")
    else:
        print("Invalid Grade")
        
main()