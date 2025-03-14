math = (input("Enter the math score: "))
eng = (input("Enter the english score: "))
math = int(math)
eng = int(eng)
print("The operator should be +, -, *, /")
oper = input("Enter the operator: ")

if oper == "+":

    print(math + eng)
elif oper == "-":
    print(math - eng)
elif oper == "*":
    print(math * eng)
elif oper == "/":
    print(math / eng)
else:
    print("Invalid operator")
#end of code .
