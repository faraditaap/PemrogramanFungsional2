from collections import namedtuple
print('\nProgram Koleksi Kartu Uno \n')

Card = namedtuple('Card',['rank','color','type'])

class IsiKartu:
    ranks = [str(n) for n in range(0, 9)] + list('SRWB')
    colors = 'red yellow green blue'.split()
    types = 'ordinary action'.split()

    def __init__(self):
        self._cards = [Card(rank, color, type) for color in self.colors
                                         for rank in self.ranks
                                         for type in self.types]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
    
deck = IsiKartu()
print('banyak kartu uno : ')
print(len(deck))
print(deck[6])

#pilhan random
from random import choice
print("\n--- random choice ---")
print(choice(deck))

print(choice(deck))
print(choice(deck))

#slicing
print('\n-- slice is --')
print(deck[:3])
print(deck[8:10])

print('\nIterative operations ')
for card in deck[:3]:
    print(card)

print('\nAnti iteration operation ')
for card in reversed(deck[:3]):
    print(card)