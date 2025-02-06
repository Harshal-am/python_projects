def add( x , y ):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y 

def divide(x, y):
    return x / y

print("select operation")
print("1. add")
print("2. subtract")
print("3. multiply")
print("4. divide")

choice = input ("enter choice (1/2/3/4): ")

num1 = float(input("enter 1st number: "))
num2 = float(input("enter 2nd number: "))

if choice == '1':
    print(f"the result is: {add(num1 , num2)}")
elif choice == '2':
    print(f"the result is:{subtract(num1 , num2)}")
elif choice == '3':
    print(f"the result is:{multiply(num1 , num2)}")
elif choice == '4':
    print(f"the result is:{divide(num1 , num2)}")
    
else:
    print("Invalid input")
    