for n in range(-10, 10):
    if n >= 2:
        divisors = []
        for divisor in range(2,n):
            if n % divisor == 0:
                divisors.append(divisor)
        if len(divisors) == 0:
            print(n, " is a prime number")
        else:
            print(n, " is not a prime number. It has factors of", divisors)
    else:
        print(n, " is a negative number, and is therefore not prime")