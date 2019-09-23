import random

player_wallet = 0

def add_to_wallet():
    global player_wallet
    deposit_amount = input(f"\nYour current wallet balance is ${player_wallet:.2f}, how much would you like to add?   ")
    player_wallet += int(deposit_amount)
    return player_wallet


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

def pull_the_lever(slot_odds, bet):
    global player_wallet
    if player_wallet >= int(bet):
        player_wallet -= int(bet)
        reel_one = random.choices(list(slot_odds.keys()), list(slot_odds.values()))
        reel_two = random.choices(list(slot_odds.keys()), list(slot_odds.values()))
        reel_three = random.choices(list(slot_odds.keys()), list(slot_odds.values()))
        reel_result = [reel_one[0], reel_two[0], reel_three[0]]
        print(f'\n~[ {reel_result[0]} | {reel_result[1]} | {reel_result[2]} ]~\n')
    else:
        player_choice = input('Not enough money! Would you like to... \n 1 : Add to your wallet \n 2 : Cash out and leave \n')
        if player_choice == '1':
            add_to_wallet()
        else:
            print(f'${player_wallet:.2f} cashed out, goodbye!')
            exit()
    winner_result(reel_result)
    return reel_result

# reel_result = pull_the_lever(slot_odds)

def winner_result(reel_result):
    if reel_result[0] == reel_result[1] and reel_result[1] == reel_result[2]:
        print('Winner')
    elif reel_result[0] == reel_result[1] or reel_result[0] == reel_result[2] or reel_result[1] == reel_result[2]:
        print('Partial Winner')
    else:
        print('Loser')
    add_winnings_to_wallet(reel_result, slot_odds, bet)

# winner_result(reel_result)

def add_winnings_to_wallet(reel_result, slot_odds, bet):
    global player_wallet
    if reel_result[0] == reel_result[1] and reel_result[1] == reel_result[2]:
        winnings = (1 / slot_odds[reel_result[0]]) * 100 * int(bet)
        player_wallet += winnings
        print(f'Congradulations! You have won ${winnings:.2f}')
    elif reel_result[0] == reel_result[1] or reel_result[0] == reel_result[2]:
        winnings = (1 / slot_odds[reel_result[0]]) * 20 * int(bet)
        player_wallet += winnings
        print(f'Congradulations! You have won ${winnings:.2f}')
    elif reel_result[1] == reel_result[2]:
        winnings = (1 / slot_odds[reel_result[1]]) * 20 * int(bet)
        player_wallet += winnings
        print(f'Congradulations! You have won ${winnings:.2f}')
    navigation()
    

# add_winnings_to_wallet(reel_result, slot_odds)

# print(player_wallet)

def navigation():
    global player_wallet
    player_action = input(f'Would you like to... \n 1 : Play again \n 2 : Chash out and leave \n')
    if player_action == '1':
        reel_result = pull_the_lever(slot_odds, bet)
    elif player_action == '2':
        print(f'${player_wallet:.2f} cashed out, goodbye!')


print('\nWelcome to the Bottega Casino! Add money to your wallet to get started.')
add_to_wallet()
bet = input('\nSet the bet amount:   ')
# navigation()
reel_result = pull_the_lever(slot_odds, bet)