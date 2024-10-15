def main():
    age = int(input("What is your age? "))
    alt(age)

def alt(age):
    if age >= 18:
        print("Your are an adult")
    elif age < 18:
        print("You are a child!")
main()