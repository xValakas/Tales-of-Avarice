# 12/10/2023
# OSCAR SMITH: 2300371
# INDEPENDENT PROJECT
# FYR106 EXPLORE

import time
import sys

import colorama
from colorama import init, Fore, Back, Style
colorama.init()

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


delay_print(Fore.RED + "Chapter 1: Beginning of the End.\n")
print(Fore.RESET)

time.sleep(3)

delay_print("""The tale begins with the arrival of seven sinners on the Cursed Isles; A dark, enchanted shore fit only 
for the dauntless and the daring. Your surroundings become clearer as you awaken, though your vision is shrouded in fog
and your ears filled with the eerie whispers of the forgotten souls who perished here. You find yourself lying on an
unfamiliar beach, your clothes are ragged and dirty. A strange feeling suddenly washes over you, a premonition for 
danger.
You have no option but to move, but where will you go?\n\n""")

time.sleep(3)

delay_print("""\x1B[3mRocks fill your surroundings from all sides, making it hard to move anywhere but south.\x1B[0m \n
Your movement is restricted as the heavy wet sand reaches almost to your ankles. You are surrounded
by jagged rocks and worst of all, you can barely see. In the distance, you notice faint traces of 
pulsating light, your only hope in this desolate hell.\n\n""")
