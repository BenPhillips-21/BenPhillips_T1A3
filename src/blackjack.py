import random
import sys



def calculate_hand(user_hand):
    result = 0
    for item in user_hand:
        if item == 'A':
            if result <= 10:
                result += 11
            else:
                result += 1
        elif item in ['J', 'K', 'Q']:
            result += 10
        else:
            result += int(item)
    return result

def play_again():
    again = input("Do ye wish to play again? (y/n): ")
    if again != "y":
        print("Thanks for playing!")
        sys.exit
    else:
        play_blackjack()

def hit():
    global user_hand
    user_hand += random.sample(deck, 1)
    print(user_hand)
    result_of_user_hand = calculate_hand(user_hand)  
    print(result_of_user_hand)
    if result_of_user_hand == 21:
        print("Blackjack! Ye win!")
        play_again()
    elif result_of_user_hand > 21:
        print("Yer busted!")
    else:
        user_input = input("Shall ye hit again or shall ye stand? (hit/stand) ")
        if user_input == 'hit':
            hit()
        elif user_input == 'stand':
            stand()
               

def stand():
    global dealer_hand
    global user_hand
    global result_of_dealer_hand
    while result_of_dealer_hand <= 21:
        dealer_hand += random.sample(deck, 1)
        result_of_dealer_hand = calculate_hand(dealer_hand)  
        print(f'The result of my hand is: {result_of_dealer_hand}')
        if result_of_dealer_hand == 21:
            print("I win!")
            play_again()
        elif result_of_dealer_hand == result_of_user_hand or result_of_dealer_hand == 22:
            print("Push")
            play_again()
        elif result_of_dealer_hand > 22:
            print("Dangit I'm busted!")
            play_again()
        
        

# deck of cards / player dealer hand



deck = [2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,
        'A', 'A', 'A', 'A', 'J', 'J', 'J', 'J', 'Q', 'Q', 'Q', 'Q', 'K', 'K', 'K', 'K']
dealer_hand = []
user_hand = []

# deal card function

dealer_hand += random.sample(deck, 2)
user_hand += random.sample(deck, 2)


print(f'Your hand: {user_hand}')
result_of_user_hand = calculate_hand(user_hand)  
print(f'({result_of_user_hand})')
if result_of_user_hand == 21:
    print("Blackjack! Ye win!")
    play_again()


result_of_dealer_hand = calculate_hand(dealer_hand)

print(f"Dealer's hand: {dealer_hand[0]}")

user_input = input("Shall ye hit or shall ye stand? (hit/stand) ")

if user_input == 'hit':
    hit()
elif user_input == 'stand':
    stand()

