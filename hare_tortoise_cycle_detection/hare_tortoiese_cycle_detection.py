def hare_tortoise_cycle_detection(str):
    tortoise = str[0]
    hare = str[0]
    while True:
        tortoise = str[tortoise]
        hare = str[str[hare]]
        if tortoise == hare:
            break
    ptr1 = str[0]
    ptr2 = tortoise
    while ptr1 != ptr2:
        ptr1 = str[ptr1]
        ptr2 = str[ptr2]
    return ptr1

arr = [3,1,3,4,2]
print(hare_tortoise_cycle_detection(arr))