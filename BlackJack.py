from turtle import clear

from art import logo
import os
import random

game = "run"
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def clear():
    os.system('cls')

def get_cards(num):
    p_card = [cards[random.randint(0, len(cards) - 1)] for i in range(num)]
    return p_card


def sum_cards(hand):
    total = 0
    for num in hand:
        total += num
    return total


def retry(game):
    while True:
        choice = input("Would you like to play a game of Blackjack? Type 'y' or 'n': ")
        if choice == "y":
            clear()
            print(logo)
            return game
        elif choice == "n":
            game = "end"
            return game
        else:
            print("Error, invalid input.")


def over_21(total, hand):
    cont = True
    if total > 21:
        count = 0
        if 11 in hand:
            for card in hand:
                if card == 11:
                    hand[count] = 1
                    total = sum_cards(hand=hand)
                else:
                    count += 1
        else:
            cont = False
    return {"redeem": cont, "total": total, "hand": hand}


def get_result(ph, pt, ct):
    chance = over_21(total=pt, hand=ph)
    if chance["redeem"] == False or chance["total"] > 21:
        result = "It's a Bust! You Lose."
    elif chance["total"] > comp_info["total"]:
        result = "You Win"
    elif chance["total"] < comp_info["total"]:
        result = "You Lose"
    else:
        result = "It's a tie!"
    info = [result, ph, chance["total"], ct]
    return info


game = retry(game)


def add_card(player_hand):
    while True:
        user_choice = input("Type 'y' to get another card, or type 'n' to pass: ")
        if user_choice == "y":
            player_hand.append(get_cards(num=1)[0])
            break
        elif user_choice == "n":
            break
        else:
            print("Error, invalid input")
    return player_hand


while game == "run":
    player_hand = get_cards(num=2)
    comp_hand = get_cards(num=2)
    print(f"Your cards: {player_hand}")
    print(f"Computer's first card: {comp_hand[0]}")
    player_hand = add_card(player_hand)
    player_total = sum_cards(hand=player_hand)
    comp_total = sum_cards(hand=comp_hand)
    comp_info = over_21(total=comp_total, hand=comp_hand)
    info = get_result(ph=player_hand, pt=player_total, ct=comp_total)
    print(
        f"Your final hand: {info[1]}\nYour final total: {info[2]}\nComputer's final hand: {comp_hand}\nComputer's final total: {info[3]}\n{info[0]}")
    game = retry(game)