import random
#import asyncio
#from aioconsole import ainput
import dolphin_memory_engine as dme

items = ['Fountain Gardens', 'Flower Fields', 'Rainbow Falls', 'Big-Bean Vine ', 'Mole Hole', 'Weird Woods', 'Fangora']
locations = ['Patch Castle Goal', 'Fountain Gardens Goal', 'Flower Fields Goal', 'Rainbow Falls Goal', 'Big-Bean Vine Goal', 'Mole Hole Goal', 'Weird Woods Goal']

unrandom_items = items[:]
unrandom_locations = locations[:]

seed = int(input('What is the seed? >>> '))

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

    #Cutscenes
    dme.write_byte(0x906A962B, 0x03)
    dme.write_byte(0x906A96F7, 0x03)
    dme.write_byte(0x906A973F, 0x03)
    dme.write_byte(0x906A971B, 0x03)
    dme.write_byte(0x906A96EB, 0x03)

    #Unlock Map
    dme.write_byte(0x906A7007, 0x10)

    #Unlock Patch Castle
    dme.write_byte(0x906A7067, 0x02)

