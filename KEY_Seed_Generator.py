import random
#import asyncio
#from aioconsole import ainput
import dolphin_memory_engine as dme
import re

items = ['Fountain Gardens', 'Flower Fields', 'Rainbow Falls', 'Big-Bean Vine ', 'Mole Hole', 'Weird Woods', 'Pyramid Sands', 'Lava Landing', 'Cool Cave', 'Dino Jungle', 'Temper Temple', 'Dusk Dunes', 'Toy Tracks', 'Mushroom Run', 'Sweets Park', 'Melody Town', 'Cocoa Station', 'Dark Manor', 'Splash Beach', 'Blub-Blub Ocean', 'Secret Island', 'Deep-Dive Deep', 'Boom Boatyard', 'Fossil Reef', 'Snowy Fields', 'Cozy Cabin', 'Mt. Slide', 'Frosty Wheel', 'Frigid Fjords', 'Evergreen Lift', 'Future City', 'Tube Town', 'Mysterious UFO', 'Stellar Way', 'Moon Base', 'Outer Rings', "Whispy's Forest", 'Tempest Towers', 'Cloud Palace', 'Castle Dedede', 'Meta Melon Isle', 'Battleship Halberd', 'Fangora', 'Hot Wings', 'Squashini', 'Capamari', 'King Dedede', 'Meta Knight', 'Yin-Yarn']
locations = ['Patch Castle Goal', 'Fountain Gardens Goal', 'Flower Fields Goal', 'Rainbow Falls Goal', 'Big-Bean Vine Goal', 'Mole Hole Goal', 'Weird Woods Goal', 'Pyramid Sands Goal', 'Lava Landing Goal', 'Cool Cave Goal', 'Dino Jungle Goal', 'Temper Temple Goal', 'Dusk Dunes Goal', 'Toy Tracks Goal', 'Mushroom Run Goal', 'Sweets Park Goal', 'Melody Town Goal', 'Cocoa Station Goal', 'Dark Manor Goal', 'Splash Beach Goal', 'Blub-Blub Ocean Goal', 'Secret Island Goal', 'Deep-Dive Deep Goal', 'Boom Boatyard Goal', 'Fossil Reef Goal', 'Snowy Fields Goal', 'Cozy Cabin Goal', 'Mt. Slide Goal', 'Frosty Wheel Goal', 'Frigid Fjords Goal', 'Evergreen Lift Goal', 'Future City Goal', 'Tube Town Goal', 'Mysterious UFO Goal', 'Stellar Way Goal', 'Moon Base Goal', 'Outer Rings Goal', "Whispy's Forest", 'Tempest Towers Goal', 'Cloud Palace Goal', 'Castle Dedede Goal', 'Meta Melon Isle Goal', 'Battleship Halberd Goal', 'Fangora Goal', 'Hot Wings Goal', 'Squashini Goal', 'Capamari Goal', 'King Dedede Goal', 'Meta Knight Goal']

unrandom_items = items[:]
unrandom_locations = locations[:]

#seed = input('What is the seed? >>> ')
seed = 123
#seed = "".join(re.findall(r'\d', seed))
random.seed(seed)
random.shuffle(items)
item_placement = dict(zip(locations, items))
print(item_placement)

def setup():
    print("Running Setup")
    #Unlock Badges
    hops = 0
    offset = 12
    while hops <= 5:
        level=0x906A8F77+(hops*12)
        dme.write_byte(level, 0x03)
        hops+=1

    #Cutscenes Refer to Github for more info
    dme.write_byte(0x906A962B, 0x03)
    dme.write_byte(0x906A96F7, 0x03)
    dme.write_byte(0x906A973F, 0x03)
    dme.write_byte(0x906A971B, 0x03)
    dme.write_byte(0x906A96EB, 0x03)

    #Unlock Map
    dme.write_byte(0x906A7007, 0x10)

    #Unlock Patch Castle
    dme.write_byte(0x906A7067, 0x02)

    #Set Kirby Location
    #Can be any value between 0-7
    change_saved_location(0)
    
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
        print("Hops:",hops,"Door:",dme.read_byte(0x906A7067+(hops*level_offset)+offset), "Badge:", check_medals(hops))
        if dme.read_byte(0x906A7067+(hops*level_offset)+offset) == 3:
            unlockNextLevel(hops)
        hops += 1

def change_saved_location(world=0):
    #We craft a string because its easier.
    #The string then gets converted to bytes
    string = f'A00{world}ROOMNONE'
    dme.write_bytes(0x906A700C, string.encode('ascii'))

def castle_portal(levelNum):
    #UNSTABLE AND/OR BROKEN!!
    #Change Patch castle level header to "Rainbow Falls"
    dme.write_bytes(0x906A7068, b'/x90/x6C/x3D/xA0')

def unlockNextLevel(hops):
    level_offset = 36
    unlock_hops = 0

    
    for item in unrandom_items:
        unlock_hops += 1
        if items[hops] == item:
            if dme.read_byte(0x906A7067+(unlock_hops*level_offset)) == 0x01:
                dme.write_byte(0x906A7067+(unlock_hops*level_offset), 0x02)
                print(unrandom_locations[hops], "unlocked",items[hops])
            return

#--------------------------------------------------------------------------

dme.hook()

while True:
    usrinput = input(">>> ")
    if usrinput == "setup":
        setup()
    elif usrinput == "stop":
        break
    else:
        check_doors()
        
dme.un_hook()
