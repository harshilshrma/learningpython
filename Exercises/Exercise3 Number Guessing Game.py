# You have to build a "Number Guessing Game," in which a winning number is set to some integer value.
# The Program should take input from the user, and if the entered number is less than the winning number,
# a message should display that the number is smaller and vice versa.

# Instructions:
# # 1. You are free to use anything we've studied till now.
# # 2. The number of guesses should be limited, i.e (5 or 9).
# # 3. Print the number of guesses left.
# # 4. Print the number of guesses he took to win the game.
# # 5. “Game Over” message should display if the number of guesses becomes equal to 0.
# # You are advised to participate in solving this problem.
# # This task helps you to become a good problem solver and helps you accepting the challenge and acquiring new skills.

#SOLUTION (NUMBER IS = 77)
print("\t\t\t\t\t\t***** GUESS THE NUMBER! *****")
username = input("Please enter your name: ")
print("Welcome", username.capitalize(), "we are glad you are here today!\n")
print("Let us introduce you to this game -\nWe have chosen a 2-digit positive integer for this game, "
      "lets say 18, 20 etc, which you have to guess.\nBut, you have to keep in mind that ONLY 9 GUESSES are allowed, else the game is over.")
print("We will keep giving you hints throughout the game to help you.\nLet's see in how many tries you finish this game!")
print("ALL THE BEST!\n")

