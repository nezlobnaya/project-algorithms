
# import numpy as np

# def fib(n):
#     if n == 0:
#         return 0
#     F = np.matrix('1 1; 1 0')
#     if n > 2:
#         F = power(F, n-1, base=F)
#     return F[0, 0]

# debug_msg = "debug: F^{} (for the {} fibonacci number) =\n{}"
# def power(F, n, base):
#     if n == 1:
#         return F
#     F = power(F, n // 2, base)
#     F = F @ F # can't use `F @= F` yet
#     n_even = 2*(n//2)
#     print(debug_msg.format(n_even, nth(n_even+1), F))
#     if n%2:
#         F = F @ base  # can't use `F @= base` yet
#         print(debug_msg.format(n, nth(n+1), F))
#     return F

# def nth(n):
#     n_tens, n_ones = divmod(n, 10)
#     special = ('1st', '2nd', '3rd')
#     if 1 <= n_ones <= 3:
#         tens = str(n_tens) if n_tens else ""
#         return tens + special[n_ones-1]
#     return f'{n}th'

# if __name__ == "__main__":
#     # for num in (1, 2, 3, 4, 5, 9):
#     for num in (9, 31):
#         print()
#         print("-"*60)
#         print(f'result: fib({num}) is {fib(num):,}')

#Time complexity O(Log(n))

# Another option:

def mult(x,y):
    if ( len(y) == 2 ):
        a = x[0]*y[0]+x[1]*y[1]
        b = x[2]*y[0]+x[3]*y[1]
        return [a,b]
    a = x[0]*y[0] + x[1]*y[2]
    b = x[0]*y[1] + x[1]*y[3]
    c = x[2]*y[0] + x[3]*y[2]
    d = x[2]*y[1] + x[3]*y[3]
    return [a,b,c,d]

# Only works for positive powers!
def matrix_power( x, n ):
    if ( n == 1 ):
        return x
    if ( n%2 == 0 ):
        return matrix_power( mult(x, x), n//2 )
    return mult(x, matrix_power( mult(x, x), n//2 ) )
    
# fibonacci example:
A = [1,1,1,0]
v = [1,0]

x = 31
print(f'result : fib {x} is {mult(matrix_power(A,x-1),v)[0]: ,}') #1,346,269

