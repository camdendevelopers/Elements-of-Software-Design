#  File: Blackjack.py
#  Description: This program creates a Blackjack game using classes and instances. 
#               Good luck and please send your bets to me ;) 
#               Just kidding, just give me full points. Just kidding again!
#  Student's Name: Marcos Ortiz
#  Student's UT EID: mjo579
#  Course Name: CS 313E 
#  Unique Number: 51320
#
#  Date Created: 9/16/2016
#  Date Last Modified: 9/23/2016

import random

class Card():
    #Initialize Card object
    def __init__(self, suit, pip):
        self.suit = suit
        self.pip = pip

        if self.pip == "J" or self.pip == "Q" or self.pip == "K":
            self.value = 10
        elif self.pip == "A":
            self.value = 11
        else:
            self.value = int(self.pip)

    #Defines who the Card object will be printed
    def __str__(self):
        return "{}{}".format(self.pip, self.suit)

    #Method that retrives the value of Card object once it has been created.
    def getValue(self):
        return self.value

    #Method that changes the value of Card object (In case of Ace's)
    def setValue(self, newValue):
        self.value = newValue

class Deck():
    suitList = ["C", "D", "H", "S"]
    pipList = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    
    #Initialize Deck object
    def __init__(self):
        self.cardList = []
        for suit in Deck.suitList:
           for pip in Deck.pipList:
               card = Card(suit,pip)
               self.cardList.append(card)

   #Defines who the Card object will be printed
    def __str__(self):
        string = ""
        for i in range(1, len(self.cardList) + 1):
            card = str(self.cardList[i - 1])
            if i % 13 == 0:
                string += ("{:>4}".format(card) + "\n")
            else:
                string += "{:>4}".format(card)
        #return " ".join(str(card) for card in self.cardList) + "\n"
        return string

    #Method to shuffle deck
    def shuffle(self):
        random.shuffle(self.cardList)

    #Method that remove first card in deck and transfers it to player
    def dealOne(self, player):
        card = self.cardList.pop(0)
        player.handTotal += card.getValue()
        player.hand.append(card)

class Player():
    
    def __init__(self):
        self.hand = []
        self.handTotal = 0

    def __str__(self):
        return " ".join(str(card) for card in self.hand)

def opponentTurn(deck, dealer, opponent):
    aList = ["AH", "AD","AH","AS"]
    has_ace = False
    ace_idx = 0
    turn = ""

    #Check to see if initial hand contains and Ace and if true will create a flag and not index
    for i in range(len(opponent.hand)):
        card = str(opponent.hand[i])
        if card in aList:
            has_ace = True
            ace_idx = i
            print("Assuming 11 points for an ace you were dealt for now.")

    #Checks to see if player has natural blackjack. If true, it will end turn and start dealer turn
    if opponent.handTotal == 21:
        print("You hold {}".format(opponent))
        print("Blackjack!")
        print("Dealer's turn\n")
        return
            
    #Loop that prompts user for decision and will execute accordingly
    while turn != "2":
        print("You hold {} for a total of {}".format(opponent, opponent.handTotal))
        turn = input("1 (hit) or 2 (stay)?: ")

        if turn == "1":

            deck.dealOne(opponent)
            print("\nCard dealt: ", opponent.hand[len(opponent.hand) - 1])

            if opponent.handTotal > 21:
                if has_ace:
                    has_ace = False
                    card = opponent.hand[ace_idx]
                    card.setValue(1)
                    opponent.handTotal -= 10
                    print("Over 21. Switching an Ace from 11 points to 1.\nNew total: {}\n".format(opponent.handTotal))

                elif str(opponent.hand[len(opponent.hand)-1]) in aList:
                    ace_idx = len(opponent.hand)-1
                    card = opponent.hand[ace_idx]
                    card.setValue(1)
                    opponent.handTotal -= 10
                    print("Over 21. Switching an Ace from 11 points to 1.\nNew total: {}\n".format(opponent.handTotal))

                elif not has_ace:
                    #del opponent.hand[len(opponent.hand) - 1]
                    print("Over 21. You lose sucker!\n")
                    break
            elif opponent.handTotal == 21:
                print("21! My turn...\n")
                print("Dealer's turn\n")
                break
            else:
                print("New total: ", opponent.handTotal)
        else:
            #print("New total: ", opponent.handTotal)
            print("Staying with {}\n".format(opponent.handTotal))
            print("Dealer's turn")
            return


