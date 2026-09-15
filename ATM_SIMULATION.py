#ATM MACHINE
balance = 10000
PIN = "1234"
pin= input("Enter Your PIN:")

if pin == PIN:
    while True:
        print("\n===Welcome to XYZ BANK ATM===\n")
        print("1. Bal.Enquiery")
        print("2. Deposite")
        print("3. Withdrawl")
        print("4. EXIT")

        ch = input("Enter your option from (1 to 4):")
        if ch =="1":
            print("Available balance is : INR",balance)
        elif ch =="2":
            amount = float(input("Enter your deposite amount:"))
            if amount>0:
                balance += amount # balance = balance + amount
                print("Deposite Successful")
                print("Updated Balance is :",balance)
            else:
                print("Invalid Amount!")
        elif ch =="3":
            amount = float(input("Enter your Withdrawl amount:"))
            if amount <= balance:
                balance -= amount
                print("Please Collect your cash-->")
                print("AV. Blance: INR: ",balance)
            else:
                print("Insufficient balance!")
        elif ch=="4":
            print("Thank you visit Again!!")
            break
        else:
            print("INVALID CHOICE !!!")
else:
    print("INCORRECT PIN!!! TRY AGAIN ")

