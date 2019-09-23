import random

player_wallet = 100

def add_to_wallet():
    global player_wallet
    deposit_amount = input(f"Your current wallet balance is ${player_wallet:.2f}, how much would you like to add?   ")
    player_wallet += int(deposit_amount)
    return player_wallet

# add_to_wallet()

slot_odds = {
    '7': 3, 
    '777': 2, 
    'Cherry': 1, 
    'Apple': 1, 
    'Orange': 1,
    'Watermelon': 1,
    'Pear': 1,
    'Pineapple': 1,
    'Bar': 2,
    'Pot of Gold': 1
}

def pull_the_lever(slot_odds):
    global player_wallet
    player_wallet -= 10
    reel_one = random.choices(list(slot_odds.keys()), list(slot_odds.values()))
    reel_two = random.choices(list(slot_odds.keys()), list(slot_odds.values()))
    reel_three = random.choices(list(slot_odds.keys()), list(slot_odds.values()))
    reel_result = [reel_one[0], reel_two[0], reel_three[0]]
    print(reel_result)
    return reel_result

reel_result = pull_the_lever(slot_odds)

def winner_result(reel_result):
    if reel_result[0] == reel_result[1] and reel_result[1] == reel_result[2]:
        print('Winner')
    elif reel_result[0] == reel_result[1] or reel_result[0] == reel_result[2] or reel_result[1] == reel_result[2]:
        print('Partial Winner')
    else:
        print('Loser')

winner_result(reel_result)

def add_winnings_to_wallet(reel_result, slot_odds):
    global player_wallet
    if reel_result[0] == reel_result[1] and reel_result[1] == reel_result[2]:
        winnings = (1 / slot_odds[reel_result[0]]) * 1000
        player_wallet += winnings
        print(f'Congradulations! You have won ${winnings:.2f}')
    elif reel_result[0] == reel_result[1] or reel_result[0] == reel_result[2]:
        winnings = (1 / slot_odds[reel_result[0]]) * 200
        player_wallet += winnings
        print(f'Congradulations! You have won ${winnings:.2f}')
    elif reel_result[1] == reel_result[2]:
        winnings = (1 / slot_odds[reel_result[1]]) * 200
        player_wallet += winnings
        print(f'Congradulations! You have won ${winnings:.2f}')
    

add_winnings_to_wallet(reel_result, slot_odds)

print(player_wallet)