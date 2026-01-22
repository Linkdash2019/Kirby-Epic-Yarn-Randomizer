import variableManagment
import random
import dolphin_memory_engine as dme

isSetup = 0

topRow = [
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0
]
bottomRow = [
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0
]

chestItems = [
    #Top Row
    #Quilty Square
    "Chandelier",
    #Grass Land
    "Flower Sofa", "Flower Clock", "Rainbow Arch",
    "Lattice", "Carrot Dresser", "Telescope",
    #Hot Land
    "Camel Sofa", "Stone Lamp", "Crystal",
    "Bronto Slide", "Pyramid", "Magic Carpet",
    #Treat Land
    "Stuffed Bear", "Mushroom Bed", "Donut Pillow",
    "Toy Piano", "Choco Ottoman", "Ghost-in-a-Box",
    #Water Land
    "Sun Clock", "Jellyfish Light", "Treasure Rug",
    "Dangler Light", "Pirate Ship", "Anemone Sofa",
    #Snow Land
    "Big Bear Bed", "Fireplace", "Knit-Cap Sofa",
    "Snow Clock", "Penguin Chest", "Holiday Tree",
    #Space Land
    "Space Monitor", "Digital Clock", "Communicator",
    "Robot Bed", "Cosmic Bin", "Saturn Stand",
    #Dream Land
    "Whispy Woods", "Bookcase", "Cloud Rug",
    "Castle Dedede", "Palm Chair", "Galaxia Sword"
    
    #Bottom Row
    #Quilty Square
    "King's Throne",
    #Grass Land
    "Fountain", "Frog Umbrella Stand", "Outdoor Bath",
    "Cloud Pillow", "Tree-Stump Bed", "Log Cake",
    #Hot Land
    "Cactus Juice", "Cartoon Meat", "Frog Mirror",
    "Torch", "Camel Pillow", "Hourglass",
    #Treat Land
    "Tin Robot", "Mushroom Lamp", "Dessert Dresser",
    "Clef Tree", "Chocolate Bar", "Pumpkin",
    #Water Land
    "Moon Clock", "Aquarium", "Totem Pole",
    "Mast", "Treasure Chest", "Fossil",
    #Snow Land
    "Penguin Mirror", "Chimney", "Snowman",
    "Snow Globe", "Sleigh", "Star Wreath",
    #Space Land
    "Space Table", "Circuitry Rug", "Space Food",
    "Star Candy", "Porthole", "Saturn Donuts",
    #Dream Land
    "Apple Table", "Pancakes", "Bubbly Soda",
    "Dedede's Robe", "Ice Cream", "Knight Helmet"
]

