class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, idNumber, testScores):
        super().__init__(firstName, lastName, idNumber)
        self.testScores = testScores

    def calculate(self):
        average = sum(self.testScores) / len(self.testScores)

        if average > 89:
            return "O"
        elif average > 79:
            return "E"
        elif average > 69:
            return "A"
        elif average > 54:
            return "P"
        elif average > 39:
            return "D"
        else:
            return "T"
