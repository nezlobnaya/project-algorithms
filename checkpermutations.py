"""
You are given a string as input.

Write a function that checks if the letters in the string can be rearranged to form a palindrome ( or if the input is already a palindrome).

You can ignore spaces in the string.

Example

Input - “car race”

Output - True (the letters can be rearranged to “racecar”)

"""
def checkPermutation(s):
    counts = {}
    for i in s:
        if i == " ":
            continue
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    hasOdd = False
    for key, value in counts.items():
        if value % 2 == 1:
            if hasOdd:
                # we have more than one char
                # that appears an odd number
                # of times
                return False
            hasOdd = True

    return True

print(checkPermutation("car race"))