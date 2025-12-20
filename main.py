import random
import threading
import time
import dolphin_memory_engine as dme
import re

items = ['Patch Castle', 'Fountain Gardens', 'Flower Fields', 'Rainbow Falls', 'Big-Bean Vine ', 'Mole Hole', 'Weird Woods', 'Pyramid Sands', 'Lava Landing', 'Cool Cave', 'Dino Jungle', 'Temper Temple', 'Dusk Dunes', 'Toy Tracks', 'Mushroom Run', 'Sweets Park', 'Melody Town', 'Cocoa Station', 'Dark Manor', 'Splash Beach', 'Blub-Blub Ocean', 'Secret Island', 'Deep-Dive Deep', 'Boom Boatyard', 'Fossil Reef', 'Snowy Fields', 'Cozy Cabin', 'Mt. Slide', 'Frosty Wheel', 'Frigid Fjords', 'Evergreen Lift', 'Future City', 'Tube Town', 'Mysterious UFO', 'Stellar Way', 'Moon Base', 'Outer Rings', "Whispy's Forest", 'Tempest Towers', 'Cloud Palace', 'Castle Dedede', 'Meta Melon Isle', 'Battleship Halberd', 'Fangora', 'Hot Wings', 'Squashini', 'Capamari', 'King Dedede', 'Meta Knight', 'Yin-Yarn']
locations = ['Patch Castle Goal', 'Fountain Gardens Goal', 'Flower Fields Goal', 'Rainbow Falls Goal', 'Big-Bean Vine Goal', 'Mole Hole Goal', 'Weird Woods Goal', 'Pyramid Sands Goal', 'Lava Landing Goal', 'Cool Cave Goal', 'Dino Jungle Goal', 'Temper Temple Goal', 'Dusk Dunes Goal', 'Toy Tracks Goal', 'Mushroom Run Goal', 'Sweets Park Goal', 'Melody Town Goal', 'Cocoa Station Goal', 'Dark Manor Goal', 'Splash Beach Goal', 'Blub-Blub Ocean Goal', 'Secret Island Goal', 'Deep-Dive Deep Goal', 'Boom Boatyard Goal', 'Fossil Reef Goal', 'Snowy Fields Goal', 'Cozy Cabin Goal', 'Mt. Slide Goal', 'Frosty Wheel Goal', 'Frigid Fjords Goal', 'Evergreen Lift Goal', 'Future City Goal', 'Tube Town Goal', 'Mysterious UFO Goal', 'Stellar Way Goal', 'Moon Base Goal', 'Outer Rings Goal', "Whispy's Forest", 'Tempest Towers Goal', 'Cloud Palace Goal', 'Castle Dedede Goal', 'Meta Melon Isle Goal', 'Battleship Halberd Goal', 'Fangora Goal', 'Hot Wings Goal', 'Squashini Goal', 'Capamari Goal', 'King Dedede Goal', 'Meta Knight Goal']

unrandom_items = items[:]
unrandom_locations = locations[:]
try:
    seed = int(input('What is the seed?\nLeave blank for a random seed\nNumbers ONLY\n>>> '))
except ValueError:
    seed = int(time.time())
    print("Seed is:", seed)
random.seed(seed)
random.shuffle(items)
firstItem = items.pop(0)
item_placement = dict(zip(locations, items))

def setup():
    print("Running Setup")
    #Unlock Badges
    hops = 0
    offset = 12
    while hops <= 40:
        level=0x906A8F77+(hops*offset)
        dme.write_byte(level, 0x03)
        hops+=1

    #Watch Cutscenes
    #Refer to GitHub for more info
    #TODO Finish finding all cutscenes
    dme.write_byte(0x906A962B, 0x03)
    dme.write_byte(0x906A96F7, 0x03)
    dme.write_byte(0x906A973F, 0x03)
    dme.write_byte(0x906A971B, 0x03)
    dme.write_byte(0x906A96EB, 0x03)

    #Unlock Map
    dme.write_byte(0x906A7007, 0x10)

    #Unlock First Level
    hops = 0
    for item in unrandom_items:
        if item == firstItem:
            dme.write_byte(0x906A7067+(hops*36), 0x02)
            print("START unlocked", item, "\nLevel id is:", hops)
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
    
