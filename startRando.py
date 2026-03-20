import random
import time
import dolphin_memory_engine as dme
import tkinter as tk
from tkinter import messagebox
import variableManagment as var
import shuffle
import gui

background_thread = None

def change_saved_location(world=0):
    #We craft a string because it's easier.
    #The string then gets converted to bytes
    string = f'A00{world}ROOMNONE'
    dme.write_bytes(0x906A700C, string.encode('ascii'))

def startRando(inputSeed=""):
    dme.hook()
    if not dme.is_hooked():
        tk.messagebox.showerror("Error", "Could not hook Dolphin.\nCheck that Kirby Epic Yarn is running and try again.")
        return

    if inputSeed == "":
        #Random Seed
        shuffle.shuffle()
    else:
        #Set Seed
        shuffle.shuffle(inputSeed)

    # Check if file 1 is probably empty
    if dme.read_byte(0x906A962B) == dme.read_byte(0x906A96F7) == 0x01:
        gui.lastUnlockedLog.config(state='normal')
        gui.lastUnlockedLog.insert(tk.INSERT, "Running setup...\n")
        gui.lastUnlockedLog.config(state='disabled')
        if var.shuffleDoors == True:
            setup()
        gui.lastUnlockedLog.config(state='normal')
        gui.lastUnlockedLog.insert(tk.INSERT, "Done!\n")
        gui.lastUnlockedLog.insert(tk.INSERT, "Seed is " + var.seed + "\n")
        gui.lastUnlockedLog.insert(tk.INSERT, f'Fluffs gift is {var.spoiler['Start']}\n')
        gui.lastUnlockedLog.config(state='disabled')
    else:
        gui.lastUnlockedLog.config(state='normal')
        gui.lastUnlockedLog.insert(tk.INSERT, "Save found on file 1, resuming randomizer\n")
        gui.lastUnlockedLog.config(state='disabled')

    print(var.spoiler)
    gui.startrando_button.config(state='disabled')
    for wiget in gui.options_tab.winfo_children():
        wiget.config(state='disabled')
    background_thread.start()

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

    #Unlock Map (0x10) Unlock Magic Sock (0x14)
    dme.write_byte(0x906A7007, 0x14)

    #Give every apartment an owner
    #(To unlock only Kirby's pad do x00 x82)
    dme.write_bytes(0x906A7005, b"\xFF\xFF")

    #Unlock shops
    dme.write_byte(0x906A7002, 0x01) #Show merchants
    dme.write_byte(0x906A7007, 0xFF) #Unlock "Doors"

    #Unlock First Level
    hops = 0
    for item in var.doorItems:
        if item == var.spoiler['Start']:
            if item == 'Patch Castle': var.pcUnlock = True
            elif item == 'Fangora': var.boss1Unlock = True
            elif item == 'Hot Wings': var.boss2Unlock = True
            elif item == 'Squashini': var.boss3Unlock = True
            elif item == 'Capamari': var.boss4Unlock = True
            elif item == 'King Dedede': var.boss5Unlock = True
            elif item == 'Meta Knight': var.boss6Unlock = True
            else: dme.write_byte(0x906A7067+(hops*36), 0x02)
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

    #Unlock all boss doors + patch castle
    dme.write_byte(0x906A7067 + (0 * 36), 0x03)
    dme.write_byte(0x906A7067 + (43 * 36), 0x03)
    dme.write_byte(0x906A7067 + (44 * 36), 0x03)
    dme.write_byte(0x906A7067 + (45 * 36), 0x03)
    dme.write_byte(0x906A7067 + (46 * 36), 0x03)
    dme.write_byte(0x906A7067 + (47 * 36), 0x03)
    dme.write_byte(0x906A7067 + (48 * 36), 0x03)
