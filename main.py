player_wallet = 0

def add_to_wallet():
    global player_wallet
    deposit_amount = input(f"Your current wallet balance is ${player_wallet:.2f}, how much would you like to add?   ")
    player_wallet += int(deposit_amount)
    return player_wallet

add_to_wallet()