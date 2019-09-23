import random

player_wallet = 0

def add_to_wallet():
    global player_wallet
    deposit_amount = input(f"Your current wallet balance is ${player_wallet:.2f}, how much would you like to add?   ")
    player_wallet += int(deposit_amount)
    return player_wallet

add_to_wallet()

slot_odds = {
    7: 3, 
    777: 2, 
    'Cherry': 10, 
    'Apple': 10, 
    'Orange': 10,
    'Watermelon': 10,
    'Pear': 10,
    'Pineapple': 10,
    'Bar': 2,
    'Pot of Gold': 1
}
