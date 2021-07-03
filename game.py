def snake_room():
    print("\nThere is a snake here")
    print("Behind the snake is another door")
    print("The snake is having eggs!")
    print("What would you do?(1 or 2)")
    print("1).Take the eggs")
    print("2).Taunt the snake")

def monster_room():
    print("\nNow you entered the room of monsters!")
    print("The monster is sleeping.\nBehind the monster there is another door.What would you do?(1 or 2)")
    print("1).Go through the door silently")
    print("2).Kill the monster and show your courage!")

def treasure_room():
    print("\nYou are now in a room filled with diamonds!")
    print("And there is a door too!")
    print("What would you do?(1 or 2)")
    print("1).Take some diamonds and go through the door")
    print("2).Just go through the door")

def game_over():
    print("Game Over")
    

def lets_play_again():
    print("Do you want to play again?(y or n)")
    choice5=input(">")
    if choice5=='y':
        start()

    elif choice5=='n':
        quit()

def start():

    print ("You are standing in a dark room")
    print("\nThere is a door to your left and right. Which one would you take?(l or r) ")
    choice1=input(">")
    if choice1.lower()=='l':
        snake_room()
        choice2=input(">")
        if choice2.lower()=='1':
            print("\nYou want the eggs not the treasure!!thats why the snake killed you.Game Over!!")
            game_over()
            lets_play_again()

        elif choice2.lower()=='2':
             treasure_room()

    elif choice1.lower()=='r':
        monster_room()

        choice3=input(">")
        if choice3.lower()=='1':
            treasure_room()

        elif choice3.lower()=='2':
            print("The monster was hungry he ate you! Game over")
            game_over()
            lets_play_again()


                                
    choice4=input(">")
    if choice4.lower()=='1':
        print("Game Over")
        lets_play_again()

    elif choice4.lower()=='2':
        print("Yay!!You Win")
        lets_play_again()


start()