while True:
      try1 = int(input("Enter your FIRST guess: "))
      if try1 < 0:
            print("THIS IS NOT A POSITIVE NUMBER!\nTry Again! (Guesses Left: 8)\n")
      if 0 <= try1 < 10:
            print("THIS IS NOT A 2 DIGIT NUMBER!\nTry Again! (Guesses Left: 8)\n")
      if 10 <= try1 < 70:
            print("You are FAR BEHIND the number.\nTry Again! (Guesses Left: 8)\n")
      if 70 <= try1 < 77:
            print("You are SLIGHTLY BEHIND the number.\nTry Again! (Guesses Left: 8)\n")
      if try1 == 77:
            print("\nCongratulations, you guessed the right number and finished the game in 1 guess!\nGive yourself a pat on the back!")
            break
      if 78 <= try1 < 80:
            print("You are SLIGHTLY AHEAD from the number.\nTry Again! (Guesses Left: 8)\n")
      if 80 <= try1 < 100:
            print("You are FAR AHEAD from the number.\nTry Again! (Guesses Left: 8)\n")
      if try1 >= 100:
            print("THIS IS NOT A 2 DIGIT NUMBER!\nTry Again! (Guesses Left: 8)\n")
      else:
            try1 = int(input("Enter your SECOND guess: "))
            if try1 < 0:
                  print("THIS IS NOT A POSITIVE NUMBER!\nTry Again! (Guesses Left: 7)\n")
            if 0 <= try1 < 10:
                  print("THIS IS NOT A 2 DIGIT NUMBER!\nTry Again! (Guesses Left: 7)\n")
            if 10 <= try1 < 70:
                  print("You are FAR BEHIND the number.\nTry Again! (Guesses Left: 7)\n")
            if 70 <= try1 < 77:
                  print("You are SLIGHTLY BEHIND the number.\nTry Again! (Guesses Left: 7)\n")
            if try1 == 77:
                  print("\nCongratulations, you guessed the right number and finished the game in 2 guesses!\nGive yourself a pat on the back!")
                  break
            if 78 <= try1 < 80:
                  print("You are SLIGHTLY AHEAD from the number.\nTry Again! (Guesses Left: 7)\n")
            if 80 <= try1 < 100:
                  print("You are FAR AHEAD from the number.\nTry Again! (Guesses Left: 7)\n")
            if try1 >= 100:
                  print("THIS IS NOT A 2 DIGIT NUMBER!\nTry Again! (Guesses Left: 7)\n")
            else:
                  try1 = int(input("Enter your THIRD guess: "))
                  if try1 < 0:
                        print("THIS IS NOT A POSITIVE NUMBER!\nTry Again! (Guesses Left: 6)\n")
                  if 0 <= try1 < 10:
                        print("THIS IS NOT A 2 DIGIT NUMBER!\nTry Again! (Guesses Left: 6)\n")
                  if 10 <= try1 < 70:
                        print("You are FAR BEHIND the number.\nTry Again! (Guesses Left: 6)\n")
                  if 70 <= try1 < 77:
                        print("You are SLIGHTLY BEHIND the number.\nTry Again! (Guesses Left: 6)\n")
                  if try1 == 77:
                        print("\nCongratulations, you guessed the right number and finished the game in 3 guesses!\nGive yourself a pat on the back!")
                        break
                  if 78 <= try1 < 80:
                        print("You are SLIGHTLY AHEAD from the number.\nTry Again! (Guesses Left: 6)\n")
                  if 80 <= try1 < 100:
                        print("You are FAR AHEAD from the number.\nTry Again! (Guesses Left: 6)\n")
                  if try1 >= 100:
                        print("THIS IS NOT A 2 DIGIT NUMBER!\nTry Again! (Guesses Left: 6)\n")
                  else:
                        try1 = int(input("Enter your FOURTH guess: "))
                        if try1 < 0:
                              print("THIS IS NOT A POSITIVE NUMBER!\nTry Again! (Guesses Left: 5)\n")
                        if 0 <= try1 < 10:
                              print("THIS IS NOT A 2 DIGIT NUMBER!\nTry Again! (Guesses Left: 5)\n")
                        if 10 <= try1 < 70:
                              print("You are FAR BEHIND the number.\nTry Again! (Guesses Left: 5)\n")
                        if 70 <= try1 < 77:
                              print("You are SLIGHTLY BEHIND the number.\nTry Again! (Guesses Left: 5)\n")
                        if try1 == 77:
                              print("\nCongratulations, you guessed the right number and finished the game in 4 guesses!\nGive yourself a pat on the back!")
                              break
                        if 78 <= try1 < 80:
                              print("You are SLIGHTLY AHEAD from the number.\nTry Again! (Guesses Left: 5)\n")
                        if 80 <= try1 < 100:
                              print("You are FAR AHEAD from the number.\nTry Again! (Guesses Left: 5)\n")
                        if try1 >= 100:
                              print("THIS IS NOT A 2 DIGIT NUMBER!\nTry Again! (Guesses Left: 5)\n")
                        else:
                              try1 = int(input("Enter your FIFTH guess: "))
                              if try1 < 0:
                                    print("THIS IS NOT A POSITIVE NUMBER!\nTry Again! (Guesses Left: 4)\n")
                              if 0 <= try1 < 10:
                                    print("THIS IS NOT A 2 DIGIT NUMBER!\nTry Again! (Guesses Left: 4)\n")
                              if 10 <= try1 < 70:
                                    print("You are FAR BEHIND the number.\nTry Again! (Guesses Left: 4)\n")
                              if 70 <= try1 < 77:
                                    print("You are SLIGHTLY BEHIND the number.\nTry Again! (Guesses Left: 4)\n")
                              if try1 == 77:
                                    print("\nCongratulations, you guessed the right number and finished the game in 5 guesses!\nGive yourself a pat on the back!")
                                    break
                              if 78 <= try1 < 80:
                                    print("You are SLIGHTLY AHEAD from the number.\nTry Again! (Guesses Left: 4)\n")
                              if 80 <= try1 < 100:
                                    print("You are FAR AHEAD from the number.\nTry Again! (Guesses Left: 4)\n")
                              if try1 >= 100:
                                    print("THIS IS NOT A 2 DIGIT NUMBER!\nTry Again! (Guesses Left: 4)\n")
                              else:
                                    try1 = int(input("Enter your SIXTH guess: "))
                                    if try1 < 0:
                                          print("THIS IS NOT A POSITIVE NUMBER!\nTry Again! (Guesses Left: 3)\n")
                                    if 0 <= try1 < 10:
                                          print("THIS IS NOT A 2 DIGIT NUMBER!\nTry Again! (Guesses Left: 3)\n")
                                    if 10 <= try1 < 70:
                                          print("You are FAR BEHIND the number.\nTry Again! (Guesses Left: 3)\n")
                                    if 70 <= try1 < 77:
                                          print("You are SLIGHTLY BEHIND the number.\nTry Again! (Guesses Left: 3)\n")
                                    if try1 == 77:
                                          print("\nCongratulations, you guessed the right number and finished the game in 6 guesses!\nGive yourself a pat on the back!")
                                          break
                                    if 78 <= try1 < 80:
                                          print("You are SLIGHTLY AHEAD from the number.\nTry Again! (Guesses Left: 3)\n")
                                    if 80 <= try1 < 100:
                                          print("You are FAR AHEAD from the number.\nTry Again! (Guesses Left: 3)\n")
                                    if try1 >= 100:
                                          print("THIS IS NOT A 2 DIGIT NUMBER!\nTry Again! (Guesses Left: 3)\n")
                                    else:
                                          try1 = int(input("Enter your SEVENTH guess: "))
                                          if try1 < 0:
                                                print("THIS IS NOT A POSITIVE NUMBER!\nTry Again! (Guesses Left: 2)\n")
                                          if 0 <= try1 < 10:
                                                print("THIS IS NOT A 2 DIGIT NUMBER!\nTry Again! (Guesses Left: 2)\n")
                                          if 10 <= try1 < 70:
                                                print("You are FAR BEHIND the number.\nTry Again! (Guesses Left: 2)\n")
                                          if 70 <= try1 < 77:
                                                print("You are SLIGHTLY BEHIND the number.\nTry Again! (Guesses Left: 2)\n")
                                          if try1 == 77:
                                                print("\nCongratulations, you guessed the right number and finished the game in 7 guesses!\nGive yourself a pat on the back!")
                                                break
                                          if 78 <= try1 < 80:
                                                print("You are SLIGHTLY AHEAD from the number.\nTry Again! (Guesses Left: 2)\n")
                                          if 80 <= try1 < 100:
                                                print("You are FAR AHEAD from the number.\nTry Again! (Guesses Left: 2)\n")
                                          if try1 >= 100:
                                                print("THIS IS NOT A 2 DIGIT NUMBER!\nTry Again! (Guesses Left: 2)\n")
                                          else:
                                                try1 = int(input("Enter your EIGHTH guess: "))
                                                if try1 < 0:
                                                      print("THIS IS NOT A POSITIVE NUMBER!\nTry Again! (Guesses Left: 1)\n")
                                                if 0 <= try1 < 10:
                                                      print("THIS IS NOT A 2 DIGIT NUMBER!\nTry Again! (Guesses Left: 1)\n")
                                                if 10 <= try1 < 70:
                                                      print("You are FAR BEHIND the number.\nTry Again! (Guesses Left: 1)\n")
                                                if 70 <= try1 < 77:
                                                      print("You are SLIGHTLY BEHIND the number.\nTry Again! (Guesses Left: 1)\n")
                                                if try1 == 77:
                                                      print("\nCongratulations, you guessed the right number and finished the game in 8 guesses!\nGive yourself a pat on the back!")
                                                      break
                                                if 78 <= try1 < 80:
                                                      print("You are SLIGHTLY AHEAD from the number.\nTry Again! (Guesses Left: 1)\n")
                                                if 80 <= try1 < 100:
                                                      print("You are FAR AHEAD from the number.\nTry Again! (Guesses Left: 1)\n")
                                                if try1 >= 100:
                                                      print("THIS IS NOT A 2 DIGIT NUMBER!\nTry Again! (Guesses Left: 1)\n")
                                                else:
                                                      try1 = int(input("Enter your NINTH & LAST guess: "))
                                                      if try1 < 0:
                                                            print("THIS IS NOT A POSITIVE NUMBER!\n(Guesses Left: 0)\n")
                                                            print("You couldn't find the right number in 9 guesses.\nGAME OVER!")
                                                            break
                                                      if 0 <= try1 < 10:
                                                            print("THIS IS NOT A 2 DIGIT NUMBER!\n(Guesses Left: 0)\n")
                                                            print("You couldn't find the right number in 9 guesses.\nGAME OVER!")
                                                            break
                                                      if 10 <= try1 < 70:
                                                            print("You are FAR BEHIND the number.\n(Guesses Left: 0)\n")
                                                            print("You couldn't find the right number in 9 guesses.\nGAME OVER!")
                                                            break
                                                      if 70 <= try1 < 77:
                                                            print("You are SLIGHTLY BEHIND the number.\n(Guesses Left: 0)\n")
                                                            print("You couldn't find the right number in 9 guesses.\nGAME OVER!")
                                                            break
                                                      if try1 == 77:
                                                            print("\nCongratulations, you guessed the right number and finished the game in 9 guesses!\nGive yourself a pat on the back!")
                                                            break
                                                      if 78 <= try1 < 80:
                                                            print("You are SLIGHTLY AHEAD from the number.\n(Guesses Left: 0)\n")
                                                            print("You couldn't find the right number in 9 guesses.\nGAME OVER!")
                                                            break
                                                      if 80 <= try1 < 100:
                                                            print("You are FAR AHEAD from the number.\n(Guesses Left: 0)\n")
                                                            print("You couldn't find the right number in 9 guesses.\nGAME OVER!")
                                                            break
                                                      if try1 >= 100:
                                                            print("THIS IS NOT A 2 DIGIT NUMBER!\n(Guesses Left: 0)\n")
                                                            print("You couldn't find the right number in 9 guesses.\nGAME OVER!")
                                                            break
###MY CODE ISNT WORKING FOR NUMBERS GREATER THAN OR EQUAL TO 100 (AND I CANT FIND THE ISSUE RN).

#SOLUTION FROM VIDEO:
# no of guesses 9
# print no of guesses left
# No of guesses he took to finish
# game over

# n=18
# number_of_guesses=1
# print("Number of guesses is limited to only 9 times: ")
# while (number_of_guesses<=9):
#     guess_number = int(input("Guess the number :\n"))
#     if guess_number<18:
#         print("you enter less number please input greater number.\n")
#     elif guess_number>18:
#         print("you enter greater number please input smaller number.\n ")
#     else:
#         print("you won\n")
#         print(number_of_guesses,"no.of guesses he took to finish.")
#         break
#     print(9-number_of_guesses,"no. of guesses left")
#     number_of_guesses = number_of_guesses + 1
#
# if(number_of_guesses>9):
#     print("Game Over")