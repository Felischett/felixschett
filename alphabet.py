alphabet = "abcdefghijklmnopqrstuvwxyz"
def firstTask():
    alphabet_dict = {letter: i for i, letter in enumerate(alphabet)}

    print(alphabet_dict)

def secondTask():
    for i, letter in enumerate(alphabet):
        print(i, letter)


def main():
    firstTask()
    secondTask()

if _name_ == "_main_":
    main()