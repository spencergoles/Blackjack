# Blackjack
# By: Spencer Goles @2019

import sys
from random import shuffle
from time import sleep


# 4 suites in a deck is 52 - 4*13 = 52
# In blackjack suite is irrelevant only facevalue is needed
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4


def deal(deck):
    hand = []
    for x in range(2):
        shuffle(deck)
        card = deck.pop()
        if card == 11: card = "J"
        if card == 12: card = "Q"
        if card == 13: card = "K"
        if card == 14: card = "A"
        hand.append(card)
    return hand

def countHand(hand):
    count = 0 
    for card in hand: 
        if card == "A":
	        if count >= 11: count+= 1
	        if count <11: count += 11
        if card == "J" or card == "Q" or card == "K":
            count += 10
        else: count += card
    return count 

def printScores(playerHand, dealerHand):
    print("\n\nYour hand is " + str(playerHand) + " with a total of " + str(countHand(playerHand)))
    print("The dealer's hand is " + str(dealerHand) + " with a total of " + str(countHand(dealerHand)) + "\n\n")


def hit(hand):
    card = deck.pop()
    if card == 11: card = "J"
    if card == 12: card = "Q"
    if card == 13: card = "K"
    if card == 14: card = "A"
    hand.append(card)
    return hand

def runGame():
    playerHand = deal(deck)
    dealerHand = deal(deck)
    while True:
        print("Dealer's Card: ", str(dealerHand[0]))
        print("Your Cards: " + str(playerHand[0]) + " and " + str(playerHand[1]))
        checkBlackjack(playerHand, dealerHand)
        response = input("\nHit or Stay? (H/S)\n\n")
        if response.lower() == "h":
            hit(playerHand)
            while countHand(dealerHand) < 17:
                hit(dealerHand)
            checkScore(playerHand, dealerHand)
            repeatMenu()
        elif response.lower() == "s": 
            while countHand(dealerHand) < 17:
                hit(dealerHand)
            checkScore(playerHand, dealerHand)
            repeatMenu()
        else:
            print("\n\nInvalid Input")



def checkScore(playerHand, dealerHand):
    if countHand(dealerHand) == 21:
        printScores(playerHand, dealerHand)
        print("The dealer has a blackjack, better luck next game.")
        repeatMenu()
    if countHand(playerHand) == 21:
        printScores(playerHand, dealerHand)
        print("You have a blackjack and win!")
        repeatMenu()
    if countHand(dealerHand) > 21:
        printScores(playerHand, dealerHand)
        print("The dealer has busted, you win!")
        repeatMenu()
    if countHand(playerHand) > 21:
        printScores(playerHand, dealerHand)
        print("You have busted and the dealer wins.")
        repeatMenu()
    if countHand(dealerHand) > countHand(playerHand):
        printScores(playerHand, dealerHand)
        print("The dealer has a higher score and wins.")
        repeatMenu()
    if countHand(playerHand) > countHand(dealerHand):
        printScores(playerHand, dealerHand)
        print("You have a higher score than the dealer and win!")
        repeatMenu()
    

def checkBlackjack(playerHand, dealerHand):
    if countHand(dealerHand) == 21:
        printScores(playerHand, dealerHand)
        print("The dealer has a blackjack, better luck next game.")
        repeatMenu()
    if countHand(playerHand) == 21:
        printScores(playerHand, dealerHand)
        print("You have a blackjack and win!")
        repeatMenu()


def repeatMenu():
    print("\n\n\n\nWould you like to play again? (Y/N)\n\n")
    response = input()
    if response.lower() == "y":
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4
        runGame()
    if response.lower() == "n":
        print("\n\nThanks for playing!\n")
        sleep(1)
        exit()
    else:
        print("\n\nInvalid Input")


if __name__ == "__main__":
    print("\nWelcome to Blackjack!\n\n")
    runGame()