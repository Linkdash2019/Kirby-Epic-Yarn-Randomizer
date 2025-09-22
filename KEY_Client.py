
import asyncio

import dolphin_memory_engine as dme

def setup():
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


def badge_unlock():
    hops = 0
    offset = 12
    while hops <= 40:
        level=0x906A8F77+(hops*12)
        dme.write_byte(level, 0x03)
        hops+=1

def inbox():
    pass #Add code to check recieved checks

def check_medals():
    hops = 0
    offset = 8
    while hops <= 43:
        level=0x906A7067+offset+(hops*0x24)
        print(dme.read_byte(level))
        hops+=1

def check_doors():
    hops = 0
    while hops <= 43:
        level=0x906A7067+(hops*0x24)
        print(dme.read_byte(level))
        hops+=1

def check_chests():
    hops = 0
    offset = 24
    while hops <= 43:
        level=0x906A7067+offset+(hops*0x24)
        print(dme.read_byte(level))
        hops+=1
        
dme.hook()

badge_unlock()
dme.un_hook()
