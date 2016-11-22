def reverse(s):
    new_str = ""
    for i in range(len(s)):
        new_str += s[len(s) - i - 1]
    return new_str

print(reverse('happy'))
print(reverse('tired'))
print(reverse('confused'))

def is_palindrome(p):
    is_pal = False
    for i in range(len(p)):
        if p[i] == p[len(p) - i - 1]:
            is_pal = True
        else:
            is_pal = False
print(is_palindrome(121))
print(is_palindrome("tacocat"))
print(is_palindrome("tired"))