chestLocations = [
    "Patch Castle 1",

    "Flower Fields 1",
    "Rainbow Falls 1",
    "Big-Bean Vine 1",
    "Mole Hole 1",
    "Weird Woods 1",

    "Pyramid Sands 1",
    "Lava Land 1",
    "Cool Cave 1",
    "Dino Jungle 1",
    "Temper Temple 1",
    "Dusk Dunes 1",

    "Toy Tracks 1",
    "Mushroom Run 1",
    "Sweets Park 1",
    "Melody Town 1",
    "Cocoa Station 1",
    "Dark Manor 1",

    "Splash Beach 1",
    "Blub-Blub Ocean 1",
    "Secret Island 1",
    "Deep-Dive Deep 1",
    "Boom Boatyard 1",
    "Fossil Reef 1",

    "Snowy Fields 1",
    "Cozy Cabin 1",
    "Mt. Slide 1",
    "Frosty Wheel 1",
    "Frigid Fjords 1",
    "Evergreen Lift 1",

    "Future City 1",
    "Tube Town 1",
    "Mysterious UFO 1",
    "Steller Way 1",
    "Moon Base 1",
    "Outer Rings 1",

    "Whispy Forest 1",
    "Tempest Towers 1",
    "Cloud Palace 1",
    "Castle Dedede 1",
    "Meta Melon Isle 1",
    "Battle Ship Halberd 1",
     #Bottom Row
    "Patch Castle 2",

    "Flower Fields 2",
    "Rainbow Falls 2",
    "Big-Bean Vine 2",
    "Mole Hole 2",
    "Weird Woods 2",

    "Pyramid Sands 2",
    "Lava Land 2",
    "Cool Cave 2",
    "Dino Jungle 2",
    "Temper Temple 2",
    "Dusk Dunes 2",

    "Toy Tracks 2",
    "Mushroom Run 2",
    "Sweets Park 2",
    "Melody Town 2",
    "Cocoa Station 2",
    "Dark Manor 2",

    "Splash Beach 2",
    "Blub-Blub Ocean 2",
    "Secret Island 2",
    "Deep-Dive Deep 2",
    "Boom Boatyard 2",
    "Fossil Reef 2",

    "Snowy Fields 2",
    "Cozy Cabin 2",
    "Mt. Slide 2",
    "Frosty Wheel 2",
    "Frigid Fjords 2",
    "Evergreen Lift 2",

    "Future City 2",
    "Tube Town 2",
    "Mysterious UFO 2",
    "Steller Way 2",
    "Moon Base 2",
    "Outer Rings 2",

    "Whispy Forest 2",
    "Tempest Towers 2",
    "Cloud Palace 2",
    "Castle Dedede 2",
    "Meta Melon Isle 2",
    "Battle Ship Halberd 2"

]

unrandom_chestItems = chestItems[:]
unrandom_chestLocations = chestLocations[:]

def setup():
    global isSetup
    if isSetup == 0:
        random.seed(variableManagment.seed)
        random.shuffle(chestItems)
        print(dict(zip(chestLocations, chestItems)))
        isSetup = 1

def item_reset():
    #Top
    loopNum = 0
    while loopNum < 43:
        dme.write_byte(0x906A80EF + (loopNum * 12), 0x00)
        loopNum += 1

    # Bottom row
    loopNum = 0
    while loopNum < 43:
        dme.write_byte(0x906A80EF + (loopNum * 12) + (12 * 125), 0x00)
        loopNum += 1

def chest_check():
    # 43 Normal Levels
    # 7 Bosses
    hops = 0
    offset = 24
    level_offset = 36

    while hops <= 42:
        if dme.read_byte(0x906A7067 + (hops * level_offset) + offset) == 0:
            print("0 0 0")

        elif dme.read_byte(0x906A7067 + (hops * level_offset) + offset) == 1:
            print("1 0 0")
            topRow[hops] = 1

        elif dme.read_byte(0x906A7067 + (hops * level_offset) + offset) == 2:
            print("0 1 0")
            bottomRow[hops] = 1

        elif dme.read_byte(0x906A7067 + (hops * level_offset) + offset) == 3:
            print("1 1 0")
            topRow[hops] = 1
            bottomRow[hops] = 1

        elif dme.read_byte(0x906A7067 + (hops * level_offset) + offset) == 4:
            print("0 0 1")

        elif dme.read_byte(0x906A7067 + (hops * level_offset) + offset) == 5:
            print("1 0 1")
            topRow[hops] = 1

        elif dme.read_byte(0x906A7067 + (hops * level_offset) + offset) == 6:
            print("0 1 1")
            bottomRow[hops] = 1

        elif dme.read_byte(0x906A7067 + (hops * level_offset) + offset) == 7:
            print("1 1 1")
        print(hops)

        hops += 1

def set_top_save(hops):
    pass

def set_bottom_save(hops):
    pass

def item_assign():
    #Top row
    hops = 0
    for item in topRow:
        if item == 1:
            dme.write_byte(0x906A80EF + (hops * 12), 0x01)
        hops += 1

    # Bottom row
    hops = 0
    for item in bottomRow:
        if item == 1:
            dme.write_byte(0x906A80EF + (hops * 12) + (12 * 125), 0x01)
        hops += 1

def test():
    setup()
    item_reset()
    chest_check()
    #item_assign()