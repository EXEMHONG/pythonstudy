import random

def roll_dice():
    """Simulate rolling a 6-sided dice."""
    return random.randint(1, 6)

def ladder_game():
    print("Welcome to the Ladder Game!")
    print("You are at the bottom of the ladder.")
    position = 0
    
    while position < 10:  # The goal is to reach position 10
        input("Press Enter to roll the dice...")
        dice_value = roll_dice()
        print("You rolled:", dice_value)
        
        if dice_value in [1, 2]:  # Move down the ladder
            print("Oops! You move down one step.")
            position -= 1
        elif dice_value in [3, 4, 5]:  # Move up the ladder
            print("Great! You move up one step.")
            position += 1
        else:  # Move up two steps
            print("Wow! You move up two steps.")
            position += 2
        
        print("Your current position:", position)
        print("-------------------------")
    
    print("Congratulations! You reached the top of the ladder.")

# Run the ladder game
ladder_game()
