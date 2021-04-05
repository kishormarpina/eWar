plist = set()
def isPoly(word):
    if(word in plist):
        return True
    flag = True
    k =  len(word)
    if(k == 1):
        flag = True
    else:
        for i in range(k//2):
            if(word[i] != word[k-i-1]):
                flag = False
                break
    return flag
def countSubPalindromes(s):
    count = 0
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            word = s[i:j]
            if(isPoly(word)):
                plist.add(word)
                count += 1
    return count
print(countSubPalindromes("abba"))
