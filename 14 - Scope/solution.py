class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    # Add your code here

    def computeDifference(self):
        maximum = max(self.__elements)
        minimum = min(self.__elements)

        self.maximumDifference = maximum - minimum
