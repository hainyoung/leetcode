class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        # print(anagrams)
        for word in strs:
            # anagrams[sorted(word)] # TypeError : unhashable type:'list'
            # anagrams[''.join(sorted(word))]  # 여기까지가 키(1)
            anagrams[''.join(sorted(word))].append(word) # key, value #(2)

        # print(anagrams) 
        #(1) defaultdict(<class 'list'>, {'aet': [], 'ant': [], 'abt': []})
        
        # print(anagrams) 
        # (2) defaultdict(<class 'list'>, {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']})

        
        return anagrams.values() # value들만 return