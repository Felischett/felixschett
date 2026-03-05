import unittest



# def combine(names, points):
#     combined = zip(names, points)
#     return combined

# def filtered(combined):
#     passed = list(filter(lambda x: x[1] > 50, combined))
#     return passed
#
# def sort(passed):
#     sorti = list(map(lambda x: f"name: {x[0]} has {x[1]} points", passed))
#     return sorti





def combine(names, ages):
    combined = zip(names, ages)
    return combined

def filtered(combined):
    passed = list(filter(lambda x: x[1] >= 18, combined))
    return passed

def str(passed):
    sorti = list(map(lambda x: f"{x[0]} is allowed because he's/she's {x[1]} years old!", passed))
    return sorti



def main():
    names = ["Felix", "Anna", "Klaus"]
    ages = [15, 20, 25]
    #points = [100, 70, 700, 80]

    #combined = combine(names, points)
    #passed = filtered(combined)
    #sorti = sort(passed)

    combined = combine(names, ages)
    passed = filtered(combined)
    sorti = str(passed)


    print(sorti)


def buildPassedList(names, scores):
    """
    Erstellt eine Liste der bestandenen Personen (>= 60 Punkte)
    mit zip, filter, map und lambda.
    """

    paired = zip(names, scores)

    passed = filter(lambda x: x[1] >= 60, paired)

    result = map(lambda x: f"{x[0]}: {x[1]}", passed)

    return list(result)


class TestbuildPassedList(unittest.TestCase):
    def test_some_pass(self):
        names = ["Felix", "Anna", "Clemens"]
        score = [80, 45, 60]

        result = buildPassedList(names,score)

        self.assertEqual(result, ["Felix: 80", "Clemens: 60"])

    def test_none_pass(self):
        names = ["Felix", "Anna"]
        score = [10, 20]

        result = buildPassedList(names, score)

        self.assertEqual(result, [])

    def test_all_pass(self):
        names = ["Felix", "Anna"]
        score = [100, 200]

        result = buildPassedList(names, score)

        self.assertEqual(result, ["Felix: 100", "Anna: 200"])



if __name__ == "__main__":
    main()
    unittest.main()