import random
import threading
import time
import dolphin_memory_engine as dme
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

items = ['Patch Castle', 'Fountain Gardens', 'Flower Fields', 'Rainbow Falls', 'Big-Bean Vine ', 'Mole Hole', 'Weird Woods', 'Pyramid Sands', 'Lava Landing', 'Cool Cave', 'Dino Jungle', 'Temper Temple', 'Dusk Dunes', 'Toy Tracks', 'Mushroom Run', 'Sweets Park', 'Melody Town', 'Cocoa Station', 'Dark Manor', 'Splash Beach', 'Blub-Blub Ocean', 'Secret Island', 'Deep-Dive Deep', 'Boom Boatyard', 'Fossil Reef', 'Snowy Fields', 'Cozy Cabin', 'Mt. Slide', 'Frosty Wheel', 'Frigid Fjords', 'Evergreen Lift', 'Future City', 'Tube Town', 'Mysterious UFO', 'Stellar Way', 'Moon Base', 'Outer Rings', "Whispy's Forest", 'Tempest Towers', 'Cloud Palace', 'Castle Dedede', 'Meta Melon Isle', 'Battleship Halberd', 'Fangora', 'Hot Wings', 'Squashini', 'Capamari', 'King Dedede', 'Meta Knight', 'Yin-Yarn']
locations = ['Patch Castle Goal', 'Fountain Gardens Goal', 'Flower Fields Goal', 'Rainbow Falls Goal', 'Big-Bean Vine Goal', 'Mole Hole Goal', 'Weird Woods Goal', 'Pyramid Sands Goal', 'Lava Landing Goal', 'Cool Cave Goal', 'Dino Jungle Goal', 'Temper Temple Goal', 'Dusk Dunes Goal', 'Toy Tracks Goal', 'Mushroom Run Goal', 'Sweets Park Goal', 'Melody Town Goal', 'Cocoa Station Goal', 'Dark Manor Goal', 'Splash Beach Goal', 'Blub-Blub Ocean Goal', 'Secret Island Goal', 'Deep-Dive Deep Goal', 'Boom Boatyard Goal', 'Fossil Reef Goal', 'Snowy Fields Goal', 'Cozy Cabin Goal', 'Mt. Slide Goal', 'Frosty Wheel Goal', 'Frigid Fjords Goal', 'Evergreen Lift Goal', 'Future City Goal', 'Tube Town Goal', 'Mysterious UFO Goal', 'Stellar Way Goal', 'Moon Base Goal', 'Outer Rings Goal', "Whispy's Forest", 'Tempest Towers Goal', 'Cloud Palace Goal', 'Castle Dedede Goal', 'Meta Melon Isle Goal', 'Battleship Halberd Goal', 'Fangora Goal', 'Hot Wings Goal', 'Squashini Goal', 'Capamari Goal', 'King Dedede Goal', 'Meta Knight Goal']

unrandom_items = items[:]
unrandom_locations = locations[:]

seed = 0
firstItem = None
lastUnlockedItem = "Not Initialized"

def startRando(inputSeed=""):
    global lastUnlockedItem

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
        lastUnlockedItem = "Running setup"
        setup()
    else:
        lastUnlockedItem = "Save found on file 1\nResuming randomizer"

    # Spoiler Maker
    item_placement = dict(zip(locations, items))

    background.start()

def seedGen(setSeed=str(int(time.time()))):
    global seed
    seed = setSeed
    random.seed(setSeed)
    random.shuffle(items)
    global firstItem
    firstItem = items.pop(0)

def setup():
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

    #Unlock Map
    dme.write_byte(0x906A7007, 0x10)

    #Unlock First Level
    hops = 0
    for item in unrandom_items:
        if item == firstItem:
            dme.write_byte(0x906A7067+(hops*36), 0x02)
            global lastUnlockedItem
            lastUnlockedItem = (f'START unlocked {item}')
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

    for item in unrandom_items:
        if items[hops] == item:
            if dme.read_byte(0x906A7067+(unlock_hops*level_offset)) == 0x01:
                if item == 'Yin-Yarn':
                    level = 0x906A8F77 + (41 * 36)
                    dme.write_byte(level, 0x02)
                else:
                    dme.write_byte(0x906A7067+(unlock_hops*level_offset), 0x02)
                global lastUnlockedItem
                lastUnlockedItem = (f'{unrandom_locations[hops]} unlocked {items[hops]}')
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

