import random

def main():
    val = int(input("Pick a Number between 1 and 10: "))
    myst(val)
    
def myst(val):
    sn = random.randint(1, 10)
    if val > sn:
        print("Too High")
    elif val < sn:
        print("Too Low")
    elif val == sn:
        print("Correct!")   
    print(f"The number was: {sn}")

main()