class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        mas = []
        a = 0
        mas += [a]
        for i in gain:
            mas += [a+i]
            a += i
        maxim = -1000
        for i in mas:
            if i > maxim:
                maxim = i
        return(maxim)
