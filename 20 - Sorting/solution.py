if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    not_sorted = True
    total_swaps = 0

    while not_sorted:
        not_sorted = False
        count = 0
        for i in range(1, len(a)):
            if a[i - 1] > a[i]:
                not_sorted = True
                count += 1
                a[i - 1], a[i] = a[i], a[i - 1]

        total_swaps += count

    print(f"Array is sorted in {total_swaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")