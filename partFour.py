def main():
    AD = "admin"
    PS = "password123"
    ADI = input("Username: ")
    PSI = input("Password: ")
    verify(AD, PS, PSI, ADI)

def verify(AD, PS, PSI, ADI):
    if ADI == AD and PS == PSI:
         print("Access Granted")
    else:
        print("Error Access Denied")
main()
