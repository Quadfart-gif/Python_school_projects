# Building a simple calculator app
#add
#subtract
#divide
#multiply

#displayig the interface
def iNterface():
    print("What operationg would you like to use type the associated number")
    print("1. Addition")
    print("2. subtraction")
    print("3. division")
    print("4. multiplication")
    print("5. EXIT")

# function after doing the interface
def pLay():
    while True:
        oPeration = int(input("input a value: "))
        if oPeration == 1:
            #coding for addition
            num1 = int(input("input first number:"))
            num2 = int(input("input second number:"))
            aDD = num1 + num2
            print(num1, "+", num2, "=", aDD)
        elif oPeration == 2:
            #coding for subtraction
            numS1 = int(input("input first number:"))
            numS2 = int(input("input first number:"))
            sUB = numS1 - numS2
            print(numS1, "-", numS2, "=", sUB )
        elif oPeration == 3:
            #coding for division
            numD1 = int(input("input first number:"))
            numD2 = int(input("input first number:"))
            dIV = numD1 - numD2
            print(numD1, "-", numD2, "=", dIV)
        elif oPeration == 4:
            #coding for multiplying
            numM1 = int(input("input first number:"))
            numM2 = int(input("input first number:"))
            mUL = numM1 - numM2
            print(numM1, "-", numM2, "=", mUL)
        elif oPeration == 5:
            #exit the calculator
            print("Exiting calculator...")
            break
        else:
            print("invalid input")

iNterface()
pLay()

    

