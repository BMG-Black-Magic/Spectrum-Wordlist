
import itertools

with open("adjectives.txt") as f:
    adjectives = [line.strip() for line in f if line.strip()]

with open("nouns.txt") as f:
    nouns = [line.strip() for line in f if line.strip()]

with open("numbers.txt") as f:
    numbers = [line.strip() for line in f if line.strip()]

with open("wordlist.txt", "w") as out:
    for adj, noun, num in itertools.product(adjectives, nouns, numbers):
        out.write(f"{adj}{noun}{num}\n")

print("Done!")
