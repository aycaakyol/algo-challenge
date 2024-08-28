# Problem: https://leetcode.com/problems/longest-common-prefix/description/

def longestCommonPrefix(strs):
    minl = len(strs[0])
    prefix = strs[0]

    for x in strs:
        if len(x) < minl:
            minl = len(x)
            prefix = x
            strs.remove(x)

            break

    for x in strs:
        for i in range(minl, -1, -1):
            if x[0:i] == prefix[0:i]:
                prefix = x[0:i]
                break

            if i == 0:
                prefix = ""

    return prefix

print(longestCommonPrefix(["a"]))


    