#File:CS112_T2_2_20230727
#purpose:Number scrabble is played with the list of numbers between 1 and 9. Each player takes
#turns picking a number from the list. Once a number has been picked, it cannot be picked
#again. If a player has picked three numbers that add up to 15, that player wins the game.
#However, if all the numbers are used and no player gets exactly 15, the game is a draw
#Author:RAHAF LUAI MOOHIALDIN AL HAKIMI
#ID:20230727




def rules():
    print("Rules of the game:")
    print("1- The game consists of two players.")
    print("2- The objective of the game is for a player to select three numbers from 1 to 9 whose sum is 15.")
    print("3- The first player starts by placing a number, then the other player selects.")
    print("4- The steps repeat until one person gets three numbers whose sum is 15.")
    print("5- If neither player manages to achieve the sum of 15, the result is a draw.")

def get_15(numbers):
    for i in range(len(numbers) - 2):
        for j in range(i + 1, len(numbers) - 1):
            for k in range(j + 1, len(numbers)):
                if numbers[i] + numbers[j] + numbers[k] == 15:
                    return True
    return False

def number_scrabble_game():
    print("Welcome to Number Scrabble Game (: ")
    rules_input = input("If you do not know or want to understand the rules of the game press 1,"
                        " and if you know the rules press any button: ")

    if rules_input == '1':
        rules()

    player_wins = [0, 0]  # Track the number of wins for each player

    while True:
        numbers = list(range(1, 10))
        player_numbers = [[], []]  # "To harvest the number of players"

        for turn in range(1, 10):
            player_turn = (turn - 1) % 2  # "To determine which player goes first"
            choosen_player_numbers = player_numbers[player_turn]

            print("Player", player_turn + 1, "turn:")
            print("Available numbers:", numbers)

            while True:  # "If the player chooses a number that is not available, this action is taken."
                picked_number = int(input("Pick a number: "))

                if picked_number not in numbers:
                    print("Number is not available. please try again.")
                else:
                    break

            choosen_player_numbers.append(picked_number)
            numbers.remove(picked_number)  # "To remove the number after it's chosen."

            # Check all combinations of three numbers for the sum of 15
            if len(choosen_player_numbers) >= 3:
                if get_15(choosen_player_numbers):
                    print(f"Player {player_turn + 1} wins :) ")
                    player_wins[player_turn] += 1
                    break  # exit the inner loop

        else:
            print("It's a draw:( ")

        play_again = input("Do you want to play again? Press '1' for Yes, any other key to quit: ")
        if play_again != '1':
            break  # exit the outer loop to end the game

    print("Winning Statistics:")
    print(f"Player 1 wins: {player_wins[0]} times")
    print(f"Player 2 wins: {player_wins[1]} times")


number_scrabble_game()