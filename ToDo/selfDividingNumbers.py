class Solution:
    def selfDividingNumbers(self, left, right):
        self.acceptedlist = []
        for i in range(left, right + 1):
            flag = 0
            print(i - left)
            print(self.acceptedlist[0])
            # for j in range(0, temp.length):
            #     if (i/j != 0):
            #         flag = 1
            # if (flag == 0):
            #     self.acceptedlist.append(i)
        print(self.acceptedlist)

blah = Solution()
blah.selfDividingNumbers(1,9)
