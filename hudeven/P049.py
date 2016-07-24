class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key in dict:
                dict[key].append(word)
            else:
                dict[key] = [word]
        res = []
        for key in dict:
            res.append(dict[key])
        return res
