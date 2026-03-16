import time
import dolphin_memory_engine as dme
import variableManagment as var

exitEvent = None

def setSelectedFile(fileNum):
    dme.write_byte(0x906A6C4F, fileNum)

def check_doors():
    #43 Normal Levels
    #7 Bosses
    hops = 0
    offset = 0
    level_offset = 36

    while hops <= 49:
        #check door status
        if dme.read_byte(0x906A7067+(hops*level_offset)+offset) == 3:
            #Check if door has a medal
            if dme.read_byte(0x906A7067+(hops*level_offset)+8) < 255:
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
    hops += 1

    for item in var.doorItems:
        if var.items[hops] == item:
            #These other doors will be redirected correcly when unlocked
            if item == 'Patch Castle':
                if var.pcUnlock==False:
                    var.pcUnlock = True
                    var.lastUnlockedItem = f'{list(var.locations.keys())[hops]} unlocked {var.items[hops]}'
            elif item == 'Fangora':
                if var.boss1Unlock==False:
                    var.boss1Unlock = True
                    var.lastUnlockedItem = f'{list(var.locations.keys())[hops]} unlocked {var.items[hops]}'
            elif item == 'Hot Wings':
                if var.boss2Unlock==False:
                    var.boss2Unlock = True
                    var.lastUnlockedItem = f'{list(var.locations.keys())[hops]} unlocked {var.items[hops]}'
            elif item == 'Squashini':
                if var.boss3Unlock==False:
                    var.boss3Unlock = True
                    var.lastUnlockedItem = f'{list(var.locations.keys())[hops]} unlocked {var.items[hops]}'
            elif item == 'Capamari':
                if var.boss4Unlock==False:
                    var.boss4Unlock = True
                    var.lastUnlockedItem = f'{list(var.locations.keys())[hops]} unlocked {var.items[hops]}'
            elif item == 'King Dedede':
                if var.boss5Unlock==False:
                    var.boss5Unlock = True
                    var.lastUnlockedItem = f'{list(var.locations.keys())[hops]} unlocked {var.items[hops]}'
            elif item == 'Meta Knight':
                if var.boss6Unlock==False:
                    var.boss6Unlock = True
                    var.lastUnlockedItem = f'{list(var.locations.keys())[hops]} unlocked {var.items[hops]}'

            if dme.read_byte(0x906A7067+(unlock_hops*level_offset)) == 0x01:
                #For Yin-Yarn give patch for dramatic effect
                if item == 'Yin-Yarn':
                    level = 0x906A8F77 + (41 * 36)
                    dme.write_byte(level, 0x02)
                #And the normal levels will just unlock normally
                else:
                    dme.write_byte(0x906A7067+(unlock_hops*level_offset), 0x02)
                var.lastUnlockedItem = f'{list(var.locations.keys())[hops]} unlocked {var.items[hops]}'
            return
        unlock_hops += 1

def redirectBossDoors():
    # Patch Castle
    if var.pcUnlock: dme.write_bytes(0x906A7068, b"\x90\x6C\x3D\x10")
    else: dme.write_bytes(0x906A7068, b"\x00\x00\x00\x00") 
    # Fangora
    if var.boss1Unlock: dme.write_bytes(0x906A7674, b"\x90\x6C\x45\x20")
    else: dme.write_bytes(0x906A7674, b"\x00\x00\x00\x00") 
    # Hot Wings
    if var.boss2Unlock: dme.write_bytes(0x906A7698, b"\x90\x6C\x45\x50")
    else: dme.write_bytes(0x906A7698, b"\x00\x00\x00\x00")
    # Squashini
    if var.boss3Unlock: dme.write_bytes(0x906A76BC, b"\x90\x6C\x45\x80")
    else: dme.write_bytes(0x906A76BC, b"\x00\x00\x00\x00") 
    # Capamari
    if var.boss4Unlock: dme.write_bytes(0x906A76E0, b"\x90\x6C\x45\xB0")
    else: dme.write_bytes(0x906A76E0, b"\x00\x00\x00\x00") 
    # King Dedede
    if var.boss5Unlock: dme.write_bytes(0x906A7704, b"\x90\x6C\x45\xE0")
    else: dme.write_bytes(0x906A7704, b"\x00\x00\x00\x00") 
    # Meta Knight
    if var.boss6Unlock: dme.write_bytes(0x906A7704, b"\x90\x6C\x46\x10")
    else: dme.write_bytes(0x906A7728, b"\x00\x00\x00\x00") 
def backgroundLoop(exitEvent):
    locationRadioButton = 'inLevel'

    while not exitEvent.is_set():
        # When world map entered
        if (dme.read_bytes(0x906A7010, 4) == b'ROOM') & (locationRadioButton == 'inLevel'):
            locationRadioButton = 'onMap'
            setSelectedFile(0x00)
            redirectBossDoors()
            check_doors()
        # When level entered
        elif (dme.read_bytes(0x906A7010, 4) != b'ROOM') & (locationRadioButton == 'onMap'):
            locationRadioButton = 'inLevel'
            setSelectedFile(0x00)
        else:
            time.sleep(1)
            redirectBossDoors()
