# Write a program to show up all the 52 deck of cards

Suits = ['CLUB', 'DIAMOND', 
         'HEART', 'SPADE']

SuitsUnicode = ["\u2663", "\u2665", 
         "\u2666", "\u2660"] 

Ranks = ['A', '2', '3', '4',
         '5', '6', '7', '8',
         '9', '10', 'J', 'Q', 'K']

for rank in Ranks:

    # for suit in Suits:
    #     print(f"{rank} of {suit}".ljust(16), end='')
    
    for suit in SuitsUnicode:
        print(f"{rank} of {suit}".ljust(16), end='')
        
    print()