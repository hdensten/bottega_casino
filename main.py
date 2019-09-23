import random

player_wallet = 0

def add_to_wallet():
    global player_wallet
    deposit_amount = input(f"Your current wallet balance is ${player_wallet:.2f}, how much would you like to add?   ")
    player_wallet += int(deposit_amount)
    return player_wallet

# add_to_wallet()

slot_odds = {
    '7': 3, 
    '777': 2, 
    'Cherry': 10, 
    'Apple': 10, 
    'Orange': 10,
    'Watermelon': 10,
    'Pear': 10,
    'Pineapple': 10,
    'Bar': 2,
    'Pot of Gold': 1
}

def pull_the_lever(slot_odds):
    reel_one = random.choices(list(slot_odds.keys()), list(slot_odds.values()))
    reel_two = random.choices(list(slot_odds.keys()), list(slot_odds.values()))
    reel_three = random.choices(list(slot_odds.keys()), list(slot_odds.values()))
    reel_result = [reel_one[0], reel_two[0], reel_three[0]]
    return reel_result
    
pull_the_lever(slot_odds)