def hint(levelNum):
    unlock_hops = 0
    saying = "Out of bounds error"
    levelName = unrandom_items[levelNum]
    for item in items:
        if item == levelName:
            saying = f"They say {unrandom_items[levelNum]} is unlocked by {locations[unlock_hops]}"
            break
        unlock_hops += 1
    return saying

def backgroundLoop():
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

def userGUILoop():

    def updateText():
        lastUnlockedItemtxt['text'] = lastUnlockedItem
        seedtxt['text'] = f"Seed: {seed}"
        root.after(100, updateText)

    def getHint():
        hintNum = random.randrange(1, 49)
        hinttxt['text'] = hint(hintNum)

    # Create the main application window
    root = tk.Tk()
    root.title("Kirby Epic Yarn Randomizer")
    tabControl = ttk.Notebook(root)

    main_tab = ttk.Frame(tabControl)
    warp_tab = ttk.Frame(tabControl)
    hint_tab = ttk.Frame(tabControl)
    info_tab = ttk.Frame(tabControl)

    tabControl.add(main_tab, text='Main')
    tabControl.add(warp_tab, text='Warp')
    tabControl.add(hint_tab, text='Hint')
    tabControl.add(info_tab, text='Info')
    tabControl.pack(expand=1, fill="both")

    #Main Tab
    name = ttk.Entry(main_tab)
    startrando_button = ttk.Button(main_tab, text="Start Randomizer", command=lambda: startRando(name.get()))
    lastUnlockedItemtxt = ttk.Label(main_tab, text=lastUnlockedItem)

    name.pack()
    startrando_button.pack()
    lastUnlockedItemtxt.pack()

    #Warp Tab
    warpWarp = ttk.Label(warp_tab, text="Warning: Before pressing any of these buttons exit fully to the title screen!\n"
                                        "Failer to do so WILL corrupt your save file and/or your Wii system memory!")
    warp0_button = ttk.Button(warp_tab, text="Quality Square", command=lambda: change_saved_location(0))
    warp1_button = ttk.Button(warp_tab, text="Grass Land", command=lambda: change_saved_location(1))
    warp2_button = ttk.Button(warp_tab, text="Hot Land", command=lambda: change_saved_location(2))
    warp3_button = ttk.Button(warp_tab, text="Treat Land", command=lambda: change_saved_location(3))
    warp4_button = ttk.Button(warp_tab, text="Water Land", command=lambda: change_saved_location(4))
    warp5_button = ttk.Button(warp_tab, text="Snow Land", command=lambda: change_saved_location(5))
    warp6_button = ttk.Button(warp_tab, text="Space Land", command=lambda: change_saved_location(6))
    warp7_button = ttk.Button(warp_tab, text="Dream Land", command=lambda: change_saved_location(7))

    warpWarp.grid(row=0, columnspan=3)
    warp0_button.grid(row=1, column=0)
    warp1_button.grid(row=1, column=1)
    warp2_button.grid(row=1, column=2)
    warp3_button.grid(row=1, column=3)
    warp4_button.grid(row=2, column=0)
    warp5_button.grid(row=2, column=1)
    warp6_button.grid(row=2, column=2)
    warp7_button.grid(row=2, column=3)

    #Hint Tab
    hinttxt = ttk.Label(hint_tab, text="Hint")
    getHint_button = ttk.Button(hint_tab, text="Get Hint", command=getHint)
    hinttxt.pack()
    getHint_button.pack()

    #Info Tab
    seedtxt = ttk.Label(info_tab, text=f"Seed: {seed}")
    seedtxt.pack()

    # Run the application
    updateText()
    root.mainloop()

#--------------------------------------------------------------------------

#Begin background loop and input loop
background = threading.Thread(target=backgroundLoop)
exitEvent = threading.Event()
userGUILoop()
exitEvent.set()
