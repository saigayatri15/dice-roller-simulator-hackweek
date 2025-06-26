import random
import time
import os
dice_art={
    1:(
"┌─────────┐",
"│         │",
"│    ●    │",
"│         │",
"└─────────┘"
    ),
    2:(
"┌─────────┐",
"│  ●      │",
"│         │",
"│      ●  │",
"└─────────┘"
    ),
    3:(
"┌─────────┐",
"│  ●      │",
"│    ●    │",
"│      ●  │",
"└─────────┘"
    ),
    4:(
"┌─────────┐",
"│  ●   ●  │",
"│         │",
"│  ●   ●  │",
"└─────────┘"
    ),
    5:(
"┌─────────┐",
"│  ●   ●  │",
"│    ●    │",
"│  ●   ●  │",
"└─────────┘"
    ),
    6:(
"┌─────────┐",
"│  ●   ●  │",
"│  ●   ●  │",
"│  ●   ●  │",
"└─────────┘"
    )
}


def clear_screen():
    """Clears the terminal screen based on the operating system."""
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix-based systems (Linux, macOS)
        os.system('clear')

def roll_dice():
    result=random.randint(1,6)
    clear_screen()
    for _ in range(20):
        for line in dice_art[random.randint(1,6)]:
            print(line)
        time.sleep(0.1)
        clear_screen()
    print("You have rolled:")
    for line in dice_art[result]:
        print(line)


def main():
    while True:
        play=input("Press the Enter key to roll the die: ")
        if play=="":
            roll_dice()
            break
        else:
            print("Invalid input entered. Try again.")

main()