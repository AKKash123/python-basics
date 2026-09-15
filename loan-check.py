print("====Loan Eligibility checker====")

age = int(input("Enter your age:"))
income = int(input("\n Enter your annual income: "))
cscore = int(input("\nEnter your credit score:"))

#logic implementation
print("\n---wait ---for checking eligibility---\n")

if age>=18 and income>=20000 and cscore>=650:
    print("Congratulation you are eligible for loan\n")

    #max loan
    max = income*5
    print(f"You can take maximum loan amount inr{max}")
elif age<18:
    print("SORRY!!")
elif income<20000:
    print("Sorry that you have low income")
elif cscore<650:
    print("Sorry Your credit score low")
else:
    print("Sorry you donot have any eligibility criteria!!")
