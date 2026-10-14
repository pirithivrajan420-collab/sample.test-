import math


def add(a, b):
  return a + b


def subtract(a, b):
  return a - b


def multiply(a, b):
  return a * b


def divide(a, b):
  if b == 0:
    return "Error! Division by zero."
  return a / b


def power(base, exp):
  return base**exp


def square_root(x):
  if x < 0:
    return "Error! Cannot take square root of negative number."
  return math.sqrt(x)


def c_to_f(c):
  return (c * 9 / 5) + 32


def f_to_c(f):
  return (f - 32) * 5 / 9


def km_to_miles(km):
  return km * 0.621371


def miles_to_km(miles):
  return miles / 0.621371


def main():
  while True:
    print("\n--- Multi-Purpose Python Calculator ---")
    print("1. Basic Arithmetic (Add, Subtract, Multiply, Divide)")
    print("2. Scientific Operations (Power, Square Root)")
    print("3. Unit Conversions (Temperature & Distance)")
    print("4. Exit")

    choice = input("Select a mode (1-4): ")

    if choice == "1":
      print("\n[Basic Arithmetic]")
      op = input("Enter operation (+, -, *, /): ")
      try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if op == "+":
          print(f"Result: {add(a, b)}")
        elif op == "-":
          print(f"Result: {subtract(a, b)}")
        elif op == "*":
          print(f"Result: {multiply(a, b)}")
        elif op == "/":
          print(f"Result: {divide(a, b)}")
        else:
          print("Invalid operation!")
      except ValueError:
        print("Invalid input! Please enter valid numbers.")

    elif choice == "2":
      print("\n[Scientific Operations]")
      print("1. Exponentiation (base^exp)")
      print("2. Square Root")
      sub_choice = input("Select option (1-2): ")
      try:
        if sub_choice == "1":
          base = float(input("Enter base: "))
          exp = float(input("Enter exponent: "))
          print(f"Result: {power(base, exp)}")
        elif sub_choice == "2":
          x = float(input("Enter number: "))
          print(f"Result: {square_root(x)}")
        else:
          print("Invalid option!")
      except ValueError:
        print("Invalid input!")

    elif choice == "3":
      print("\n[Unit Conversions]")
      print("1. Celsius to Fahrenheit")
      print("2. Fahrenheit to Celsius")
      print("3. Kilometers to Miles")
      print("4. Miles to Kilometers")
      sub_choice = input("Select conversion (1-4): ")
      try:
        val = float(input("Enter value to convert: "))
        if sub_choice == "1":
          print(f"Result: {c_to_f(val):.2f} °F")
        elif sub_choice == "2":
          print(f"Result: {f_to_c(val):.2f} °C")
        elif sub_choice == "3":
          print(f"Result: {km_to_miles(val):.2f} miles")
        elif sub_choice == "4":
          print(f"Result: {miles_to_km(val):.2f} km")
        else:
          print("Invalid option!")
      except ValueError:
        print("Invalid input!")

    elif choice == "4":
      print("Exiting calculator. Goodbye!")
      break
    else:
      print("Invalid choice. Please select between 1 and 4.")


if __name__ == "__main__":
  main()