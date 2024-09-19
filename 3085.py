class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = defaultdict(int) # 26 distinct keys
        for c in word: # O(word.length)
            freq[c] += 1
        
        min_deletions = 10**6

        for c, f in freq.items(): # O(26)
            tot_deletions = 0
            for c2, f2 in freq.items(): # O(26)
                if c2 == c:
                    continue
                if f2 < f:
                    tot_deletions += f2
                    continue 
                deletions = f2 - f - k
                tot_deletions += max(deletions, 0)
            
            min_deletions = min(min_deletions, tot_deletions)
        # tot = O(word.length + 26 * 26)
        return min_deletions




                
