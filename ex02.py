is_admin = "False"

if is_admin:
    print("Hello, Admin")
else:
    print("Access denied.")

name = "Bill"
age = 16

if name == "Bill" and age >= 16:
    print("Ok")
else:
    print("No")

if name == "Bil" or age >= 16:
    print("Ok")
else:
    print("No")