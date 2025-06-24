def minDeletionSize(strs):
    count_delete = 0
    n = len(strs)
    for i in range(len(strs[0])):
        column = ''
        for j in range(n):
            column += strs[j][i]
        print(column)
        if column != sorted("".join(column)):
            count_delete += 1
    return count_delete

print(minDeletionSize(["abc", "bce", "cae"]))

s = 'abcd'
d = ''.join(sorted(s))
print(d)
print(s == d)
        