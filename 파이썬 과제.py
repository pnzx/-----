def recursion(s, l, r, count):
    if l >= r:
        print("1", count, end=' ')
    elif s[l] != s[r]:
        print("0", count, end=' ')
    else:
        count += 1
        return recursion(s, l+1, r-1, count)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1, count=1)

# 입력받기
n=int(input())
string= [input() for _ in range (n)]

for s in string:
    isPalindrome(s)
    print()