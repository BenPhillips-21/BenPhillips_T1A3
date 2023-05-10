import random
import sys

print("You're sitting at a blackjack table in an old Saloon.")
print("Across from you is the old dealer")
print("To your left is a very muscular man")
print("To your right is a young man with a big smile on his face")
choice = input("Do you want to play blackjack? (blackjack), talk to the muscular man? (muscles) or to the funny guy? (funny)\n")

if choice == "muscles":
    def protein_calculator(age, weight, gender, activity, goals):
        if gender == 'male':
            bmr = 88.36 + (13.4 * weight) + (4.8 * height) - (5.7 * age)
        elif gender == 'female':
            bmr = 447.6 + (9.2 * weight) + (3.1 * height) - (4.3 * age)

        if activity == 'sedentary':
            tdee = bmr * 1.2
        elif activity == 'lightly active':
            tdee = bmr * 1.375
        elif activity == 'moderately active':
            tdee = bmr * 1.55
        elif activity == 'very active':
            tdee = bmr * 1.725
        else:
            tdee = bmr * 1.9

        if goals == 'gain':
            protein_calories = tdee * (22/100)
            protein = protein_calories / 4
            print(f"You should eat {protein:.2f} grams of protein a day to put on mass")
        elif goals == 'lose':
            protein_calories = tdee * (20/100)
            protein = protein_calories / 4
            print(f"You should eat {protein:.2f} grams of protein a day to lose weight")
        else: 
            protein_calories = tdee * (18/100)
            protein = protein_calories / 4
            print(f"You should eat {protein:.2f} grams of protein a day to maintain your current mass")

        return protein

    age = int(input("Enter your age: "))
    height = float(input("Enter your height: (cm) "))
    weight = float(input("Enter your weight: (kg) "))
    gender = input("Enter your gender (male/female): ")
    activity = input("Enter your level of activity (sedentary/lightly active/moderately active/very active/extremely active): ")
    goals = input("Enter your goals (gain/maintain/lose):  ")

    protein_requirement = protein_calculator(age, weight, gender, activity, goals)

elif choice == "blackjack": 
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
            play_again()
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
            print(f'My current hand is {dealer_hand}')
            dealer_hand += random.sample(deck, 1)
            result_of_dealer_hand = calculate_hand(dealer_hand) 
            print(f'My new hand is {dealer_hand}') 
            print(f'The sum of my hand is: {result_of_dealer_hand}')
            if result_of_dealer_hand == 21:
                print("I win!")
                play_again()
            elif result_of_dealer_hand > result_of_user_hand and result_of_dealer_hand <= 21:
                print("I win!")
                play_again()
            elif result_of_dealer_hand == result_of_user_hand or result_of_dealer_hand == 22:
                print("Push")
                play_again()
            elif result_of_dealer_hand > 22:
                print("Dangit I'm busted!")
                play_again()
            
    deck = [2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,
            'A', 'A', 'A', 'A', 'J', 'J', 'J', 'J', 'Q', 'Q', 'Q', 'Q', 'K', 'K', 'K', 'K']
    dealer_hand = []
    user_hand = []

    dealer_hand += random.sample(deck, 2)
    user_hand += random.sample(deck, 2)

    print(f'Your hand: {user_hand}')
    result_of_user_hand = calculate_hand(user_hand)  
    print(f'({result_of_user_hand})')
    if result_of_user_hand == 21:
        print("Blackjack! Ye win!")
        play_again()

    result_of_dealer_hand = calculate_hand(dealer_hand)
    print(f"Dealer's first card: {dealer_hand[0]}")
    user_input = input("Shall ye hit or shall ye stand? (hit/stand) ")

    if user_input == 'hit':
        hit()
    elif user_input == 'stand':
        stand()

# elif choice == "funny":
#     # guy that tells a random joke

# elif choice == "shoot":
#     # game in which you have to guess a number or guy shoots you

# else:
