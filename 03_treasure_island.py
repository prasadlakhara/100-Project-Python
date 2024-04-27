print('''                                   ~~~~                                      
                              ~~~~     |     ~~~~                              
                          ~~~~         |         ~~~~                          
                      ~~~~             |             ~~~~                      
                  ~~~~                 |                 ~~~~                  
              ~~~~    _____        ___|___        _____    ~~~~              
          ~~~~        |~~~|        |     |        |~~~|        ~~~~          
      ~~~~            |~~~|        |     |        |~~~|            ~~~~      
  ~~~~                |~~~|        |     |        |~~~|                ~~~~  
  ____________________|~~~|________|_____|________|~~~|____________________  
 |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
 |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
 |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
 |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
 |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
 |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
 |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
 |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
 |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
 |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
 |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
 |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
''')
print("Welcome to Treasure Island.")
print("Your Mission is to find the treasure.")
chpoise1 = input('''You're at a crossroad, where do you want to go? Type "Left" or "Right".''').lower()


if chpoise1 == "left":
    #Continue in the Game
    choise2 = input('''You've come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across''').lower()
    if choise2 == "wait":
        choise3 = input('''You've arrive at the island unharmed. There is a house with 3 doors. One Red, One Yellow, and One Blue. Which colour do you choose?''').lower()
        if choise3 == "red":
            print("It's a room full of fire. GAME OVER")
        elif choise3 == "Yellow":
            print("You found the treasure! you Win!")
        elif choise3 == "Blue":
            print("You enter a room of beasts. GAME OVER")
        else:
            print("You got attacked by an angry trout. GAME OVER.")
    else:
        print("You got attacked by an angry trout. GAME OVER.")
else:
    print("You fell into a hole. GAME OVER.")