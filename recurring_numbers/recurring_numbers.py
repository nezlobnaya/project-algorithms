from collections import Counter
def recurring(str):
    count = Counter(str)
    new_arr = []
    for i in str:
        for key, value in count.items():
            if value >= 2:
                new_arr.append(key)
                print(f'{key} occurs {value} times')
            else:
                pass
        return new_arr

arr = [1, 1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0, 12, 12]

print(f"The recurring numbers {recurring(arr)}")