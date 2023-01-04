class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            word_count = [0] * 26
            for c in s:
                word_count[ord(c) - ord("a")] += 1

            res[tuple(word_count)].append(s)

        return res.values()
