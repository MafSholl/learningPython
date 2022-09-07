def divide(a, b):
    if b == 0:
        raise ValueError("Denominator cannot be zero")

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("At least geht sense na")
    return a / b
    # return int(a) / int(b)

num = int(input("Enter the numerator: "))
den = int(input("Enter the denominator: "))
# num = input("Enter the numerator: ")
# den = input("Enter the denominator: ")

while True:
    try:
        print(divide(num, den))
        break
    # except:
    #     print("wrong")
    #     num = int(input("Enter the numerator: "))
    #     den = int(input("Enter the denominator: "))

    except ValueError:
        print("wrong")
        num = int(input("Enter the numerator: "))
        den = int(input("Enter the denominator: "))

    except TypeError:
        print()
