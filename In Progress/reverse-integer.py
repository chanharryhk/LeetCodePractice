class Solution(object):
    def reverse(self, x):
        revList = []
        ans = 0
        flag = False
        if x > 2147483647 or x < -2147483647:
            return 0
        if (x < 0):
            x *= -1
            flag = True
        # Converting value into string
        rev = str(x)
        # Iterating through all the letters to flip
        for i in range(len(rev) - 1, -1, -1):
            if int(rev[i]) == 0:
                continue
            revList.append(int(rev[i]))
        # Joined array back into a string then an integer
        ans = int(''.join(str(i) for i in revList))
        # Checking if the value was originally negative
        if flag is True:
            ans *= -1
        return ans
test = Solution()
print(test.reverse(99))

