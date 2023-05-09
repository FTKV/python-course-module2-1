# try:
#     user_input = int(input("Take a number: "))
# except ValueError as e:
#     print(f"Not a number, {e}")

# try:
#     if True:
#         continue
# except ValueError as e:
#     print(e)

while True:
    try:
        user_input = int(input("Take a number: "))
        print(user_input)
        break
    except ValueError as e:
        print(f"Not a number, {e}")