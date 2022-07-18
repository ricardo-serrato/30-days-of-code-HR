n = int(input())
phone_book = dict()
for i in range(n):
    line = input()
    line = line.split()
    phone_book[line[0]] = phone_book.get(line[0], line[1])

while True:
    try:
        key = input().strip()

        value = phone_book.get(key)

        if value is None:
            print("Not found")
        else:
            print(f"{key}={value}")
    except:
        break
