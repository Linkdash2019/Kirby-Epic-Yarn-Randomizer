import variableManagment as var
import random

# Settings
setSeed="1234"
shuffleDoors = False
shuffleChests = True

# Use settings
var.seed = setSeed
random.seed(var.seed)

var.items += var.nothingItem
var.locations = var.locations | var.startLocation
if shuffleDoors:
    var.items += var.doorItems
    var.locations = var.locations | var.doorLocations
if shuffleChests:
    var.items += var.chestItems
    var.locations = var.locations | var.chestLocations

# Shuffle
random.shuffle(var.items)

# Output
for key, value in (dict(zip(var.locations, var.items)).items()):
    print(f"{key}: {value}")