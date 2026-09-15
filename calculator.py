print("==Simple Calculator===\n")

num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))

#display menu
print("\nChoose the option below:-")
print("1. addition")
print("2.subtraction")
print("3.Multiplication")
print("4.Division")

#choice switch
ch = input("\n Enter your choice from (1 to 4):")
if ch == "1":
    print(f"\n Result:{num1}+{num2}={num1+num2}")
elif ch == "2":
    print(f"\n Result:{num1}-{num2}={num1-num2}")
elif ch == "3":
    print(f"\n Result:{num1}*{num2}={num1*num2}")
elif ch == "4":
    print(f"\n Result:{num1}/{num2}={num1/num2}")
else:
    print("please choose the correct option !!")