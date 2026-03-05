#This program simulates 100,000 poker hands and analyzes how often each hand type appears.
#For every round, create_deck() generates a random 5-card hand. The functions() routine
# checks this hand and identifies whether it contains
# a Pair, Two Pairs, Three of a Kind, Straight, Flush, Full House, Four of a Kind, or nothing special.
# The main loop repeats this process 100,000 times, and statisticUpdate() counts each detected combination.
# At the end, the program prints how many times each hand type occurred and the percentage of the total simulations.

import random
from collections import Counter
import time
import functools

def timer_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_zeit = time.perf_counter()

        ergebnis = func(*args, **kwargs)

        end_zeit = time.perf_counter()
        laufzeit = end_zeit - start_zeit
        print(f"Laufzeit: {laufzeit:.6f} Sekunden")

        return ergebnis

    return wrapper


RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Bube", "Dame", "König", "Ass"]
RINDEX = {r: i for i, r in enumerate(RANKS)}


def create_deck():
    c = 4
    n = 13
    pull = 4
    hand = {}
    handCount = 0
    colour = ["Kreuz", "Pik", "Herz", "Karo"]

    cards = {
        "Kreuz": ["2", "3", "4", "5", "6", "7", "8", "9", "10","Bube", "Dame", "König", "Ass"],
        "Pik":   ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Bube", "Dame", "König", "Ass"],
        "Herz":  ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Bube", "Dame", "König", "Ass"],
        "Karo":  ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Bube", "Dame", "König", "Ass"]
    }

    while handCount <= pull:
        handCount = 0
        num = random.randrange(c)
        col = random.randrange(n)

        if colour[num] not in hand:
            hand[colour[num]] = []

        hand[colour[num]].append(cards[colour[num]][col])

        for x in range(c):
            if colour[x] in hand:
                handCount += len(hand[colour[x]])

    print(hand)
    return hand

def functions(hand: dict):
    rank_count = Counter()
    suit_count = {}
    unique_values = set()

    for suit, rank_list in hand.items():
        suit_count[suit] = len(rank_list)
        for r in rank_list:
            rank_count[r] += 1
            unique_values.add(RINDEX[r])

    # Paar / Drilling / Poker
    pair = any(v == 2 for v in rank_count.values())
    triple = any(v == 3 for v in rank_count.values())
    poker = any(v == 4 for v in rank_count.values())

    if pair:
        print("Paar gefunden!")
    if triple:
        print("Drilling gefunden!")
    if poker:
        print("Poker (Vierling) gefunden!")

    # Flush:
    flush = any(v >= 5 for v in suit_count.values())
    if flush:
        print("Flush gefunden!")

    # Straße:
    sorted_vals = sorted(unique_values)
    run = 1
    street = False
    for i in range(1, len(sorted_vals)):
        if sorted_vals[i] == sorted_vals[i - 1] + 1:
            run += 1
            if run >= 5:
                street = True
                break
        else:
            run = 1
    if street:
        print("Straße gefunden!")

    anzahl_paare = list(rank_count.values()).count(2)

    if poker:
        kombi = "Vierling"
    elif triple and anzahl_paare == 1:
        kombi = "Full House"
    elif flush:
        kombi = "Flush"
    elif street:
        kombi = "Straße"
    elif triple:
        kombi = "Drilling"
    elif anzahl_paare == 2:
        kombi = "Zwei Paare"
    elif pair:
        kombi = "Paar"
    else:
        kombi = "Nichts"

    # optional: ausgeben, was erkannt wurde
    print("Kombination:", kombi)

    return kombi


def statisticUpdate(stat: dict, kombi: str):
    stat[kombi] += 1

@timer_decorator
def main():
    kombis = ["Nichts", "Paar", "Zwei Paare", "Drilling",
              "Straße", "Flush", "Full House", "Vierling"]
    statistics = {k: 0 for k in kombis}

    for i in range(100000):
        hand = create_deck()
        kombi = functions(hand)
        statisticUpdate(statistics, kombi)

    print("Statistik nach 100000 Spielen:")
    for k, v in statistics.items():
        anteil = (v / 100000) * 100
        print(f"{k:12s}: {v:7d} hat einen Anteil von {anteil:6.3f}%")

#main = timer_decorator(main)

if __name__ == "__main__":
    main()