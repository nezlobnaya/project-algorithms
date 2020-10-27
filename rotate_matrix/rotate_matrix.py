"""

Given an N x N matrix, rotate it 90 degrees clockwise. You cannot use any extra space!

Example

Input - [

[1, 2, 3],

[4, 5, 6],

[7, 8, 9]]

Output - [

[7, 4, 1],

[8, 5, 2],

[9, 6, 3]]

Solution

Unfortunately, this question is akin to one of those “brain teaser” questions. Either, you’ve seen the question before and can solve it immediately, or you’re going to spend the next 15 minutes staring at the example test case going “uhhhhhh”.

If you’re in the second scenario, your best bet is to right down a bunch of examples and try and see if you can find a pattern somewhere.

The way you solve this is to 

Transpose the Matrix
Reverse the rows of the transposed Matrix
That’s it!

"""
def rotateMatrix(m):
    
    # Transpose of Matrix
    for r in range(len(m)):
        for c in range(r + 1, len(m[r])):
            m[r][c], m[c][r] = m[c][r], m[r][c]

    # Reverse Rows
    for r in range(len(m)):
        for c in range(len(m[r]) // 2):
            m[r][c], m[r][len(m[r]) - 1 -c] = m[r][len(m[r]) - 1 -c], m[r][c]
    
    # Done in O(1) space, so we don't have to return anything!

testCaseOne = [[1, 2, 3], [4, 5,6], [7,8,9]]
solutionOne = [[7,4,1],[8,5,2],[9,6,3]]
rotateMatrix(testCaseOne)
print(testCaseOne == solutionOne)