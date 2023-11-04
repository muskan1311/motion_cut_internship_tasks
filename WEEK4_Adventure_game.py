print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print('''
      Welcome to Treasure Island. 
      Your mission is to find the treasure.
      ''')


cross_road= input('You\'re at a crossroad. Where do you want to go? Type "left" or "right"\n')
up_cross_road= cross_road.lower()
if up_cross_road == "left":
  wait = input('''You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n
                   ___ __ 
   (_  ( . ) )__                  '.    \   :   /    .'
     '(___(_____)      __           '.   \  :  /   .'
                     /. _\            '.  \ : /  .'
                .--.|/_/__      -----____   _  _____-----
_______________''.--o/___  \_______________(_)___________
       ~        /.'o|_o  '.|  ~                   ~   ~
  ~            |/    |_|  ~'         ~
               '  ~  |_|        ~       ~     ~     ~
      ~    ~          |_|O  ~                       ~
             ~     ___|_||_____     ~       ~    ~
   ~    ~      .'':. .|_|A:. ..::''.
             /:.  .:::|_|.\ .:.  :.:\   ~
  ~         :..:. .:. .::..:  .:  ..:.       ~   ~    ~
             \.: .:  :. .: ..:: .lcf/
    ~      ~      ~    ~    ~         ~
               ~           ~    ~   ~             ~
        ~         ~            ~   ~                 ~
   ~                  ~    ~ ~                 ~

what do you think? ''')
  up_wait = wait.lower()
  if up_wait == "wait":
    door = input('''
  You arrive at the island unharmed. 
  There is a house with 3 doors. One red, one yellow and one blue. 
  Which colour do you choose?\n''')
    up_door = door.lower()
    if up_door == "yellow":
      room = input('''
    
Looks like you have come across a room
                   
                _      ()              ()      _
               / \     ||______________||     / \
              /___\    |                |    /___\
                |      |      ~@@~      |      |
               (_)     |_______  _______|     (_)
            ___/_\___  {_______}{_______}  ___/_\___
             |__~__|   %%%%%%%%%%%%%%%%%%   |__~__|
          ___|_____|__%%%%%%%%%%%%%%%%%%%%__|_____|___
             |     | %%%%%%%%%%%%%%%%%%%%%% |     |
              `=====%%%%%%%%%%%%%%%%%%%%%%%%=====`
             `=====%%%%%%%%%%%%%%%%%%%%%%%%%%=====`
            `=====%%%%%%%%%%%%%%%%%%%%%%%%%%%%=====`
           `=====/||||||||||||||||||||||||||||\=====`
          `======||||||||||||||||||||||||||||||======`
          `=======|||||||||||||||||||||||||||lc|=======`
         `==============================================`
        `================================================`
       `==================================================`
     `====================================================`
  You must be tired. Do you want to take rest or want to find clue to treasure?
  rest or clue????''')
      room_lower = room.lower()
      if room_lower == 'clue':
        book = input(
          ''' 
  You start hearing steps. You need to take a fast decision. 
  You can see on bed a suitcase lying and on side table a book is lying.
  Hurry make your decision fast book or suitcase!!!!.
  You can get caught.!!!!! ''')
        book_lower = book.lower()
        if book_lower == 'book':
          map = input('''
 
  Congrats you find yourself the treasure map.
  There is map inside this book. Great choice!!
  lets read the map now.
  ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/

  According to the map. 
  You are at the outskirts somewhere and in order to reach to your treasure
  You have to cross mountains first

  To reach mountains. You can take your boat or you can swim to the mountain
  choose either your boat or swim.
  All upto you. You are close make a right choice.  ''')
          map_lower = map.lower()
          if map_lower == "swim":
            jungle = input(
              '''
  You have reached near mountains. 
  You prefer climbing? or you want to go through the jungle?
  climb or jungle? ''')
            jungle_lower = jungle.lower()
            if jungle_lower == 'jungle':
               walk = input('''
  You want to get out of this jungle as soon as possible.
  You saw a bike near a tree. 
                            /'=----=           ______
            ((    ||          "--.__."
             "  @>||_____________//
          _______ /^\"""""""""""//\========)
         _--"""--/-. "\        // _\-:::-/_-.
       ." .-"""-/ "_\  "\  == // ;::\:::/::".\
      ; /     _/ "  \\   "\-+//--..._\_/:::::\\
      . ;    o    . ||   ( ()/)======(o)::::::.
      . \         ; .|    -|.;____...."b:::::;
       . -._  _ -  ;       ==    :::::::::::;
        "-..____.'     ls         ":::::::'

  Do you want to use bike or walk?
  choose wisely!! ''')
               walk_lower = walk.lower()
               if walk_lower == "walk":
                 west = input('''
Patience is the key indeed and you have that.
This jungle is so confusing. 
You are standing in middle of jungle with two ways.
Choose east or west??? ''')
                 west_lower = west.lower()
                 if west_lower =='west':
                   print('''
After choosing west. You went straight out of jungle.
You saw a Big cross as in your map.
You did some digging there
                         
            And you finally found your treasure!!!!!!                     
                
           CONGRATULATIONS YOU FINALLY WON!!!!!!!! ''')
                   
                 else:
                   print('''
I am sorry you were so close. Best of luck for next time.
                GAME OVER
''')

                 
               else:
                 print("Due to heavy rain. You can't. GAME OVER")
            else:
              print('''
  Its raining heavily. You can't climb today
            GAME OVER''') 

            
          else:
            print("Sorry the boat dont go there. Bad move. GAME OVER")
        else:
          print('''
  Congrats this suitcase has lots of money
  but not a tiny bit close to the treasure you just have lost.
   
                  GAME OVER''')
      else:
        print("Keep Sleeping! Your game is OVER")
      
    elif up_door == "red":
      print("GAME OVER")
    elif up_door == "blue":
      print("GAME OVER")
    else:
      print("GAME OVER due to invalid input.")
  else:
    print("Attacked by Trout. GAME OVER")
else:
  print("Fall into the hole. GAME OVER")