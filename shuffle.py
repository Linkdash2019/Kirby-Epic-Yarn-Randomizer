import variableManagment as var
import random
import time

def shuffle(setSeed=str(int(time.time()))):
    # Settings
    var.seed = setSeed

    # Use settings
    var.seed = setSeed
    random.seed(var.seed)

    
    var.locations = var.locations | var.startLocation
    if var.shuffleDoors:
        var.items += var.doorItems
        var.locations = var.locations | var.doorLocations
    if var.shuffleChests:
        var.items += var.chestItems
        var.locations = var.locations | var.chestLocations
    var.items += var.nothingItem

    var.unrandom_items = var.items[:]

    # Shuffle
    random.shuffle(var.items)

    #Finish
    var.spoiler = dict(zip(var.locations, var.items))