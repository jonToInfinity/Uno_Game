import random

#  Uno deck
colors = ["Red", "Yellow", "Green", "Blue"]
values = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Skip", "Reverse", "Draw Two"]
wild_cards = ["Wild", "Wild Draw Four"]

deck = [(color, value) for color in colors for value in values] + [(color, wild) for color in colors for wild in wild_cards]

# Shuffle the deck
random.shuffle(deck)

# Initialize players and hands
num_players = 4  # Change this for different numbers of players
players = [f"Player {i}" for i in range(1, num_players + 1)]
hands = {player: [] for player in players}

# Deal initial cards to players
for _ in range(7):
    for player in players:
        card = deck.pop()
        hands[player].append(card)

# Initialize game state
discard_pile = [deck.pop()]

# Define a function to check if a card can be played
def can_play(card, top_card):
    color, value = card
    top_color, top_value = top_card
    return color == top_color or value == top_value or color == "Wild"

# Game loop
current_player_index = 0
direction = 1  # 1 for clockwise, -1 for counterclockwise
while True:
    current_player = players[current_player_index]
    top_card = discard_pile[-1]

    print(f"{current_player}'s turn")
    print(f"Top card: {top_card[0]} {top_card[1]}")

    valid_cards = [card for card in hands[current_player] if can_play(card, top_card)]
    if not valid_cards:
        print("No valid cards. Drawing a card.")
        drawn_card = deck.pop()
        hands[current_player].append(drawn_card)
    else:
        print("Valid cards in hand:")
        for i, card in enumerate(valid_cards):
            print(f"{i}: {card[0]} {card[1]}")

        choice = input("Enter the index of the card to play or 'd' to draw a card: ")

        if choice == 'd':
            drawn_card = deck.pop()
            hands[current_player].append(drawn_card)
        else:
            choice = int(choice)
            selected_card = valid_cards[choice]
            hands[current_player].remove(selected_card)
            discard_pile.append(selected_card)

            if len(hands[current_player]) == 0:
                print(f"{current_player} wins!")
                break

            if selected_card[1] == "Reverse":
                direction *= -1
            elif selected_card[1] == "Skip":
                current_player_index += direction

    current_player_index = (current_player_index + direction) % num_players



