import random
import tkinter as tk
from tkinter import ttk
import chestTest
import dolphin_memory_engine

import variableManagment

def hint(levelNum):
    unlock_hops = 0
    saying = "Out of bounds error"
    levelName = variableManagment.unrandom_items[levelNum]
    for item in variableManagment.items:
        if item == levelName:
            saying = f"They say {variableManagment.unrandom_items[levelNum]} is unlocked by {variableManagment.locations[unlock_hops]}"
            break
        unlock_hops += 1
    return saying

def userGUILoop(startRando, change_saved_location):
    def updateText():
        lastUnlockedItemtxt['text'] = variableManagment.lastUnlockedItem
        seedtxt['text'] = f"Seed: {variableManagment.seed}"
        root.after(100, updateText)

    def getHint():
        hintNum = random.randrange(1, 49)
        hinttxt['text'] = hint(hintNum)

    def testDebug():
        chestTest.test()

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
    lastUnlockedItemtxt = ttk.Label(main_tab, text=variableManagment.lastUnlockedItem)

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
    seedtxt = ttk.Label(info_tab, text=f"Seed: {variableManagment.seed}")
    seedtxt.pack()

    debugBtn = ttk.Button(info_tab, text="Debug", command=testDebug)
    debugBtn.pack()

    # Run the application
    updateText()
    root.mainloop()