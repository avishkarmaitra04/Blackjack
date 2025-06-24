import random
logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


def deal_card():
    return random.choice([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "PUSH 🙃", 0
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱", -1
    elif u_score == 0:
        return "Win with a Blackjack 😎", 1.5
    elif u_score > 21:
        return "You went over. You lose 😭", -1
    elif c_score > 21:
        return "Opponent went over. You win 😁", 1
    elif u_score > c_score:
        return "You win 😃", 1
    else:
        return "You lose 😤", -1

def update_stats(stats, result):
    stats["games"] += 1
    if "win" in result.lower():
        stats["wins"] += 1
    elif "lose" in result.lower():
        stats["losses"] += 1
    elif "push" in result.lower():
        stats["pushes"] += 1

def print_stats(stats):
    print("\n📊 Game Stats:")
    print(f"  Games Played: {stats['games']}")
    print(f"  Wins: {stats['wins']}")
    print(f"  Losses: {stats['losses']}")
    print(f"  Pushes: {stats['pushes']}\n")

def ask_yes_no(prompt):
    while True:
        choice = input(prompt + " (y/n): ").lower()
        if choice in ['y', 'n']:
            return choice
        print("Invalid input. Please enter 'y' or 'n'.")

def play_hand(hand, bet, balance):
    while True:
        score = calculate_score(hand)
        if score == 0:
            print(f"\nYour hand: {hand} → Blackjack! 🎉")
            break
        else:
            print(f"\nYour hand: {hand}, score: {score}")
        if score > 21:
            break
        move = input("Type 'y' to hit, 'n' to stand, or 'exit' to quit: ").lower()
        if move == 'exit':
            return 'exit', hand, score, bet
        elif move == 'y':
            hand.append(deal_card())
        elif move == 'n':
            break
        else:
            print("Invalid input.")
    return 'continue', hand, calculate_score(hand), bet

def play_game(balance, stats):
    cards = [deal_card(), deal_card()]
    dealer = [deal_card(), deal_card()]
    hands = [cards]
    bets = []

    print(f"\nYour balance: ₹{balance}")
    while True:
        bet_input = input("Enter your bet amount or type 'exit': ₹")
        if bet_input == 'exit':
            return 'exit', balance
        try:
            bet = int(bet_input)
            if 0 < bet <= balance:
                break
            else:
                print("Invalid bet.")
        except ValueError:
            print("Enter a valid number.")
    bets.append(bet)
    insurance_bet = 0

    score = calculate_score(cards)
    if score == 0:
        print(f"\nYour cards: {cards} → Blackjack! 🎉")
    else:
        print(f"\nYour cards: {cards}, score: {score}")
    print(f"Dealer's first card: {dealer[0]}")

    # Insurance
    if dealer[0] == 11 and balance - bet >= bet // 2:
        if ask_yes_no("Dealer shows Ace. Take insurance?") == 'y':
            insurance_bet = bet // 2
            print(f"Insurance placed: ₹{insurance_bet}")

    # Split
    if cards[0] == cards[1] and balance >= bet * 2:
        if ask_yes_no("Split?") == 'y':
            hands = [[cards[0], deal_card()], [cards[1], deal_card()]]
            bets = [bet, bet]
            balance -= bet

    # player hands
    for i, hand in enumerate(hands):
        print(f"\nPlaying Hand {i+1}: {hand}")
        if len(hand) == 2 and balance >= bets[i]:
            if ask_yes_no("Double down?") == 'y':
                bets[i] *= 2
                hand.append(deal_card())
        status, hand, score, final_bet = play_hand(hand, bets[i], balance)
        if status == 'exit':
            return 'exit', balance
        hands[i] = hand
        bets[i] = final_bet

    dealer_score = calculate_score(dealer)
    if dealer_score == 0:
        print(f"\nDealer has Blackjack! 😱 Cards: {dealer}")
        for i, hand in enumerate(hands):
            score = calculate_score(hand)
            result, payout = compare(score, 0)
            print(f"Hand {i+1}: {hand} → {result} (Bet: ₹{bets[i]})")
            balance += int(bets[i] * payout)
            update_stats(stats, result)
        if insurance_bet:
            print(f"Insurance won! +₹{insurance_bet * 2}")
            balance += insurance_bet * 2
        else:
            print("No insurance taken.")
        print(f"Your updated balance: ₹{balance}")
        return 'continue', balance

    # Dealer plays normally
    while dealer_score < 17:
        dealer.append(deal_card())
        dealer_score = calculate_score(dealer)

    if dealer_score == 0:
        print(f"\nDealer's cards: {dealer} → Blackjack! 😱")
    else:
        print(f"\nDealer's cards: {dealer}, score: {dealer_score}")

    for i, hand in enumerate(hands):
        score = calculate_score(hand)
        result, payout = compare(score, dealer_score)
        print(f"Hand {i+1}: {hand} → {result} (Bet: ₹{bets[i]})")
        balance += int(bets[i] * payout)
        update_stats(stats, result)

    if insurance_bet and dealer_score != 0:
        print("Insurance lost.")
        balance -= insurance_bet

    print(f"Your updated balance: ₹{balance}")
    return 'continue', balance

# game starts
INITIAL_BALANCE = 1000
print(logo)
print("🃏 Welcome to Blackjack 🃏")

while True:
    balance = INITIAL_BALANCE
    stats = {"games": 0, "wins": 0, "losses": 0, "pushes": 0}

    while balance > 0:
        status, balance = play_game(balance, stats)
        if status == 'exit':
            print("\n👋 You exited the game.")
            break

    if balance <= 0:
        print("\n💸 You're out of money! Dealer wins.")
    print_stats(stats)

    if ask_yes_no("Play again?") != 'y':
        print("Thanks for playing! 🎉")
        break
    else:
        print("\n🆕 New game starting...\n")
