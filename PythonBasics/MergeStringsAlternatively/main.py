class Solution(object):
    def get_max_word(self, string_1, string_2):
        if (len(string_1) > len(string_2)):
            return string_1
        else: 
            return string_2

    def mergeAlternately(self, word1, word2):
        max_word = self.get_max_word(word1, word2)
        min_word_len = min(len(word1), len(word2))
    
    
        merged_word = ""
    
        for i in range(min_word_len):
            merged_word += word1[i]
            merged_word += word2[i]
        
        merged_word += max_word[min_word_len: ]
        return merged_word
    