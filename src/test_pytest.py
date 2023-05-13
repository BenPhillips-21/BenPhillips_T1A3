import random
import pytest

# pytest that asserts that the calculate hand function returns the correct values
def test_calculate_hand():
    assert calculate_hand(['A', 'J']) == 21
    assert calculate_hand(['4', '5', '6']) == 15
    assert calculate_hand(['10', 'K']) == 20
    assert calculate_hand(['A', '3', '5', 'A']) == 20
    assert calculate_hand(['2', '1', '2', '9']) == 14


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

# in order to do the protein calculator test, run pytest and input the values below and they will receive the correct results

def test_protein_calculator():
     assert protein_calculator(21, 180, 80, 'male', 'very active', 'gain') == 180.7046175
     assert protein_calculator(30, 160, 55, 'female', 'sedentary', 'lose') == 79.23599999999999
     assert protein_calculator(70, 195, 105, 'male', 'moderately active', 'maintain') == 141.75710999999998



def protein_calculator(age, height, weight, gender, activity, goals):
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
        
while True:
    try:
        age = int(input("How old are you? "))
        if not (0 <= age <= 100):
            raise ValueError("Age must be between 0 and 100")
        break
    except ValueError:
        print("Please enter a valid integer for your age (0-100)")
        
while True:
    try:
        height = float(input("How tall are you in centimetres? "))
        if not (0 <= height <= 250):
            raise ValueError("Please enter a realistic height. (0-250)")
        break
    except ValueError as e:
        print(e)

while True:
    try:
        weight = float(input("How much do you weigh in kilograms? "))
        if not (0 <= weight <= 500):
            raise ValueError("Please enter a realistic weight. (0-500)")
        break
    except ValueError as e:
        print(e)
        
while True:
    try:
        gender = input("My eye sight ain't too good, you a male or female? (male/female) ")
        if gender.lower() not in ['male', 'female']:
            raise ValueError("Please enter either 'male' or 'female' for your gender.")
        break
    except ValueError as e:
        print(e)
        
while True:
    try:
        activity = input("How active are you? (sedentary/lightly active/moderately active/very active/extremely active) ")
        if activity.lower() not in ['sedentary', 'lightly active', 'moderately active', 'very active', 'extremely active']:
            raise ValueError("Please enter a valid activity level.")
        break
    except ValueError as e:
        print(e)

while True:
    try:
        goals = input("And are you trying to gain, maintain, or lose weight? (gain, maintain, lose)  ")
        if goals.lower() not in ['gain', 'maintain', 'lose']:
            raise ValueError("Please enter either 'gain', 'maintain', or 'lose' for your weight goals.")
        break
    except ValueError as e:
        print(e)

protein_requirement = protein_calculator(age, weight, height, gender, activity, goals)