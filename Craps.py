import os
import random

def roll_dice():
    diceone = random.randint(1, 6)
    dicetw0 = random.randint(1, 6)
    return diceone, dicetwo

def display_dice(diceone, dicetwo):
    dice_art = {
        1: ("+-------+\n"
            "|       |\n"
            "|   o   |\n"
            "|       |\n"
            "+-------+"),
        2: ("+-------+\n"
            "| o     |\n"
            "|       |\n"
            "|     o |\n"
            "+-------+"),
        3: ("+-------+\n"
            "| o     |\n"
            "|   o   |\n"
            "|     o |\n"
            "+-------+"),
        4: ("+-------+\n"
            "| o   o |\n"
            "|       |\n"
            "| o   o |\n"
            "+-------+"),
        5: ("+-------+\n"
            "| o   o |\n"
            "|   o   |\n"
            "| o   o |\n"
            "+-------+"),
        6: ("+-------+\n"
            "| o   o |\n"
            "| o   o |\n"
            "| o   o |\n"
            "+-------+"),
    }
    return f"{dice_art[diceone]}\n{dice_art[dicetwo]}"

def play_craps():
    point = None
    first_roll = True
    while True:
        input("Press Enter to roll the dice.")
        diceone, dicetwo = roll_dice()
        roll = diceone + dicetwo
        os.system('cls')
        print(display_dice(diceone, dicetwo))
        print(f"You rolled a {roll}")

        if first_roll:
            if roll in (7, 11):
                print("You win!")
                break
            elif roll in (2, 3, 12):
                print("Craps! You lose.")
                break
            else:
                point = roll
                print(f"Your point is {point}")
                first_roll = False
        else:
            if roll == point:
                print("You win!")
                break
            elif roll == 7:
                print("Seven out! You lose.")
                break

def main():
    print("""
                         .oooooo.                                          
                        d8P'  `Y8b                                         
oo.ooooo.  oooo    ooo 888          oooo d8b  .oooo.   oo.ooooo.   .oooo.o 
 888' `88b  `88.  .8'  888          `888""8P `P  )88b   888' `88b d88(  "8 
 888   888   `88..8'   888           888      .oP"888   888   888 `"Y88b.  
 888   888    `888'    `88b    ooo   888     d8(  888   888   888 o.  )88b 
 888bod8P'     .8'      `Y8bood8P'  d888b    `Y888""8o  888bod8P' 8""888P' 
 888       .o..P'                                       888                
o888o      `Y8P'                                       o888o             
  
                                                                           
    """)

    user = input("Hello welcome to pyCraps! What's your name? ")
    os.system('cls')

    print(f"Nice to meet you {user}! What kind of dice game would you like to play?")
    print("""
                                                                                       
                                              ,:::::::;.                                             
                                          '::::::::::::::::..                                        
                                       ,:::::::::::::::::::::::.                                     
                                   ,,::::::::::::::::::::::::::::::.                                 
                               ^::,::::::::::::::::::::::::::::::::::::                              
                           ':::::::::::::::::::::::::::::::::::::::::::::::                          
                         ::::::::::::::::::::::"@@@-(],::::::::::::::::::::,,                        
                        ,::::::::::::::::::::::$@@@@@@,:::::::::::::::::::,."                        
                       ^i`.^,::::::::::::::::::::::,:,:::::::::::::::::,`.:ll                        
                       `ii>l`'",:::::::::::::::::::::::::::::::::::,,^'^IIlll.                       
                       .iiiiiil"`^,:::::::::::::::::::::::::::::,:"`^;lIkMIll                        
                        iiiliiiiii;"",::::::::::::::::::::::::,,"";IIlO@@@+ll                        
                        iid@@@@>iii>il:,:::::::::::::::::::::,,Illlll>@@x+lll                        
                        i>!}(@@@iii>>>>>iI;;::,:::::::::::::;llllllllt@$0;ll:                        
                        >ii!c@@$iii>>>>>>>>i!lII;;:::;;;;IIllllllllllII!llll.                        
                        ;>iiiiiiiiiiii>>>>>>>>>ii!;;IIlIlB@@a;lllllll!i@@hlI.                        
                         iiiiiiiiiiiiiii>>>>>>>>>i;;llll@@@BBllllllllc@@brll                         
                         iiiiiiiiii>>>iiii>>>>>>>i""lll@@@1>lllllllll$@t0Ill.                        
                         >iiiiiiii!@ai>>ii>>>>>>>i`'IlI$@@hllllllllll@@;!lll                         
                         >iiiiiiii@@@@@>>>>>>>>>>i`'IllllIllllllllllllIdIlI:                         
                         iiiiiiiii},|@@k>>>>>>>>>i`'IllI!@@@>llllllIl@@@@lI                          
                         >>>>>iiiii<k@@>>>>>>>>>>i`'Ill_@@Wxlllllllld@*"lll                          
                        ..>>>>>>iii>>>>>>>>>>>>>>i^.Il!@@@I(llllllll@@oll;.                          
                          '<>>>>>>>>>>>>>>>>>>>>>i^.Ill>@milllllllllllll                             
                           .^>>>>>>>>>>>>>>>>>>>>i".Illlll@@Illllllll`.                              
                              .:>>>>>>>>>>@@$_>>>i".Illl@@@@Illllll                                  
                                  Ii>>>>>iW@@@@>>i".;ll@@@:mllll:.                                   
                                     l>>>>>;J@@/ii,.;ll$@@!lll.                                      
                                       .!>i>>bjiii:`IIlllllI                                         
                                          .l>>iiiiI:IlllI..                                          
                                              liii!IllI                                              
                                                                                                     
                      A) CASINO CRAPS 
                      B) DICE HEADS
                      C) GUESS THE DICE ROLL                                                                                                                                        
    """)

    choice = input("Enter your choice: ").upper()
    os.system('cls')

    if choice == 'A':
        print("Welcome to Casino Craps!")
        play_craps()
    elif choice == 'B':
        print("To be added.")
    elif choice == 'C':
        print("To be added.")
    else:
        print("To be added.")

if __name__ == "__main__":
    main()
