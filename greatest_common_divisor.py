def divisor(m:int, n:int)-> int:
  if m > n:
        small = n
  else:
      small = m
  for num in range(1, small+1):
      if((m % num == 0) and (n % num == 0)):
          gcd = num
              
  return gcd
  