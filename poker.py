import sys
from collections import Counter

def parse_hand(hand):
    if len(hand) != 5:
        raise AssertionError("Wrong amount of cards")
    handnumbers = {'2': 2, '3' : 3, '4': 4, '5': 5, '6': 6, '7': 7, '8' : 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    return sorted([handnumbers[card] for card in hand], reverse=True)


def evaluate_hand(hand):
    parsed_hand = parse_hand(hand)
    counts = Counter(parsed_hand)
    values = sorted(list(counts.values()), reverse=True)
    if values == [4,1]:           #Four of a kind
        return 5, parsed_hand
    elif values == [3,2]:         #Full House
        return 4, parsed_hand
    elif values == [3,1,1]:       #Triples
        return 3, parsed_hand
    elif values == [2, 2, 1]:     #Two pairs
        return 2, parsed_hand
    elif values == [2, 1, 1, 1]:  #Pair
        return 1, parsed_hand
    else:                         #Highest card
        return 0, parsed_hand


def compare_hands(hand1, hand2):
    hand1_value, numbers1 = evaluate_hand(hand1)
    hand2_value, numbers2 = evaluate_hand(hand2)
    if hand1_value > hand2_value:
        print(f"{hand1} {hand2} => First hand wins!")
    elif hand1_value < hand2_value: 
        print(f"{hand1} {hand2} => Second hand wins!")
    elif hand1_value == hand2_value:
        if numbers1 > numbers2:
            print(f"{hand1} {hand2} => First hand wins!")
        elif numbers1 < numbers2:
            print(f"{hand1} {hand2} => Second hand wins!")
        else: 
            print(f"{hand1} {hand2} => It's a tie!")

def main():
    compare_hands(sys.argv[1], sys.argv[2])    

if __name__ == "__main__":
    main()
