class Solution:
    def romanToInt(self, s: str) -> int:
        k = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        n = len(s)
        sum = 0
        i = 0
        while i < n:
            if i < n-1 and k[s[i]] < k[s[i+1]]:
                sum += k[s[i+1]] - k[s[i]] 
                i += 2
            else:
                sum += k[s[i]]
                i +=1

        return sum

          