def check_medals(hops=0):
    offset = 8
    level_offset = 36
    return dme.read_byte(0x906A7067+(hops*level_offset)+offset)

def check_doors():
    #43 Normal Levels
    #7 Bosses
    hops = 0
    offset = 0
    level_offset = 36
    
    while hops <= 49:
        if dme.read_byte(0x906A7067+(hops*level_offset)+offset) == 3:
            unlockNextLevel(hops)
            #relockTrouble(hops+1)
        hops += 1

def change_saved_location(world=0):
    #We craft a string because it's easier.
    #The string then gets converted to bytes
    string = f'A00{world}ROOMNONE'
    dme.write_bytes(0x906A700C, string.encode('ascii'))

def unlockNextLevel(hops):
    level_offset = 36
    unlock_hops = 0

    for item in unrandom_items:
        if items[hops] == item:
            if dme.read_byte(0x906A7067+(unlock_hops*level_offset)) == 0x01:
                if item == 'Yin-Yarn':
                    level = 0x906A8F77 + (41 * 36)
                    dme.write_byte(level, 0x02)
                else:
                    dme.write_byte(0x906A7067+(unlock_hops*level_offset), 0x02)
                print(unrandom_locations[hops], "unlocked",items[hops],"\nLevel id is:", unlock_hops)
            return
        unlock_hops += 1

#TODO lock levels that shouldn't be unlocked.
def relockTrouble():
    pass

def hint(levelNum):
    unlock_hops = 0

    levelName = unrandom_items[levelNum]
    for item in items:
        if item == levelName:
            print("They say", unrandom_items[levelNum], "is unlocked by", locations[unlock_hops])
        unlock_hops += 1

def backgroundLoop():
    locationRadioButton = 'inLevel'

    while True:
        if (dme.read_bytes(0x906A7010, 4) == b'ROOM') & (locationRadioButton == 'inLevel'):
            locationRadioButton = 'onMap'
            check_doors()
        elif (dme.read_bytes(0x906A7010, 4) != b'ROOM') & (locationRadioButton == 'onMap'):
            locationRadioButton = 'inLevel'
        else:
            time.sleep(1)

        if not main.is_alive():
            dme.un_hook()
            return

def userConsoleLoop():
    while True:
        command = input('>>> ' )
        if command == 'exit':
            return

        elif command == 'warp':
            location = int(input("WARNING: Failure to follow instructions may result in a corrupt save (or worse corrupt your Wii system memory)\nPlease exit to the title screen then\nenter world number (0-6) >>> "))
            change_saved_location(location)
            print("DONE! You can now load your file again!")

        elif command == 'hint':
            try:
                hintNum = int(input('Enter level number (0-48): '))
                if hintNum > 48:
                    print("Invalid hint. Resetting to hint 0.")
                    hintNum = 0
            except ValueError:
                print('Invalid hint. Resetting to hint 0.')
                hintNum = 0
            hint(hintNum)

        else:
            print(
                "Unknown command\n"
                "Valid commands are:\n"
                "  -warp (Teleport Kirby across space)\n"
                "  -hint (Get a spoiler/hint)\n"
                "  -exit (Exits the randomizer cleanly)"
            )


#--------------------------------------------------------------------------

#Wait to allow Dolphin to launch
#time.sleep(3)
dme.hook()
print("Connected!")

#Check if file 1 is probably empty
if dme.read_byte(0x906A962B) == dme.read_byte(0x906A96F7) == 0x01:
    setup()

#Begin background loop and input loop
background = threading.Thread(target=backgroundLoop)
main = threading.Thread(target=userConsoleLoop)
main.start()
background.start()
