class Solution:
    def minWindow(self, s: str, t: str) -> str:

        l = 0
        r = 0

        currMin = float('inf')
        minL = 0
        minR = 0

        dict_t = {}

        for x in t:
            dict_t[x] = dict_t.get(x, 0) + 1

        have, need = 0, len(dict_t)
        
        window = {}

        while r < len(s):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in dict_t and window[c] == dict_t[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < currMin:
                    currMin = (r - l + 1)
                    minL = l
                    minR = r + 1
                
                char_l = s[l]
                window[char_l] -= 1
                if char_l in dict_t and window[char_l] < dict_t[char_l]:
                    have -= 1
                l += 1
            
            r += 1

        return s[minL:minR] if currMin != float('inf') else ""