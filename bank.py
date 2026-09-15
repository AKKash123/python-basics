# balance = 22000
# withdrawl = 1200
# #logic
# if withdrawl<=balance:
#     #unary operator
#     balance-=withdrawl
#     print("Get your cash Successfully, your available balance:",balance)
# else:
#     print("Sorry you have insufficient balance!",balance)

#switch 
#match
balance = 22000
withdrawl = 1200
deposite = 5000
c = "withdrawl"
match c:
    case "balance":
        print('Show balance:',balance)
    case "deposite":
        balance+=deposite
        print('Av.balance:',balance)
    case "withdrawl":
        if withdrawl<=balance:
            #unary operator
            balance-=withdrawl
            print("Get your cash Successfully, your available balance:",balance)
        else:
            print("Sorry you have insufficient balance!",balance)
    case "_":
        print("Sorry Wrong choice!")