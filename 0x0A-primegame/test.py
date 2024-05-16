
def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True
def next_prime(x):
    """Return the next prime number after x."""
    if x == 2:
        return 3
    candidate = x + 2
    while True:
        if is_prime(candidate):
            return candidate
        candidate += 1

def del_mult(n, lis):
    """Remove multiples of n from the list nums in place."""
    i = 0
    while i < len(lis):
        if lis[i] % n == 0:
            del lis[i]
        else:
            i += 1

def number_list(n):
    return list(range(1, n + 1))


print(is_prime(5))

print(next_prime(11))

for i in range(1, 3):
	print(i)


a = [1]

print(a == [1])
