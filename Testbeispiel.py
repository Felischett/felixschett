def search(liste: list, tar_sum: int):
    count = 0
    pairs = []

    for x in range(len(liste)):
        for i in range(x + 1, len(liste)):
            if liste[x] + liste[i] == tar_sum:
                count += 1
                pairs.append(liste[x])
                pairs.append(liste[i])

    if count > 0:
        return pairs
    else:
        return None


def pri(pairs: list):
    if pairs is None or len(pairs) == 0:
        print("es wurden keine paare gefunden")
    else:
        for i in range(0, len(pairs), 2):
            print(f"Das paar: {pairs[i]}, {pairs[i+1]} wurde gefunden")


def main():
    liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    tar_sum = 12

    pairs = search(liste, tar_sum)
    pri(pairs)


if __name__ == "__main__":
    main()