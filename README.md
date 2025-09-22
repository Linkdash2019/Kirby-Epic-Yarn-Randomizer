# Kirby Epic Yarn Randomizer
This is a W.I.P randomizer for Kirby Epic Yarn.
It uses a Python script with the Dolphin Memory Engine to manage memory values. 

## Running
If you want to run it in its current state you'll need to get the following moduals:
* dolphin-memory-engine
* asyncio

## Random info
While your here have some info (don't worry if you don't understand it):

### Randomization Ideas
 #### Checks:
  * Level Exits
  * Chests
  * Minigame quests
  * Medals (x3)
  * Shop

#### Unlocks:
  * Doors
  * Quilty Court Upgrade
  * Residents
  * Patches


### Info
* Magic Yarn is not an item, its just an animation that plays when a boss is beaten. When a boss's door states is set to 0x03 the next world is unlocked.

* Patches change a worlds terrain to allow access to certain levels.

* Doors refer to a levels door. These have 3 states. 1=Locked. 2=Unlocked. 3=Beaten

* Medals are near doors in memory. They have 4 states 0=No Medal. 1=Bronze. 2=Silver. 3=Gold


### Important Memory Values
#### Cutscenes:
* 0x906A962B - Unknown
* 0x906A96F7 - Unknown
* 0x906A973F - Unknown
* 0x906A971B - Unknown
* 0x906A96EB - Unknown

#### Doors:
* 0x906A7067 - Patch Castle

#### Misc:
* 0x906A7007 - World Map Unlocked
