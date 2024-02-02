class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ## find the shortest word
        """
        :type strs: List[str]
        :rtype: str
        """
        ## find the shortest word
        shortestWordLength = len(strs[0])
        lengthOfArr = len(strs)
        shortestWord = 0
        
        for i in range(len(strs)):
            if len(strs[i]) < shortestWordLength:
                shortestWordLength = len(strs[i])
                shortestWord = i

        longestPrefix = ''
        isAmong = False
        for i in range(shortestWordLength):
            for t in range(1, lengthOfArr):
                if strs[0][i] == strs[t][i]:
                    isAmong = True
                else:
                    isAmong = False    
            if isAmong: 
                longestPrefix += strs[shortestWord][i]
        return longestPrefix
        
        
        