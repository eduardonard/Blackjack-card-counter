import os

import plotext as plt

from modules.new_deck import newdeck, cards_per_suit

###Inputs



#Deck


clear = lambda: os.system("cls")

probabilities = {}
actual_deck = newdeck
played_cards= []

def sum_of_cards(lis):
    res = []
    sum = 0
    aces = 0
    for i in lis:
        if i.upper() != "1":
            if i == "0":
                sum += 10
            else:
                sum += int(i)
        else:
            aces += 1
    if aces == 0:
        return [sum]
    for i in range(aces):
        res = [sum + 1, sum + 11]
    return res
    
def show_probabilities():
    for i in cards_per_suit:
        counter = actual_deck.count(i)
        probability = (counter/len(actual_deck)*10000)//10
        probabilities[i] = probability/10
    plt.clear_data()
    plt.simple_bar(list(probabilities.keys()), list(probabilities.values()))
    plt.show()


while True:
    clear()
    
    decision = input("\nTo play press player number \nto show previous card write 'show'\nto shuffle the deck write 'shuffle'\nto add cards from a csv write 'add'\n\n")
    if decision == "shuffle":
            actual_deck = newdeck
            played_cards = []
            probabilities = {}
            clear()
            continue
    elif decision == "show":
        input(f"{played_cards}")
        continue
    elif decision == "add":
        add_cards = []
        with open("runs/insameblackjackwin.txt", "r") as f:
            lines = f.read().splitlines()[2:]
            for i in lines:
                add_cards.extend(i.split())
        input("Cards added. Press a key for next game")
        played_cards.extend(add_cards)
        continue

    clear()
    print("New hand")
    
    players_dict = {}
    sum_dict = {}


    print("Input cards ")
    for i in range(1, int(decision) + 1):
        players_dict[i] = input(f"Player {i}:  ").split()
        first_card = players_dict[i][0]
        second_card = players_dict[i][1]
        played_cards.append(first_card)
        played_cards.append(second_card)
        actual_deck.remove(first_card)
        actual_deck.remove(second_card)
    
    players_dict["Dealer"] = input(f"Dealer's :  ").split()
    first_card = players_dict["Dealer"][0]
    played_cards.append(first_card)
    actual_deck.remove(first_card)
    print("------------------------------------------\n\n")

    for player in players_dict:
        
        
        while True:
            clear()
            print("\n\nRamaining cards")
            show_probabilities()
            
            print(f"\nPlayer {player}, cards: {players_dict[player]}")
            static_sum = sum_of_cards(players_dict[player])[0]
            if static_sum < 22:
                print("Sum: ",static_sum)
            else:
                input("Overflow")
                break
            new = input("Hit card or press enter: ")
            if new =="":
                break
            players_dict[player].append(new)
            played_cards.append(new)
            actual_deck.remove(new)
            
            

            
        

            
