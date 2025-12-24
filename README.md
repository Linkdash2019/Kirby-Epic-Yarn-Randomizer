# Kirby Epic Yarn Randomizer
This is a W.I.P randomizer for Kirby Epic Yarn.
It uses a Python script with the Dolphin Memory Engine to manage memory values. 

## Running
If you want to run it in its current state you'll need to get the following moduals:
* dolphin-memory-engine

## Random info
While your here have some info (don't worry if you don't understand it):

### Randomization Ideas
 #### Checks:
  * Level Exits ✅
  * Chests
  * Minigame quests
  * Medals (x3)
  * Shop

#### Unlocks:
  * Doors ✅
  * Quilty Court Upgrade
  * Residents
  * Patches
  * Magic Sock?? (Maybe)


### Info
* Magic Yarn is not an item, its just an animation that plays when a boss is beaten. When a boss's door states is set to 0x03 the next world is unlocked.

* Patches change a worlds terrain to allow access to certain levels. These have 3 states. 1=Locked. 2=Obtained. 3=Used.

* Doors refer to a levels door. These also have 3 states. 1=Locked. 2=Unlocked. 3=Beaten.

* Medals are near doors in memory. They have 5 states. 255=No Medal. 0=Wood. 1=Bronze. 2=Silver. 3=Gold.

### Important Memory Values
#### Cutscenes:
* 0x906A962B - Patch Land (Flick)
* 0x906A96F7 - Welcome to Patchland (Dialog)
* 0x906A9637 - A Close Call (Flick)
* 0x906A973F - Meet Dom Whoole (Dialog)
* 0x906A971B - See Kirbys Pad (Dialog)
* 0x906A96EB - To Grass Land (Dialog)
* 0x906A9643 - Grumble, Grumble... (Flick)
* 0x906A964F - Sinister Designs (Flick)
* 0x906A965B - Bon Appetit! (Flick)
* 0x906A9667 - All Wrapped Up (Flick)
* 0x906A9673 - Ambushed! (Flick)
* 0x906A967F - To Dream Land! (Flick)
* 0x906A968B - Until Then! (Flick)

#### Doors:
* 0x906A7067 - Patch Castle
* 0x906A708B - Fountain Gardens
* (Doors are 36 bytes away from each other in memory)

#### Patches:
* 0x906A8f77 - Butterfly Patch
* 0x906A8F83 - Alarm Clock Patch
* (Patches are 12 bytes away from each other in memory)

#### Misc:
* 0x906A7007 - World Map unlock status
* 0x906A700C - Kirby Location
* 0x906A6C4F - Save file in use
