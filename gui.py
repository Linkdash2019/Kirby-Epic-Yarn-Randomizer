import random
import tkinter as tk
from tkinter import ttk
import tkinter.scrolledtext as st
import dolphin_memory_engine

import variableManagment as var

options_tab = None
lastUnlockedLog = None
startrando_button = None


def hint():
    choice = random.choice(list(var.spoiler.keys()))
    return f"{choice} unlocks {var.spoiler[choice]}"

def userGUILoop(startRando):
    def updateText():
        seedtxt['text'] = f"Seed: {var.seed}"
        root.after(100, updateText)

    def getHint():
        hintNum = random.randrange(1, 49)
        hinttxt['text'] = hint()

    def testDebug():
        pass

    # Create the main window
    root = tk.Tk()
    root.title("Kirby Epic Yarn Randomizer")
    root.geometry("500x240")
    root.resizable(False,False)
    tabControl = ttk.Notebook(root)

    global options_tab
    main_tab = ttk.Frame(tabControl)
    options_tab = ttk.Frame(tabControl)
    hint_tab = ttk.Frame(tabControl)
    info_tab = ttk.Frame(tabControl)
    tabControl.add(main_tab, text='Main')
    tabControl.add(options_tab, text='Options')
    tabControl.add(hint_tab, text='Hint')
    tabControl.add(info_tab, text='Info')
    tabControl.pack(expand=1, fill="both")

    #Main Tab
    global startrando_button
    global lastUnlockedLog 
    name = ttk.Entry(main_tab)
    startrando_button = ttk.Button(main_tab, text="Start Randomizer", command=lambda: startRando(name.get()))
    
    lastUnlockedLog = st.ScrolledText(main_tab, width=56, height=9)

    lastUnlockedLog.config(state='disabled')

    name.pack()
    startrando_button.pack()
    lastUnlockedLog.pack()

    #Options Tab
    shuffleDoors_var = tk.BooleanVar(value=var.shuffleDoors)
    shuffleChests_var = tk.BooleanVar(value=var.shuffleChests)
    
    optionstxt = ttk.Label(options_tab, text="Options")
    shuffleDoorCheck = ttk.Checkbutton(options_tab, text="Shuffle Doors", variable=shuffleDoors_var, command=lambda: setattr(var, 'shuffleDoors', shuffleDoors_var.get()))
    shuffleChestCheck = ttk.Checkbutton(options_tab, text="Shuffle Chests", variable=shuffleChests_var, command=lambda: setattr(var, 'shuffleChests', shuffleChests_var.get()))

    optionstxt.pack()
    shuffleDoorCheck.pack()
    shuffleChestCheck.pack()

    #Hint Tab
    hinttxt = ttk.Label(hint_tab, text="Hint")
    getHint_button = ttk.Button(hint_tab, text="Get Hint", command=getHint)
    hinttxt.pack()
    getHint_button.pack()

    #Info Tab
    seedtxt = ttk.Label(info_tab, text=f"Seed: {var.seed}")
    seedtxt.pack()

   # debugBtn = ttk.Button(info_tab, text="Debug", command=testDebug)
   # debugBtn.pack()

    # Run the application
    updateText()
    root.mainloop()