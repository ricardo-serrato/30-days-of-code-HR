n = int(input().strip())

arr = list(map(int, input().rstrip().split()))
arr.reverse()

for i in range(n):
    print(f"{arr[i]} ", end="")

