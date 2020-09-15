'''
recursive solution
'''

# def fib (n):
    # if n < 0:
    #     raise ValueError('Index was negative. No such thing as a '
    #                      'negative index in a series.')
#     if n in [1, 0]:
#         return n
#     else:
#         return fib(n-1) + fib(n-2)


# for i in range(8):
#     print(f'Number{i}: {fib(i)}')

# print('Print 6th', fib(6))
# Time complexity O(2n) NOT good!

'''
using memoization
'''
# def fib (n):
#     memo = {}
#     if n < 0:
#         raise ValueError('Index was negative. No such thing as a '
#                          'negative index in a series.')
#     if n in [0, 1]:
#         return n
#     result = fib(n-1) + fib(n-2)
#     memo[n] = result
#     return result


# for i in range(8):
#     print(f'Number{i}: {fib(i)}')

# print('Print 6th', fib(6))

# Time complexity O(n) better!
# Space complexity O(n) NOT good!

'''
bottom up approach
'''
def fib(n):
    # Edge cases:
    if n < 0:
        raise ValueError('Index was negative. No such thing as a '
                         'negative index in a series.')
    elif n in [0, 1]:
        return n

    # We'll be building the fibonacci series from the bottom up
    # so we'll need to track the previous 2 numbers at each step
    prev_prev = 0  # 0th fibonacci
    prev = 1       # 1st fibonacci

    for _ in range(n - 1):
        # Iteration 1: current = 2nd fibonacci
        # Iteration 2: current = 3rd fibonacci
        # Iteration 3: current = 4th fibonacci
        # To get nth fibonacci ... do n-1 iterations.
        current = prev + prev_prev
        prev_prev = prev
        prev = current

    return current
for i in range(8):
    print(f'Number{i}: {fib(i)}')

print('Print 6th', fib(6))

# Time complexity O(n) 
# Space complexity O(1) good!