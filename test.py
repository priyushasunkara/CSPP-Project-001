def largestNumber(list):
    a = 0
    for i in list:
        if a < i:
            a = i
    return a
print (largestNumber([77,48,19,17,93,90]))
