from collections import defaultdict


def readInput():
    cards = []
    with open("input.txt","r") as file:
        for line in file:
            parts = line.strip().split(": ")[1]
            winning, your_numbers = parts.split(" | ")
            winning_set = set(winning.split())  # Convert to set for quick lookup
            your_numbers_list = your_numbers.split()
            matches = sum(1 for i in your_numbers_list if i in winning_set)
            cards.append(matches)
    return cards

def countCards(cards):
    card_copies = defaultdict(int)

    for i in range(len(cards)):
        card_copies[i] +=1

    for i,matches in enumerate(cards):
        for j in range(1,matches+1):
            if i+j<len(cards):
                card_copies[i+j] += card_copies[i]

    return sum(card_copies.values())



if __name__=='__main__':
    cards = readInput()
    total = countCards(cards)
    print("Total number of scratch cards:", total)
