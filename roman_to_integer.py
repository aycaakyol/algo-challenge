# Problem: https://leetcode.com/problems/roman-to-integer/

def romanToInt(s):
    symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 
        'C': 100, 'D': 500, 'M': 1000}
    
    num = 0

    for i in range(len(s)):
        num += symbols[s[i]]

        if i - 1 >= 0:
            if s[i-1] == 'I' and s[i] == 'V':
                num += 3
                num -= symbols[s[i]]
            elif s[i-1] == 'I' and s[i] == 'X':
                num += 8
                num -= symbols[s[i]]
            elif s[i-1] == 'X' and s[i] == 'L':
                num += 30
                num -= symbols[s[i]]
            elif s[i-1] == 'X' and s[i] == 'C':
                num += 80
                num -= symbols[s[i]]
            elif s[i-1] == 'C' and s[i] == 'D':
                num += 300
                num -= symbols[s[i]]
            elif s[i-1] == 'C' and s[i] == 'M':
                num += 800
                num -= symbols[s[i]]

    return num

print(romanToInt("MCMXCIV"))