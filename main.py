import random

total_deposited = 0
total_winnings = 0
profit = 0

def add_to_wallet():
    global player_wallet, total_deposited
    deposit_amount = float(input(f"\nYour wallet balance is ${player_wallet:.2f}, how much would you like to add?   "))
    player_wallet += deposit_amount
    total_deposited += deposit_amount
    navigation()
    return player_wallet

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

def pull_the_lever(slot_odds, bet):
    global player_wallet, total_winnings, total_deposited, profit
    if player_wallet >= bet:
        player_wallet -= bet
        reel_one = random.choices(list(slot_odds.keys()), list(slot_odds.values()))
        reel_two = random.choices(list(slot_odds.keys()), list(slot_odds.values()))
        reel_three = random.choices(list(slot_odds.keys()), list(slot_odds.values()))
        reel_result = [reel_one[0], reel_two[0], reel_three[0]]
        print(f'\n~[ {reel_result[0]} | {reel_result[1]} | {reel_result[2]} ]~\n')
        add_winnings_to_wallet(reel_result, slot_odds, bet)
        return reel_result
    else:
        player_choice = input('\nNot enough money! Would you like to... \n 1 : Add to your wallet \n 2 : Cash out and leave \n')
        if player_choice == '1':
            add_to_wallet()
        elif player_choice == '2':
            profit = (total_deposited + total_winnings) - total_deposited
            print(f'\n${player_wallet:.2f} cashed out, you made a profit of ${profit:.2f}\nGoodbye!\n')
            exit()
        else:
            print('Invalid input -> returning to main menu')
            navigation()

def add_winnings_to_wallet(reel_result, slot_odds, bet):
    global player_wallet, total_winnings
    if reel_result[0] == reel_result[1] and reel_result[1] == reel_result[2]:
        winnings = (1 / slot_odds[reel_result[0]]) * 100 * bet
        player_wallet += winnings
        total_winnings += winnings - bet
        print(f'Jack Pot! You win ${winnings:.2f}')
    elif reel_result[0] == reel_result[1] or reel_result[0] == reel_result[2]:
        winnings = (1 / slot_odds[reel_result[0]]) * 20 * bet
        player_wallet += winnings
        total_winnings += winnings - bet
        print(f'Not bad! You win ${winnings:.2f}')
    elif reel_result[1] == reel_result[2]:
        winnings = (1 / slot_odds[reel_result[1]]) * 20 * bet
        player_wallet += winnings
        total_winnings += winnings - bet
        print(f'Not bad! You win ${winnings:.2f}')
    else:
        total_winnings -= bet
        print('Better luck next time...')
    navigation()

def navigation():
    global player_wallet, profit, total_deposited, total_winnings
    player_action = input(f'\nWould you like to... \n 1 : PULL THE LEVER! \n 2 : Check wallet balance \n 3 : Cash out and leave \n')
    if player_action == '1':
        reel_result = pull_the_lever(slot_odds, bet)
    elif player_action == '2':
        print(f'\nYou have ${player_wallet:.2f} in your wallet.')
        navigation()
    elif player_action == '3':
        profit = (total_deposited + total_winnings) - total_deposited
        print(f'\n${player_wallet:.2f} cashed out, you made a profit of ${profit:.2f}\nGoodbye!\n')
    else:
        print('Invalid input -> try again')
        navigation()

print('\nWelcome to the Bottega Casino! Add money to your wallet to get started.')
player_wallet = float(input('\nHow much would you like add?   '))
total_deposited += player_wallet
bet = float(input('\nSet the bet amount:   '))
reel_result = pull_the_lever(slot_odds, bet)
