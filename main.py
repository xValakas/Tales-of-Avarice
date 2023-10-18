# 12/10/2023
# INDEPENDENT PROJECT
# FYR106 EXPLORE

# Imports and Initialisations
import time
import sys
import inquirer
import os
import colorama
from colorama import init, Fore, Back, Style

colorama.init()

LINE_CLEAR = '\x1b[2K'

# Setting the ASCII art

f = open('ASCII_Art.txt', 'r')
print(''.join([line for line in f]))
f.close()

p = open('ASCII_Title.txt', 'r')
print(''.join([line for line in p]))
p.close()

z = open('ASCII_Border.txt', 'r')
print(''.join([line for line in z]))
z.close()


# Print controller
# c = char, s = string
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


# Setting an empty list for inventory, so we can append to it later
inventory = []


def input_error(s):
    for c in s:
        print("Please type either 'A' or 'B' into the console.")


# input() in this context only works with Enter
input(Fore.RED + """In this text adventure, to progress through the story you must press Enter when the text is
in italics. Good luck.
To begin, please press enter.\n""")
print(Fore.RESET)

delay_print("Chapter 1: Beginning of the End.\n")

time.sleep(3)

delay_print("""The tale begins with the arrival of seven sinners on the Cursed Isles; A dark, enchanted shore fit only 
for the dauntless and the daring. Your surroundings become clearer as you awaken, though your vision is shrouded in fog
and your ears filled with the eerie whispers of the forgotten souls who perished here. You find yourself lying on an
unfamiliar beach, your clothes are ragged and dirty. A strange feeling suddenly washes over you, a premonition for 
danger.
You have no option but to move, but where will you go?\n\n""")

time.sleep(3)

input("\x1B[3mRocks fill your surroundings from all sides, making it hard to move anywhere but south.\x1B[0m \n")

delay_print("""Your movement is restricted as the heavy wet sand reaches almost to your ankles. You are surrounded by
jagged rocks and worst of all, you can barely see. In the distance, you notice faint traces of pulsating light, your
only hope in this desolate hell.\n\n""")

time.sleep(3)

input("\x1B[3mYou move towards the light, surely it is the safest option.\x1B[0m \n")

delay_print("""Slowly, you approach the light and eventually, you see a lantern in the distance hanging from a faded
signpost with scribbles you can barely make out as words. The sign has two branches, one pointing east
and one pointing west.\n\n""")

time.sleep(3)

while True:
    choice1 = input("Which sign would you like to read?:\n A) Sign pointing west.\n B) Sign pointing east.\n")
    if choice1 in ['A', 'B']:
        break

if choice1 == "A":
    print("\x1B[3mThe sign reads: \"Trader's Market\"\x1B[0m \n")
else:
    print("\x1B[3mThe sign reads: \"The Blue Light Inn\"\x1B[0m \n")


# This is where the story (and code) branches out
while True:
    choice2 = input("Where would you like to go?\n A) Trader's Market.\n B) The Blue Light Inn.\n")
    if choice2 in ['A', 'B']:
        break
    else:
        print(input_error)

# howManyChoices = 0;
# while howManyChoices<2:

if choice2 == "A":
    delay_print("""After some time of struggling against the thick fog and the wet sand, you approach the Trader's
    Market...or what's left of it. You see stalls have been set up along the path, though most have been destroyed quite
    some time ago and are barely standing.""")
    while True:
        choice3 = input("What would you like to do first?\n A) Investigate the area.\n B) Search the stalls.")
        if choice3 in ['A', 'B']:
            # howManyChoices=howManyChoices+1;
            break
        else:
            print(input_error)
    if choice3 == "A":
        delay_print("""You seem to find a small torn piece of significantly degraded paper. You notice the faint
        markings of what seems to be a map. You are currently located on an island named the 'Cursed Isles', wherever
        that may be.""")
        inventory.append('Faded map')
        input("\x1B[3mThe following items have been added to your inventory: Faded map\x1B[0m \n")
    else:
        delay_print("""You approach the stalls, and although most are heavily damaged, there seem to be various items
        lying around. You pick up a few gold coins and find a small dagger stabbed into the sand.""")
        inventory.append('10 Gold coins' + 'Dagger')
        input("\x1B[3mThe following items have been added to your inventory: 10 Gold coins, Dagger\x1B[0m \n")

elif choice2 == "B":
    print("""You make your way along the path to the Blue Light Inn and notice the sand is darker, pulling you in 
    deeper. The fog feels lighter as it appears to adopt a ghostly blue hue, for some reason it feels strange...
    Unnatural.""")
    choice4 = input("Do you wish to follow this path, or would you like to turn back?\n A) Continue.\n B) Turn back")
    if choice4 == "A":
        delay_print("You continue to follow the path to the Blue Light Inn")
    else:
        print("a")  # I want this to loop back to line 89, though unsure how to do so
else:
    print("False input.")
