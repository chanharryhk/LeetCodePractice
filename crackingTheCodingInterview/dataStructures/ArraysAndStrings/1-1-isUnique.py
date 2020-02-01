class Soln():
    def isUnique(self, string):
        dict = {}
        for i in string:
            if i in dict:
                return False
            dict[i] = True
        return True


s = "helWrd"
solution = Soln()
print(solution.isUnique(s))