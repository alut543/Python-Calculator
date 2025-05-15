import time

while True:
print("Calculator ➖✖️➕➗:")
    cmdline = input("> ")
    if cmdline == "addition":
        setnumaddfirst = int(input("Enter your first number. > "))
        setnumaddsecond = int(input("Enter your second number. > "))
        time.sleep(2)
        print(setnumaddfirst + setnumaddsecond)
    elif cmdline == "subtraction":
            setnumsubfirst = int(input("Enter your first number. > "))
            setnumsubsecond = int(input("Enter your second number. > "))
            time.sleep(2) 
            print(setnumsubfirst - setnumaddsecond)
    elif cmdline == "multiplication":
            setnummultfirst = int(input("Enter your first number. > "))
            setnummultsecond = int(input("Enter your second number"))
            time.sleep(2)
            print(setnummultfirst * setnummultsecond)
    elif cmdline == "division":
           setnumdivfirst = int(input("Enter your first number. > "))
           setnumdivsecond = int(input("Enter your second number. > "))
           time.sleep(2)
           print(setnumdivfirst + setnumdivsecond)
                                            


