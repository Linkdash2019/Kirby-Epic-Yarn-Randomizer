import variableManagment as var
import random
import time

def shuffle(setSeed=str(int(time.time()))):
    # Settings
    var.seed = setSeed

    # Use settings
    var.seed = setSeed
    random.seed(var.seed)
    
    var.items += var.nothingItem
    var.locations = var.locations | var.startLocation
    if var.shuffleDoors:
        var.items += var.doorItems
        var.locations = var.locations | var.doorLocations
    if var.shuffleChests:
        var.items += var.chestItems
        var.locations = var.locations | var.chestLocations

    var.spoiler = dict.fromkeys(var.locations, None)

    # Shuffle
    if 'Yin-Yarn' in var.items:
        items_to_place = var.items[:]
        random.shuffle(items_to_place)

        placed_items = set()  # Items already placed

        while items_to_place:
            # Find all accessible locations
            accessible_locations = []
            for location, requirements in var.locations.items():
                if var.spoiler[location] is None:  
                    if all(req in placed_items for req in requirements):
                        accessible_locations.append(location)

       
            if not accessible_locations and 'Yin-Yarn' not in placed_items:
                #Undo last item placment
                var.spoiler[lastSuccess[0]] = None
                items_to_place.append(lastSuccess[1])
                placed_items.remove(lastSuccess[1])
                continue


            if not accessible_locations:
                #Place current item in random slot
                accessible_locations = [loc for loc, item in var.spoiler.items() if item is None]
            if not accessible_locations:
                break

            # Place a random item at a random accessible location
            location = random.choice(accessible_locations)
            item = items_to_place.pop(0)
            var.spoiler[location] = item
            placed_items.add(item)
            lastSuccess = (location, item)

    else:
        random.shuffle(var.items)
        for item in var.items:
            for location in var.locations:
                if var.spoiler[location] is None:
                    var.spoiler[location] = item
                    break # Return to item loop