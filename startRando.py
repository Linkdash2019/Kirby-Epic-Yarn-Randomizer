import random
import time
import dolphin_memory_engine as dme
from tkinter import messagebox
import variableManagment

# These are references to globals from main.py
background_thread = None

def startRando(inputSeed=""):
    dme.hook()
    if not dme.is_hooked():
        messagebox.showerror("Error", "Could not hook Dolphin.\nCheck that Kirby Epic Yarn is running and try again.")
        return

    if inputSeed == "":
        #Random Seed
        seedGen()
    else:
        #Set Seed
        seedGen(inputSeed)

    # Check if file 1 is probably empty
    if dme.read_byte(0x906A962B) == dme.read_byte(0x906A96F7) == 0x01:
        variableManagment.lastUnlockedItem = "Running setup"
        setup()
    else:
        variableManagment.lastUnlockedItem = "Save found on file 1\nResuming randomizer"

    # Spoiler Maker
    item_placement = dict(zip(variableManagment.locations, variableManagment.items))

    background_thread.start()

def seedGen(setSeed=str(int(time.time()))):
    variableManagment.seed = setSeed
    random.seed(setSeed)
    random.shuffle(variableManagment.items)
    variableManagment.firstItem = variableManagment.items.pop(0)

def setup():
    from background import change_saved_location

    #Unlock Badges
    hops = 0
    offset = 12
    while hops <= 40:
        level=0x906A8F77+(hops*offset)
        dme.write_byte(level, 0x03)
        hops+=1

    #Watch Cutscenes
    #Refer to GitHub for more info
    #
    #Cutscenes (Also known as 'Flicks')
    ### Even though we unlock every cutscene
    ### the game will always play the cutscene if
    ### you entered the level with a status of 0x02
    dme.write_byte(0x906A962B, 0x03)
    dme.write_byte(0x906A9637, 0x03)
    dme.write_byte(0x906A9643, 0x03)
    dme.write_byte(0x906A964F, 0x03)
    dme.write_byte(0x906A965B, 0x03)
    dme.write_byte(0x906A9667, 0x03)
    dme.write_byte(0x906A9673, 0x03)
    dme.write_byte(0x906A967F, 0x03)
    dme.write_byte(0x906A968B, 0x03)

    #Dialogs
    dme.write_byte(0x906A96F7, 0x03)
    dme.write_byte(0x906A973F, 0x03)
    dme.write_byte(0x906A971B, 0x03)
    dme.write_byte(0x906A96EB, 0x03)

    #Unlock Map (0x10) Unlock Magic Sock (0x14)
    dme.write_byte(0x906A7007, 0x14)

    #Unlock First Level
    hops = 0
    for item in variableManagment.unrandom_items:
        if item == variableManagment.firstItem:
            dme.write_byte(0x906A7067+(hops*36), 0x02)
            variableManagment.lastUnlockedItem = f'START unlocked {item}'
            break
        hops += 1

    #Set Kirby Location
    #Normal Levels
    if hops <= 0:
        change_saved_location(0)
    elif hops <= 6:
        change_saved_location(1)
    elif hops <= 12:
        change_saved_location(2)
    elif hops <= 18:
        change_saved_location(3)
    elif hops <= 24:
        change_saved_location(4)
    elif hops <= 30:
        change_saved_location(5)
    elif hops <= 36:
        change_saved_location(6)
    elif hops <= 42:
        change_saved_location(7)
    #Boss Levels
    elif hops <= 43:
        change_saved_location(1)
    elif hops <= 44:
        change_saved_location(2)
    elif hops <= 45:
        change_saved_location(3)
    elif hops <= 46:
        change_saved_location(4)
    elif hops <= 47:
        change_saved_location(5)
    elif hops <= 48:
        change_saved_location(6)
    elif hops <= 49:
        change_saved_location(7)