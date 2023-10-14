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
signpost with scribbles you can barely make out as words. The sign has three branches, one pointing east
and two pointing west.\n\n""")

time.sleep(3)

while True:
    choice1 = input("Which sign would you like to read?:\n A) Sign pointing west.\n B) Sign pointing east.")
    if choice1 in ['A', 'B']:
        break

if choice1 == "A":
    print("The sign reads: \"Trader's Market\"")
else:
    print("The sign reads: \"The Blue Light Inn\"")
