def isValid(s: str) -> bool:
    while ('()') in s or ('[]') in s or ('{}') in s:
        s = s.replace("()", "").replace('{}', "").replace('[]', "")
    if s == '':
        return True

# time complexity is linear, it scans multiple times
# space complexity, uses little space since it removes 
# items as it processes instead of saving

if __name__ == '__main__':
    brackets = ['{{}}()()[]']
    isValid(s=brackets)
    