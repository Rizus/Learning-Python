class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]] += 1
            else:
                d[s[i]] = 1
        srt = sorted(d.values(), reverse=True)
        l = ""
        for values in range(len(srt)):
            for keys, value in d.items():
                if srt[values] == value:
                    if keys * value not in l:
                        l += keys * value
                        break
        return(l)
