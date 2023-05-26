import multiprocessing
import time


def count_prime_factors(n):
    primes = {}

    for i in range(2, int(n**0.5)+1):
        while n % i == 0:
            if i not in primes:
                primes[i] = 0
            primes[i] += 1
            n //= i
    if n > 1:
        if n not in primes:
            primes[n] = 0
        primes[n] += 1
    count = 0
    for p in primes.values():
        count += p
    return count


def count_common_factors(filename):
    with open(filename, 'r') as f:
        numbers = [int(line.strip()) for line in f.readlines()]

    pool = multiprocessing.Pool()
    results = pool.map(count_prime_factors, numbers)
    pool.close()
    pool.join()
    
    total_common_factors = sum(results)
    return total_common_factors

if __name__ == '__main__':
    time_1 = time.time()
    filename = 'file.txt'
    total_common_factors = count_common_factors(filename)
    print(f'Total common factors: {total_common_factors}')
    print(f'{(time.time() - time_1):.8f}')