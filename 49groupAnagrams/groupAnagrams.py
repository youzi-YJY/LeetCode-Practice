class Solution:
    def groupAnagrams(self,strs):
        dict={}
        for item in strs:
            key=tuple(sorted(item))
            dict[key]=dict.get(key,[])+[item]
        return list(dict.values())