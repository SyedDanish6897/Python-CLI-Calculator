# Funtion for (+,-,*,/)
def add (x,y):
    return x+y
def sub (x,y):
    return x-y
def multiply (x,y):
    return x*y
def divide(x,y):
    if y==0:
        return("error ! cannot divide by 0")
    return x/y

print("Select Operation ")
print("1. Add")
print("2. sub")
print("3. multiply")
print("4. divide")

# for choosing which operation you want to choose
choice= input("Choice operation to Calculate (1/2/3/4): ")
if choice in ('1','2','3','4'):
    try: 
        num1= float(input("Enter first number"))
        num2= float(input("Enter second number"))

    except ValueError:
        print("invalid input ! Enter the numeric value ")
    
    else:
        if choice == '1':
            print("Result :",add(num1,num2))
        if choice == '2':
            print("Result :", sub(num1,num2))
        if choice == '3':
            print("Result :", multiply(num1,num2))
        if choice == '4':
            print("Result :", divide(num1,num2))
else:
    print(" Plest selet a valid opreation ")

