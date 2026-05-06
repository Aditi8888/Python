import math 
def is_prime(n) :
    if n<=1 :
        return False
    if n<=3 :
        return True
    if n%2 == 0 or n%3== 0 :
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 2):
      if n % i == 0:
          return False
      return True
for n in range(1,21) :
     if is_prime(n):
        print(f"{n} is prime")
     else:
        print(f"{n} is not prime")