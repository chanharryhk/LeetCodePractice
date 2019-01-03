class Solution:
    def numJewelsInStones(self, J, S):
        print(J)
        print(S)
        # variable to store the amount of gems
        gemCount = 0
        dict = {i:S.count(i) for i in S}
        # Loop through all the possible gems
        for i in range(len(J)):
            # if the gem is inside our dictionary
            if J[i] in dict:
                # find the amount that is allocated to it
                gemCount += dict[J[i]]
        return gemCount

# tComplexity: O(n): O(n) + O(n) is just O(n)
# looping through elements in S and storing that as the key to how many
J = "z"
S = "ZZ"
test = Solution()
test.numJewelsInStones(J,S)