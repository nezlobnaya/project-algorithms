"""
You are given two strings s and t.

Return the minimum window in s which will contain all the characters in t.

If there is no such window in s that covers all characters in t, return an empty string.

Input: s = "ADOBECODEBANC", t = "ABC"   Output: "BANC"

"""




def minWindow(s: str, t: str) -> str:
    modelWindow = {}
    for i in t:
        if i in modelWindow:
            modelWindow[i] += 1
        else:
            modelWindow[i] = 1
    
    if len(s) < len(t):
        return ""
    
    window = {k:0 for k in t}
    contains = 0
    longest = ""
    l, r = 0, 0
    
    while True:
        if contains == len(modelWindow):
            if longest == "" or (r - l) < len(longest):
                longest = s[l:r]
            if s[l] in window:
                window[s[l]] -= 1
                if window[s[l]] < modelWindow[s[l]]:
                    contains -= 1
            l += 1
        elif r < len(s):
            if s[r] in window:
                window[s[r]] += 1
                if window[s[r]] == modelWindow[s[r]]:
                    contains += 1
            r += 1
        else:
            break
    
    return longest

testCaseOne = ("ADOBECODEBANC", "ABC")
print(minWindow(*testCaseOne) == "BANC")

testCaseTwo = ("a", "a")
print(minWindow(*testCaseTwo) == "a")