import random

values,colors = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King'], ['Hearts', 'Diamonds', 'Spades', 'Clubs']
i = True

def menu():

    print("""
--------------
1. Pick up
x. End (Winner is decided)
r. Restart          
--------------          
""")
    
    choice = input().lower()
    if choice == "1":
        cards.return_randcard()
    
    elif choice == "r":
        cards.restart()
        game.start()
    elif choice == "x":
        cards.end()
    else:
        print("Invalid")
        menu()

total_score= 0
class Cards():

    def __init__(self):
        #deck and all that 
        self.deck = [(value,color) for color in colors for value in values]
        self.used = []
        self.hand = []
        self.current_count =  len(self.deck)
        #scoring
        self.total_score = total_score
        #dealer
        self.dealer = []
        self.dealer_score = 0

    def return_randcard(self):
        if self.current_count - 1 > -1:
            cardnum = random.randint(0,self.current_count - 1)
            self.current_card =  self.deck[cardnum]
            try:        
                self.total_score += int(self.current_card[0]) 
            except:
                self.total_score+=10
                if self.current_card[0] == 'Ace':
                    self.total_score += 1
            self.used.append(self.deck[cardnum])
            self.hand.append(self.deck[cardnum])
            self.deck.pop(cardnum)
            self.current_count -= 1
            print("Current Hand:", self.hand)        
            print("Current Score:", self.total_score)
        else:
            print("Deck Empty")
        
    def first_card(self):
        cardnum = random.randint(0,self.current_count - 1)
        self.current_card =  self.deck[cardnum]
        try:
            self.total_score += int(self.current_card[0]) 
        except:
            self.total_score+=10
            if self.current_card[0] == 'Ace':
                self.total_score += 1

        self.used.append(self.deck[cardnum])
        self.hand.append(self.deck[cardnum])
        self.deck.pop(cardnum)
        self.current_count -= 1

        print("Current Hand:", self.hand)
        print("Current Score:", self.total_score)

    def dealer_cards(self):
        go=0
        while go<2:
            cardnum = random.randint(0,self.current_count - 1)
            self.current_card =  self.deck[cardnum]
            try:        
                self.dealer_score += int(self.current_card[0]) 
            except:
                self.dealer_score+=10
                if self.current_card[0] == 'Ace':
                    self.dealer_score += 1

            self.used.append(self.deck[cardnum])
            self.dealer.append(self.deck[cardnum])
            self.deck.pop(cardnum)
            self.current_count -= 1

            go+=1

    def end(self):

        if self.dealer_score > self.total_score and self.dealer_score<= 21:
            print("Dealer Hand:", self.dealer)
            print("Your Score:",self.total_score,"Dealer Score:", self.dealer_score)
            print("Dealer Wins",self.dealer)

        elif self.dealer_score<self.total_score and self.total_score<=21:
            print("Dealer Hand:", self.dealer)
            print("Your Score:",self.total_score,"Dealer Score:", self.dealer_score)
            print("You win", self.hand)

        elif self.dealer_score == self.total_score and self.total_score <=21:
            print("Dealer Hand:", self.dealer)
            print("Your Hand:", self.hand)
            print("Your Score:",self.total_score,"Dealer Score:", self.dealer_score)
            print("DRAW")

        elif self.dealer_score <= 21 and self.total_score>21:
            print("Dealer Hand:", self.dealer)
            print("Your Hand:", self.hand)
            print("Your Score:",self.total_score,"Dealer Score:", self.dealer_score)
            print("YOU BUST")

        else:
            print("Dealer Hand:", self.dealer)
            print("Your Hand:", self.hand)
            print("Your Score:",self.total_score,"Dealer Score:", self.dealer_score)
            print("DEALER BUST")

        cards.restart()
        game.start()




    def restart(self):
        #deck and all that 
        self.deck = [(value,color) for color in colors for value in values]
        self.used = []
        self.hand = []
        self.current_count =  len(self.deck)
        #scoring
        self.total_score = total_score
        #dealer
        self.dealer = []
        self.dealer_score = 0

class MainGame(Cards):
    def __init__(self):
        super().__init__()
        pass

    def start(self):
        cards.first_card()
        cards.dealer_cards()

    def mainloop(i):
        while i:
            menu()

cards = Cards()
game = MainGame()
game.start()
game.mainloop()