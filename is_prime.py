def is_prime(x):
    if x > 2:
        print('x>2')
        for num in range(2, x - 1):
            print ('for loop', num)
            if x % num == 0:
                print ('x % num')
                return False
        else:
            return True
    elif x == 2:
        return True
    else:
        return False

print(is_prime(3))
print(is_prime(7))
