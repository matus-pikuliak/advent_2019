import numpy as np

deck_size = 10007
cards = np.arange(deck_size)

for line in open('input'):
    words = line.split()

    if words[1] == 'with':
        inc = int(words[-1])
        new_cards = np.zeros(cards.shape, dtype=np.int)
        for i in cards:
            new_cards[inc * i % deck_size] = cards[i]
        cards = new_cards
    elif words[1] == 'into':
        cards = np.flip(cards)
    else:
        cut = int(words[-1])
        cards = np.concatenate((cards[cut:], cards[:cut]))
    print(cards)

print(np.where(cards == 2019))
