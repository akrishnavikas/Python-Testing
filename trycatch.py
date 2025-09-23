try:
    a = 25
    print(type(a))
    d = int(input("Enter a number: "))
    value = a/d
    print(f"Result is {value}")
except ZeroDivisionError:
    print("Cannot divide by Zero")
finally:
    print("The code is written using try/catch/finally")