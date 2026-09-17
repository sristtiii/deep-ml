def valid_palindrome(s):
    for i in range(len(s)):
        t=s[:i]+s[i+1:]
        if t==t[::-1]:
            return True
    return s == s[::-1]