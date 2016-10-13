def reverse(text):
    word = []
    for x in text:
        word.append(x)
    count = len(word) - 1
    reversal = []
    rword = ''
    while count >= 0:
        reversal.append(word[count])
        count -= 1
    for x in reversal:
        rword += x
    else:
        return rword

print(reverse('happy'))
print(reverse('sad'))
print(reverse('@#hsek'))
