class Solution:
    def frequencySort(self, s: str) -> str:
        count = collections.Counter(s)
        lheap = heapq.nlargest(len(count), count.keys(), key=count.get)
        print(count)
        ans = ""
        while lheap:
            l = lheap.pop(0)
            for i in range(count[l]):
                ans += l
        return ans