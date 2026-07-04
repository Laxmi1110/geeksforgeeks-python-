class Solution:
    def countSubstring(self, s):
        n = len(s)
        
        # 1 -> +1, 0 -> -1. Substring has more 1s iff sum > 0
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + (1 if s[i] == '1' else -1)

        # Coordinate compress because pref can be -n to +n
        sorted_vals = sorted(set(pref))
        comp = {v: i + 1 for i, v in enumerate(sorted_vals)} # 1-indexed
        size = len(sorted_vals)

        # Fenwick Tree for counting
        bit = [0] * (size + 1)
        def update(idx):
            while idx <= size:
                bit[idx] += 1
                idx += idx & -idx
                
        def query(idx): # sum of [1..idx]
            res = 0
            while idx:
                res += bit[idx]
                idx -= idx & -idx
            return res

        ans = 0
        for p in pref:
            idx = comp[p]
            ans += query(idx - 1) # count of previous pref < current pref
            update(idx)
            
        return ans