def dealerTurn(deck, dealer, opponent):
    aList = ["AH", "AD","AH","AS"]
    has_ace = False
    ace_idx = 0
    turn = ""

    #Display all cards down
    print("Your hand: {} for a total of {}".format(opponent, opponent.handTotal))
    print("Dealer's hand: {} for a total of {}\n".format(dealer, dealer.handTotal))

    #Check to see if dealer's hand contains Ace
    for i in range(len(dealer.hand)):
        card = str(dealer.hand[i])
        if card in aList:
            has_ace = True
            ace_idx = i
            print("Assuming 11 points for an ace you were dealt for now.")

    if opponent.handTotal > 21:
        return

    while dealer.handTotal <= opponent.handTotal:

        deck.dealOne(dealer)
        print("Card dealt: ", dealer.hand[len(dealer.hand) - 1])

        if dealer.handTotal > 21:
            if has_ace:
                has_ace = False
                card = dealer.hand[ace_idx]
                card.setValue(1)
                dealer.handTotal -= 10
                print("Over 21. Switching an Ace from 11 points to 1.\nNew total: {}\n".format(dealer.handTotal))

            elif str(dealer.hand[len(dealer.hand)-1]) in aList:
                has_ace = True
                ace_idx = len(dealer.hand)-1
                card = dealer.hand[ace_idx]
                card.setValue(1)
                dealer.handTotal -= 10
                print("Over 21. Switching an Ace from 11 points to 1.\nNew total: {}\n".format(dealer.handTotal))

            elif not has_ace:
                #del opponent.hand[len(opponent.hand) - 1]
                print("Dealer has {}. Dealer bust! You win.\n".format(dealer.handTotal))
                break
        elif dealer.handTotal == 21:
            print("21! Dealer wins!\n")
            break
        elif opponent.handTotal == dealer.handTotal:
            print("Push. Dealer wins\n")
            break
        else:
            print("New total: {}\n".format(dealer.handTotal))

    if dealer.handTotal > opponent.handTotal and dealer.handTotal < 21:
        print("Dealer wins!\n")
        return

        
def showHands(dealer, opponent):
    print("\n\nDealer shows {} faceup".format(dealer.hand[1]))
    print("You show {} faceup\n".format(opponent.hand[1]))
    print("You go first.\n")

def main():
    print("\n{}".format("----------------------------------------------------"))
    print("{:^52}".format("WELCOME TO BLACKJACK"))
    print("{}\n".format("----------------------------------------------------"))

    #Initialize players
    dealer = Player()
    opponent = Player()

    #Initialize deck and perform inital request
    deck = Deck()
    print("Initial deck:\n{}".format(deck))

    random.seed(50)
    #random.seed(25)
    deck.shuffle()
    print("Shuffled deck:\n{}".format(deck))

    deck.dealOne(opponent)      # face up
    deck.dealOne(dealer)        # face down
    deck.dealOne(opponent)      # face up
    deck.dealOne(dealer)        # face up

    print("Deck after dealing two cards each:\n{}".format(deck))

    showHands(dealer, opponent)

    opponentTurn(deck,dealer,opponent)

    dealerTurn(deck,dealer,opponent)

    print ("Game over.")
    print("----------")
    print ("Final hands:")
    print ("   Dealer:   ", dealer)
    print ("   Opponent: ", opponent)

main()