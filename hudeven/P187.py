class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = set()
        visited = set()
        if s == None or len(s) < 10:    return list(res)

        for i in range(len(s)):
            sub = s[i : i + 10]
            if sub in visited :
                res.add(sub)
            else:
                visited.add(sub)
        return list(res)
