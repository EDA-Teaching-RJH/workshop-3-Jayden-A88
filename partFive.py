def main():
    Weekend = {"Saturday", "Sunday"}
    Day = input("What is the current day of the week? ")
    con(Weekend, Day)
    
def con(Weekend, Day):
    if Day in Weekend:
        print("It's the weekend!")
    else:
        print("It's a weekday.")

main()
