print("WELCOME TO ALL IN ONE CALCULATOR")
print("--------------------------------")
while (True):
    print("+ For Addition\n- For Subtraction\n* For Multiplication\n/ For Division\n% For Percentage\n@ for AgeCalculate")
    a = input("What you want:\n")

    if a == "!":
        break

    if a == "@":
        f = int(input("Enter Birth Day:\n"))
        g = int(input("Enter Birth Month:\n"))
        h = int(input("Enter Birth Year:\n"))
        i = int(input("Enter Present Day:\n"))
        j = int(input("Enter Present Month:\n"))
        k = int(input("Enter Present Year:\n"))

    elif a == "%":
        b = int(input("Enter the total number:\n"))
        c = int(input("Enter the scored number:\n"))

    else:
        d = int(input("Enter the first number:\n"))
        e = int(input("Enter the second number:\n"))

    if a == "+":
        print("Answer is", d + e)

    elif a == "-":
        print("Answer is", d - e)

    elif a == "*":
        print("Answer is", d * e)

    elif a == "/":
        print("Answer is", d / e)

    elif a == "%":
        print("Answer:", c * 100 / b,"%")

# Age calculator code
    if a == "@":
        if k>h:
            print("Your Age:")
            print(k - h, "Years")

        else:
            print("Invalid Present Year!")

        if j>g:
            print(j - g, "Months")

        else:
            print(g - j, "Months")

        if i>f:
            print(i - f, "Days")

        else:
            print(f - i, "Days")

    print("--------------------------------")
    print("! for exit")