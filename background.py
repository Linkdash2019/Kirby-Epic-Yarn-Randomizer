import time
import tkinter as tk
import gui
import dolphin_memory_engine as dme
import shuffle
import variableManagment as var

exitEvent = None

chestL = []

def setSelectedFile(fileNum):
    dme.write_byte(0x906A6C4F, fileNum)

def checkDoors():
    #43 Normal Levels
    #7 Bosses
    hops = 0
    offset = 0
    level_offset = 36

    while hops <= 49:
        #Check door status
        if dme.read_byte(0x906A7067+(hops*level_offset)+offset) == 3:
            #Check if door has a medal
            if dme.read_byte(0x906A7067+(hops*level_offset)+8) < 255:
                if hops == 49:
                    if var.isBeaten == False:
                        gui.lastUnlockedLog.config(state='normal')
                        gui.lastUnlockedLog.insert(tk.INSERT, f'Congratulations!\nYou have beaten Yin-Yarn!\n')
                        gui.lastUnlockedLog.config(state='disabled')
                        var.isBeaten = True
                else:
                    getItemToUnlock(var.spoiler[list(var.doorLocations.keys())[hops]], list(var.doorLocations.keys())[hops])
        hops += 1

def checkChests():
    hops = 0
    offset = 24
    level_offset = 36

    while hops <= 42:
        chest1 = False
        chest2 = False
        chest3 = False

        if dme.read_byte(0x906A7067 + (hops * level_offset) + offset) == 0:
            pass
            
        elif dme.read_byte(0x906A7067 + (hops * level_offset) + offset) == 1:
            chest1 = True

        elif dme.read_byte(0x906A7067 + (hops * level_offset) + offset) == 2:
            chest2 = True

        elif dme.read_byte(0x906A7067 + (hops * level_offset) + offset) == 3:
            chest1 = True
            chest2 = True

        elif dme.read_byte(0x906A7067 + (hops * level_offset) + offset) == 4:
            chest3 = True

        elif dme.read_byte(0x906A7067 + (hops * level_offset) + offset) == 5:
            chest1 = True
            chest3 = True

        elif dme.read_byte(0x906A7067 + (hops * level_offset) + offset) == 6:
            chest2 = True
            chest3 = True

        elif dme.read_byte(0x906A7067 + (hops * level_offset) + offset) == 7:
            chest1 = True
            chest2 = True
            chest3 = True

        if chest1:
            getItemToUnlock(
                var.spoiler[list(var.chestLocations.keys())[0+(hops*3)]], 
                list(var.chestLocations.keys())[0+(hops*3)]
            )
        if chest2:
            getItemToUnlock(
                var.spoiler[list(var.chestLocations.keys())[1+(hops*3)]],
                list(var.chestLocations.keys())[1+(hops*3)]
            )
        if chest3:
            getItemToUnlock(
                var.spoiler[list(var.chestLocations.keys())[2+(hops*3)]], 
                list(var.chestLocations.keys())[2+(hops*3)]
            )
        hops += 1

def getItemToUnlock(item, location):
    newUnlock = False
    if item in var.doorItems:
        newUnlock = unlockDoors(item)
    elif item in var.chestItems:
        newUnlock = unlockChests(item)
    if newUnlock:
        gui.lastUnlockedLog.config(state='normal')
        gui.lastUnlockedLog.insert(tk.INSERT, f'{location} unlocked {item}\n')
        gui.lastUnlockedLog.config(state='disabled')

def unlockDoors(itemToUnlock):
    level_offset = 36
    unlock_hops = 0

    for item in var.doorItems:
        if itemToUnlock == item:
            #These other doors will be redirected correcly when unlocked
            if item == 'Patch Castle':
                if var.pcUnlock==False:
                    var.pcUnlock = True
                    return True
            elif item == 'Fangora':
                if var.boss1Unlock==False:
                    var.boss1Unlock = True
                    return True
            elif item == 'Hot Wings':
                if var.boss2Unlock==False:
                    var.boss2Unlock = True
                    return True
            elif item == 'Squashini':
                if var.boss3Unlock==False:
                    var.boss3Unlock = True
                    return True
            elif item == 'Capamari':
                if var.boss4Unlock==False:
                    var.boss4Unlock = True
                    return True
            elif item == 'King Dedede':
                if var.boss5Unlock==False:
                    var.boss5Unlock = True
                    return True
            elif item == 'Meta Knight':
                if var.boss6Unlock==False:
                    var.boss6Unlock = True
                    return True
            #For Yin-Yarn give patch for dramatic effect
            elif item == 'Yin-Yarn':
                level = 0x906A9163
                if dme.read_byte(level) == 0x00:
                    dme.write_byte(level, 0x01)
                    return True

            elif dme.read_byte(0x906A7067+(unlock_hops*level_offset)) == 0x01:
                #And the normal levels will just unlock normally
                if dme.read_byte(0x906A7067+(unlock_hops*level_offset)) == 0x01:
                    dme.write_byte(0x906A7067+(unlock_hops*level_offset), 0x02)
                    return True
            return False
        unlock_hops += 1

def unlockChests(item):
    if item not in chestL:
        chestL.append(item)
        return True
    else:
        return False

def motifFix():
    #Revert 'Motifs'
    #Top row
    loopNum = 0
    while loopNum < 43:
        dme.write_byte(0x906A80EF + (loopNum * 12), 0x00)
        loopNum += 1

    # Bottom row
    loopNum = 0
    while loopNum < 43:
        dme.write_byte(0x906A80EF + (loopNum * 12) + (12 * 125), 0x00)
        loopNum += 1

    #Disks
    loopNum = 0
    while loopNum < 52:
        dme.write_byte(0x906A8AC7 + (loopNum * 12), 0x00)
        loopNum += 1

    #Apply current 'Motifs'
    for item in chestL:
        hops = 0
        tinyHops = 1
        onlyDisk = False
        for stuff in var.chestItems:
            if item == stuff:
                if tinyHops == 1 and not onlyDisk:
                    dme.write_byte(0x906A80EF + (hops * 12), 0x01)
                    break
                if tinyHops == 2 and not onlyDisk:
                    dme.write_byte(0x906A80EF + (hops * 12) + (12 * 125), 0x01)
                    break
                if tinyHops == 3 or onlyDisk:
                    diskHops = 0
                    for disk in var.diskOrder:
                        if item == disk:
                            dme.write_byte(0x906A8AC7 + (diskHops * 12), 0x01)
                            break
                        diskHops += 1   
            else:
                tinyHops += 1
                if tinyHops == 4:
                    hops+=1
                    tinyHops = 1
                    if hops >= 43:
                        onlyDisk = True

             

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
    if var.boss6Unlock: dme.write_bytes(0x906A7728, b"\x90\x6C\x46\x10")
    else: dme.write_bytes(0x906A7728, b"\x00\x00\x00\x00") 

def backgroundLoop(exitEvent):
    locationRadioButton = 'inLevel'

    while not exitEvent.is_set():
        # When world map entered
        if (dme.read_bytes(0x906A7010, 4) == b'ROOM') & (locationRadioButton == 'inLevel'):
            locationRadioButton = 'onMap'
            setSelectedFile(0x00)
            if var.shuffleDoors:
                redirectBossDoors()
                checkDoors()
            if var.shuffleChests:
                checkChests()
                motifFix()
        # When level entered
        elif (dme.read_bytes(0x906A7010, 4) != b'ROOM') & (locationRadioButton == 'onMap'):
            locationRadioButton = 'inLevel'
            setSelectedFile(0x00)
        else:
            time.sleep(1)
            if var.shuffleDoors:
                redirectBossDoors()