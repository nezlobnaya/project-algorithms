#     Find the smallest el. Swap it with the first el.
#     Find the second-smallest el. Swap it with the second el.
#     Find the third-smallest el. Swap it with the third el.
#     Repeat finding the next-smallest el, and swapping it into the correct position until the array is sorted.

# This algorithm is called selection sort because it repeatedly selects the next-smallest element and swaps it into place.

A = [64, 25, 12, 22, 11] 
  
# Traverse through all array elements 
for i in range(len(A)): 
      
    # Find the minimum element in remaining  
    # unsorted array 
    min_idx = i 
    for j in range(i+1, len(A)): 
        if A[min_idx] > A[j]: 
            min_idx = j 
              
    # Swap the found minimum element with  
    # the first element         
    A[i], A[min_idx] = A[min_idx], A[i] 
  
# Driver code to test above 
print ("Sorted array") 
for i in range(len(A)): 
    print("%d" %A[i]),  

# Time Complexity: O(n^2)

# Space Complexity: O(1)