""" @author: Adam, @date: 6-11-2019 

The key idea is to use the unique prime factorization theorem: every integer 
greater than 1 is either a prime number or can be represented as a unique 
product of primes. This guides my get_prime_factors() implementation. Also,
when checking if n is prime, we only must check up to floor(sqrt(n)). 
"""

import time

def is_prime(n):
    """Return True if n is prime and False otherwise."""
    if n == 1:
        return False
    
    for i in range(2, int(n**(.5)) + 1):  # int() takes the floor for us
        if n % i == 0:
            return False
    return True

def get_prime_factors(n, do_print=True):
    """Return a list of prime factors of n."""
    if is_prime(n):
        if do_print:
            print(f"{n} is prime.")
        return n
    
    prime_factors = []
    # Begin factorization at 2, increment if needed in loop below.
    factor = 2
    while True:
        if n % factor == 0:
            prime_factors.append(factor)
            
            # Reduce factorization problem until n//factor is prime.
            n = n//factor
            if is_prime(n):
                prime_factors.append(n)
                break
            factor = 2
            continue
        
        factor += 1
    
    return prime_factors

#%% Prime factorization. 
    
if __name__ == '__main__':
    start = time.time()
     
    # Get prime factorization of n.
    n = 600851475143
    print(get_prime_factors(n))
    
    print(time.time() - start)