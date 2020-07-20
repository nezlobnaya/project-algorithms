'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    # start and ending index
    start = 0
    end = len(arr) - 1
    # while start and end have not met 
    while end > start:
        # check end is 0 and start is not for swap
        if arr[start] is 0 and arr[end] is not 0:
            arr[start], arr[end] = arr[end], arr[start]
            # next for both in their directions
            start += 1
            end -= 1
        elif arr[start] is not 0 and arr[end] is not 0:
            start += 1
        # otherwise decrement end
        else:
            end -= 1
    
    return arr

   


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")