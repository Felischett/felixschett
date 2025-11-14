import random

def pick():
  minRange = 1
  maxRange = 46
  numbers = list(range(minRange, maxRange))
  n = 45
  pull = [] #liste

  for _ in range(6):
    idx = random.randrange(n)
    pull.append(numbers[idx])
    numbers[idx], numbers[n - 1] = numbers[n - 1], numbers[idx] 
    n -= 1

  return pull
# Returns 6 random unique numbers in the range 1–45


def statisticUpdate(stat: dict, liste):
  for z in liste:
    stat[z] += 1

# Updates the statistics by increasing the count for each drawn number


def main():
  minRange = 1
  maxRange = 46
  statistics = {z: 0 for z in range(minRange, maxRange)}


  first = pick()
  print("First pick:", sorted(first))
  statisticUpdate(statistics, first)

  for _ in range(999):
    pull = pick()
    statisticUpdate(statistics, pull)

  print("")
  for number, count in statistics.items():
   print(f"Number {number:2d}: {count}")

  maxNumber = max(statistics, key=statistics.get)
  minNumber = min(statistics, key=statistics.get)
  average = sum(statistics.values()) / len(statistics)

  print("")
  print(f"Most frequent number:  {maxNumber} with {statistics[maxNumber]} hits")
  print(f"Least frequent number:  {minNumber} with {statistics[minNumber]} hits")
  print(f"Average:               {average:.2f} hits per number")


if __name__ == "__main__":
  main()
