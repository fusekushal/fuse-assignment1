def add(x, y): #function to add two numbers
    return x + y

def subtract(x, y): #function to subtract two numbers
    return x - y

def multiply(x, y): #function to multiply two numbers
    return x * y 

def divide(x, y):
    if y != 0:
        return x / y
    else:
        raise ValueError("Cannot divide by zero")

def main():
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice (1/2/3/4): ")

    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(n1, n2))
    elif choice == '2':
        print("Result:", subtract(n1, n2))
    elif choice == '3':
        print("Result:", multiply(n1, n2))
    elif choice == '4':
        print("Result:", divide(n1, n2))
    else:
        print("Invalid choice")
        

if __name__ == "__main__":
    main()