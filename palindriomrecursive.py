def isPalindrom(strng):
    if len(strng)==0:
        return True;
    if strng[0]!=strng[len(strng)-1]:
        return False
    return isPalindrom(strng[1:-1])
print(isPalindrom("aswesome"))
print(isPalindrom("foobar"))
print(isPalindrom("tacocat"))
           