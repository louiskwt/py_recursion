def isPalindrome(s):
    # convert the string to character by stripping out punctuation and converting case
    def toChar(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijkmnopqrstuvwxyz':
                ans = ans + c
        return ans

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1: -1])
    return isPal(toChar(s))


print(isPalindrome('Do geese see God?'))  # True
