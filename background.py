import time
import dolphin_memory_engine as dme
import variableManagment

# These are references to globals from main.py
exitEvent = None

def setSelectedFile(fileNum):
    dme.write_byte(0x906A6C4F, fileNum)

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

    for item in variableManagment.unrandom_items:
        if variableManagment.items[hops] == item:
            if dme.read_byte(0x906A7067+(unlock_hops*level_offset)) == 0x01:
                if item == 'Yin-Yarn':
                    level = 0x906A8F77 + (41 * 36)
                    dme.write_byte(level, 0x02)
                else:
                    dme.write_byte(0x906A7067+(unlock_hops*level_offset), 0x02)
                variableManagment.lastUnlockedItem = f'{variableManagment.unrandom_locations[hops]} unlocked {variableManagment.items[hops]}'
            return
        unlock_hops += 1

def relockTrouble():
    hops = 1
    if dme.read_byte(0x906A7067+(hops*36)) == 0x02:
        dme.write_byte(0x906A7067+(hops*36), 0x01)
    hops = 7
    if dme.read_byte(0x906A7067 + (hops * 36)) == 0x02:
        dme.write_byte(0x906A7067 + (hops * 36), 0x01)
    hops = 13
    if dme.read_byte(0x906A7067 + (hops * 36)) == 0x02:
        dme.write_byte(0x906A7067 + (hops * 36), 0x01)
    hops = 19
    if dme.read_byte(0x906A7067 + (hops * 36)) == 0x02:
        dme.write_byte(0x906A7067 + (hops * 36), 0x01)
    hops = 25
    if dme.read_byte(0x906A7067 + (hops * 36)) == 0x02:
        dme.write_byte(0x906A7067 + (hops * 36), 0x01)
    hops = 31
    if dme.read_byte(0x906A7067 + (hops * 36)) == 0x02:
        dme.write_byte(0x906A7067 + (hops * 36), 0x01)
    hops = 37
    if dme.read_byte(0x906A7067 + (hops * 36)) == 0x02:
        dme.write_byte(0x906A7067 + (hops * 36), 0x01)

def backgroundLoop(exitEvent):
    locationRadioButton = 'inLevel'

    while not exitEvent.is_set():
        if (dme.read_bytes(0x906A7010, 4) == b'ROOM') & (locationRadioButton == 'inLevel'):
            locationRadioButton = 'onMap'
            setSelectedFile(0x00)
            relockTrouble()
            check_doors()
        elif (dme.read_bytes(0x906A7010, 4) != b'ROOM') & (locationRadioButton == 'onMap'):
            locationRadioButton = 'inLevel'
            setSelectedFile(0x00)
        else:
            time.sleep(1)