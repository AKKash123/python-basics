class Scientific:
    def __init__(self):
        self.memory = 0
        self.history=[] #list[1,2,'name']

    #basic calculator
    def Basic_op(self,a,op,b):
        if op == "+":
            res = a+b
        elif op == "-":
            res=a-b
        elif op == "*":
            res=a*b
        elif op == "/":
            if b!=0:    #denominator is 0 or not
                res=a/b
            else:
                return "Error: Zero Divisor"
        elif op == "%":
            res=a%b #remainder
        elif op == "//":
            res=a//b #Quotient value or floor division
        elif op == "**":
            res=a**b    #power
        else:
            return "Choose the correct operator!"
        #Store the infomation
        self.history.append(f"{a} {op} {b} = {res}")
        return res
    #memory operation

    def Memory_op(self,op,val=None):
        if op == "M+":
            self.memory += val  #increment post increment
            return f"Memory = {self.memory}"
        elif op == "M-":
            self.memory -= val #post decrement
            return f"Memory = {self.memory}"
        elif op == "MR": #recall or check purpose
            return f"Check: {self.memory}"
        elif op == "MC":
            return "Memory Cleared"
        else:
            return "Invalid memory Operation"

    #USER INPUT METHOD
    def User_Input(self,val):
        if isinstance(val,(int,float)):
            return True
        return False
    #Calculation History Display
    def Show_history(self):
        print("\n======History=======")
        if len(self.history)==0:
            print("No calculation Yet")
        else:
            for hist in self.history:
                print(hist)
#MAIN PROGRAM
calculator = Scientific()
print("===Scientific Calculator")
num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
opt = input("Enter the operator (+,-,*,/,%,//,**):")
#userInput Validation check
if calculator.User_Input(num1) and calculator.User_Input(num2):
    ans = calculator.Basic_op(num1,opt,num2)
    print("Result:",ans)
else:
    print("Invalid INPUT!!")
#Memory Operation
calculator.Memory_op("M+",ans)
print(calculator.Memory_op("MR"))
#HISTORY
calculator.Show_history()

            
