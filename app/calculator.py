import math
import sys

def sqrt(x: float) -> float:
    if x < 0:
        raise ValueError("Square root undefined for negative numbers.")
    return math.sqrt(x)

def factorial(n: int) -> int:
    if not float(n).is_integer():
        raise ValueError("Factorial requires integer input.")
    n = int(n)
    if n < 0:
        raise ValueError("Factorial undefined for negative integers.")
    return math.factorial(n)

def ln(x: float) -> float:
    if x <= 0:
        raise ValueError("Natural logarithm undefined for x <= 0.")
    return math.log(x)

def power(x: float, b: float) -> float:
    if x < 0 and not float(b).is_integer():
        raise ValueError("Negative base with non-integer exponent is not supported.")
    return math.pow(x, b)

def menu():
    while True:
        print("\n1) Square root √x")
        print("2) Factorial n!")
        print("3) Natural logarithm ln(x)")
        print("4) Power x^a")
        print("5) Exit")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            x = float(input("Enter x: "))
            print("√", x, "=", sqrt(x))
        elif choice == "2":
            n = int(input("Enter n: "))
            print(n, "!", "=", factorial(n))
        elif choice == "3":
            x = float(input("Enter x: "))
            print("ln(", x, ") =", ln(x))
        elif choice == "4":
            x = float(input("Enter x: "))
            b = float(input("Enter b: "))
            print(x, "^", b, "=", power(x, b))
        elif choice == "5":
            print("Exiting.")
            sys.exit(0)
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()
