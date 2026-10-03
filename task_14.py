def c_to_f(c):
    return c * 9 / 5 + 32

def f_to_c(f):
    return (f - 32) * 5 / 9

print("temperature converter")
print("1. celsius to fahrenheit")
print("2. fahrenheit to celsius")

choice = input("select: ")

try:
    value = float(input("enter temperature: "))

    if choice == "1":
        if value < -273.15:
            print("temperature not possible")
        else:
            print(f"{value:.2f} c = {c_to_f(value):.2f} f")

    elif choice == "2":
        if value < -459.67:
            print("temperature not possible")
        else:
            print(f"{value:.2f} f = {f_to_c(value):.2f} c")

    else:
        print("wrong option")

except ValueError:
    print("enter numbers only")
