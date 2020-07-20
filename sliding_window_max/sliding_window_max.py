'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
# def sliding_window_max(nums, k):
#     # Your code here
    # arrlen = len(nums)
   
    # start = 0
    # stop = k
    # highest = []
    # while stop <= arrlen:
    #     highest.append(max(nums[start:stop]))
    #     start+=1
    #     stop+=1
    # return highest
    
import collections
def sliding_window_max(nums, k):
        dq = collections.deque()
        ans = []
        for i in range(len(nums)):
            # For every element, the previous  
            # smaller elements are useless 
            # so remove them from dq 
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            # Add new element at rear of queue 
            dq.append(i)
            # Remove the elements which are  
            # out of this window 
            if dq[0] == i - k:
                # remove from front of deque
                dq.popleft()
            if i >= k - 1:
                ans.append(nums[dq[0]])
        return ans


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
