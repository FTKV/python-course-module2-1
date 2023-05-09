age = 18
color = "black"
is_access = None

if age >= 16:
    is_access = True
    if color != "red":
        print("Hello")
    else:
        print("Good bye")
else:
    print("Bye")