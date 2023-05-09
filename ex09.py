num = int(input("Take a number: "))

while num < 10:
    num += 1
    if num == 5:
        continue
    print(num)

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

for i in range(10):
    if i % 2 == 1:
        continue
    print(i)