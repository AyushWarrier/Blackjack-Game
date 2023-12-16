import random

logo = ("""
    ____  _            _    _            _                
    | __ )| | __ _  ___| | _| | __ _  ___| | _
    |  _ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    | |_) | | (_| | (__|   <| | (_| | (__|   <
    |____/|_|\__,_|\___|_|\_\_|\__,_|\___|_|\_\ 
    """)

def get_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_total(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare_scores(player_total, computer_total):
    if player_total == computer_total:
        return "😐 Draw"
    elif computer_total == 0:
        return "😭 Lose, opponent has BlackJack"
    elif player_total == 0:
        return "🎉 Win with a BlackJack"
    elif player_total > 21:
        return "😬 You went over. You lose"
    elif computer_total > 21:
        return "🥳 Opponent went over. You win"
    elif player_total > computer_total:
        return "🏆 You Win"
    else:
        return "😢 You Lose"

def play_blackjack():
    print(logo)
    
    player_cards = []
    computer_cards = []
    game_over = False

    for _ in range(2):
        player_cards.append(get_card())
        computer_cards.append(get_card())
        
    while not game_over:
        player_total = calculate_total(player_cards)
        computer_total = calculate_total(computer_cards)
        print(f"Your cards: {player_cards}, current score: {player_total}")
        print(f"Computer's first card: {computer_cards[0]}")

        if player_total == 0 or computer_total == 0 or player_total > 21:
            game_over = True
        else:
            player_should_draw = input("Type 'y' to get another card, type 'n' to pass: ")
            if player_should_draw == 'y':
                player_cards.append(get_card())
            else:
                game_over = True

    while computer_total != 0 and computer_total < 17:
        computer_cards.append(get_card())
        computer_total = calculate_total(computer_cards)
        
    print(f"Your final hand: {player_cards}, final score: {player_total}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_total}")
    print(compare_scores(player_total, computer_total))

while input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower() == 'y':
    play_blackjack()
