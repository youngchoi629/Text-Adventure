import time

user_name = input("Enter your name: ")
Age = input("\nEnter your age: ")
if(Age <= "10"):
    print("\nYou are not old enough to play this game.")
    quit()
else:
    print("\nWelcome to the game.")

time.sleep(1)
print("\n.\n.\n.\n")
print("Our protagonist", user_name, "wakes up in a room that is barely lit by a few candles.\n")
print("Ahead lies a blueprint of a robot, a map, and instructions")
print("In the map, there are 4 main rooms, and there are 2 of the 4 rooms have 2 more rooms branching out from them.\n")
print("You turn your head the to instructions, and starts reading.")
print("You only get one life, and try to do Blue tells you. Best of luck.")

while True:
    print("You look around, and sees four doors - north, south, east, west\")
   
    print("You enter north door")
    time.sleep(1)
    print("Followed by a creak, the door slowly opens. The floor of the room is scattered with all sorts of robot parts.\n")
    print("However, before you reach down to pick them up, a hologram appears.\n")
    print("The hologram says, 'Welcome. My name is Blue. Your objective is to bring me a red rose, and you can take the parts.'\n")
    north_choice_1 = input("You 1)ignore the hologram or 2)does what the hologram says\n")
        
    if(north_choice_1 == "1"):
          print("You ignore the hologram, and pick up one of the robot parts.")
          print("Instantly, the room's lights go off and all the doors lock.")
          print("Followed by a loud dragging sound, the room gets smaller and smaller.")
          time.sleep(1)
          print("\n.\n.\n.\n")
          print("Tis was the tale of", user_name, "the great.")
          quit()
          break

    elif(north_choice_1 == "2"):
        print("You decide to do what Blue says.")
        print(user_name, "asks Blue, where can I find this rose?'\n")
        time.sleep(1)
        print("Blue responds, 'It will be in one of the two doors. Good luck!'and disappears into the midst.\n")
        while True:
            north_choice_2 = input("You decide to enter the 1)right door or 2)left door\n")
            if(north_choice_2 == "1"):
                print("You enter the right door, and there is another room.\n")
                print("There is a beautiful red rose in the middle of the room, and it is surrounded by shattered glass.\n")
                print("You are barefoot, and walking over the glass is not an option.\n")
                while True:
                    north_choice_2_a = input("You 1)attempt to reach the rose or 2)try the other door.\n")
                    if(north_choice_2_a == "1"):
                    print("You take off your shirt and pants, and put them over the glass.\n")
                    print("Carefully, step by step, you walk over the glass.\n")
                    print("Some small pieces of glass pierce your foot, but you carry on.\n")
                    print("Finally, you reach the rose.\n")
                    print("You make your way back, and puts on your shirt and pants back on.\n")
                    break
                        
                    elif(north_choice_2_a == "2"):
                        print("You carefully open the other door, and the floor of the room is filled with red roses.\n")
                        print("The timer starts ticking down, and you have to find the real rose.")
                        print("You search the floor thourougly, and some few hours later, it comes down to the last two roses. You only have 10 seconds left.\n")
                        rose_choice = input("You choose the 1)right or 2)left rose.")
                        if(rose_choice == "1"):
                            print("The right one was the real rose. You make a dash for the exit and makes it out.")
                        elif(rose_choice == "2"):
                            print("THe left one was the fake rose. The ground suddenly opens, and you fall into the darkness.")
                            time.wait(1)
                            print("Tis was the tale of", user_name, "the great.")
                            quit()
                            break
                        
                    else:
                        print("Enter a valid number.\n")
                        continue
            elif(north_choice_2 == "2"):
                print("You carefully open the left door, and the floor of the room is filled with red roses.\n")
                print("You reach down to pick up one, but you cannot grab it.\n")
                print("It turns out to be just a very detailed painting.\n")
                print("You search the floor thourougly, and some few hours later, you find the actual rose.\ni")
                break
                    
            else:
                print("Enter a valid number.")
                continue

            print("You succeed in retreiving the rose. The hollogram re-appears, and says you are free to take the parts.")
            print("You haul the parts to the larger room, and goes into the next room.")
            print("This time, there a single toolbox in the room.")
            print("You open the toolbox, and there are three types of tools - a wrench, a hammer, and a drill.")
            print("Another hologram appears, and says, 'You can only take one tool out of the three. Choose wisely.'\n")
            tool_choice = input("You grab the 1)wrench or 2)hammer or 3)drill.")
            print("In the distance, you hear a sinister roar.")
            print("A few seconds later a huge troll shows itself from the dark corridor, limping towards you.")
            if(tool_choice == "wrench"):
                print("You use the wrench to smack the troll's legs, but it doesn't budge. Instead, the troll grabs you and throws you into his mouth.")
                print("Tis was the tale of", user_name, "the great.")
                quit()
            elif(tool_choice == "hammer"):
                print("You smack the troll hard in the knees. The troll falls to the ground, screeching in pain.\n")
                print("With several blows to the head, the brain oozes out and the troll cease to move.\n")
                print("The hologram says, 'Good job! Now take all three tools and proceed to the next room.\n")
                break
            time.wait(1)
            print("You put the tools next to the robot parts, and head to the east room.")
            print("You open the door, but there is nothing. However, there are two more doors in the room - just like the north room.")
            print("The hollowgram shows up once again. It says 'this time, you can earn what you need regardless of the room you choose - if you survive.'")
            print("If you go into the right room, you will have a feast. If you go into the left room, you will be faced a hardship. Choose wisely!'")
            east_choice = input("You decide to choose the 1)right room or the 2)left room")
            if(east_choice == "1"):
                print("You walk into the feast room. There is graceful classical music playing, and ahead lies plates and plates of delicous looking food.")
                print("You sit down, and drags the cake closer to you.")
                print("As soon as you touch the cake, the timer starts ticking.")
                print("The hollowgram says, 'You can only get what you need if you can eat all the food in 90 minutes.'")
                print(user_name, "starts to eat. The cake is delicious, but he already starts to feel full.")
                print("30 minutes, 40 minutes, 50 minutes, 60 minutes pass. There are still 3 plates of food, but you are too full.")
                print("Finally, the timer hits zero.")
                print("The door locks with a loud click, even before you try to escape. The floor starts to move, and you fall into the darkness.")
                print("Tis was the tale of", user_name, "the great.")
                quit()
            elif(east_choice == "2"):
                print("You open the door, and you are immediately confronted by a menacing steel door. Far away, you see the exit, but there is lava all around you.")
                print("Blue says, 'You just need to reach the exit, but without dying, of course.")
                print("You take a deep breath, and starts to walk towards the exit, jumping over the pools of lava.")
                print("A piece of lava flings up and burns your foot. It is very painful, but you trudge along.")
                print("The exit comes closer and closer. FInally, you walk out of hell and lies down in exhaustion. Your body is soaked in sweat, and your foot still hurts.")
                print("Blue says, 'Congratulations! Now the blueprint of the robot is all yours!'")
                print("You grab the blueprint and put them next to the parts and the tools.")
            else:
                
                
            
            
                
                    
                        
            print("")
