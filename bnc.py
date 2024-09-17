# cli-games/bnc.py

from random import randint

# Define roles
roles = ["Bear", "Ninja", "Cowboy"]

# Generate a random role using an array
computer = roles[randint(0,2)]

# cli-games/bnc.py
player = False

while player == False:
    print("Get ready to play Bear, Ninja, Cowboy!")
    choice = input("Would you like instructions? (yes/no) >")
    if choice.lower() == 'yes':
       print("""Bear, Ninja, Cowboy is an exciting game of strategy and skill!
             Pit your wit against the computer! Choose a player: Bear, Ninja, or
             Cowboy. The computer chooses a player. Bear eats Ninja, Ninja defeats
             Cowboy and cowboy shoots bear.""".rstrip())
    else:
       pass
    # Get player input
    selected = 0
    score = 0
    while selected != 1:
        player = input("Bear, Ninja, or Cowboy? > ")
        if (player[0].upper() + player[1:]) in roles:
            selected += 1
        else:
            print("not an option")

    # Compare computer and player role

    if computer == player:
      print("DRAW!")
    elif computer == "Cowboy":
      if player == "Bear":
        print("You lose!", computer, "shoots", player)
      else: # computer is cowboy, player is ninja
        print("You win!", player, "defeats", computer)
        score += 1
    elif computer == "Bear":
      if player == "Cowboy":
        print("You win!", player, "shoots", computer)
        score += 1
      else: # computer is bear, player is ninja
        print("You lose!", computer, "eats", player)
    elif computer == "Ninja":
      if player == "Cowboy":
        print("You lose!", computer, "defeats", player)
      else: # computer is ninja, player is bear
        print("You win!", player, "eats", computer)
        score += 1

    play_again = input("Would you like to play again? (yes/no) > ")
    if play_again == 'yes':
      player = False
      computer = roles[randint(0,2)]
    else:
      break
