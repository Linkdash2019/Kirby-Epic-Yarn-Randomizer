#Items
nothingItem = ['Nothing']

doorItems = [
    'Patch Castle', #Quilty Square
    'Fountain Gardens', 'Flower Fields',   'Rainbow Falls',  'Big-Bean Vine ', 'Mole Hole',       'Weird Woods',   #Grass Land
    'Pyramid Sands',    'Lava Landing',    'Cool Cave',      'Dino Jungle',    'Temper Temple',   'Dusk Dunes',    #Hot Land
    'Toy Tracks',       'Mushroom Run',    'Sweets Park',    'Melody Town',    'Cocoa Station',   'Dark Manor',    #Treat Land
    'Splash Beach',     'Blub-Blub Ocean', 'Secret Island',  'Deep-Dive Deep', 'Boom Boatyard',   'Fossil Reef',   #Water Land
    'Snowy Fields',     'Cozy Cabin',      'Mt. Slide',      'Frosty Wheel',   'Frigid Fjords',   'Evergreen Lift',#Snow Land
    'Future City',      'Tube Town',       'Mysterious UFO', 'Stellar Way',    'Moon Base',       'Outer Rings',   #Space Land
    "Whispy's Forest",  'Tempest Towers',  'Cloud Palace',   'Castle Dedede' , 'Meta Melon Isle', 'Battleship Halberd',#Dream Land
    'Fangora', 'Hot Wings', 'Squashini', 'Capamari', 'King Dedede', 'Meta Knight', 'Yin-Yarn' #Bosses
]

chestItems = [
    #Quilty Square
    "Chandelier","King's Throne","Patch Castle Soundtrack",
    #Grass Land
    "Flower Sofa", "Fountain", "Fountain Gardens Soundtrack",
    "Flower Clock", "Frog Umbrella Stand", "Flower Fields Soundtrack",
    "Rainbow Arch", "Outdoor Bath", "Rainbow Falls Soundtrack",
    "Lattice", "Cloud Pillow", "Big-Bean Vine Soundtrack",
    "Carrot Dresser", "Tree-Stump Bed", "Mole Hole Soundtrack",
    "Telescope", "Log Cake", "Weird Woods Soundtrack",
    #Hot Land
    "Camel Sofa", "Cactus Juice", "Pyramid Sands Soundtrack",
    "Stone Lamp", "Cartoon Meat", "Lava Landing Soundtrack",
    "Crystal", "Frog Mirror", "Cool Cave Soundtrack",
    "Bronto Slide", "Torch", "Dino Jungle Soundtrack",
    "Pyramid", "Camel Pillow", "Quilty Square Soundtrack",
    "Magic Carpet", "Hourglass", "Dusk Dunes Soundtrack",
    #Treat Land
    "Stuffed Bear", "Tin Robot", "Toy Tracks Soundtrack",
    "Mushroom Bed", "Mushroom Lamp", "Mushroom Run Soundtrack",
    "Donut Pillow", "Dessert Dresser", "Grass Land Soundtrack",
    "Toy Piano", "Clef Tree", "Melody Town Soundtrack",
    "Choco Ottoman", "Chocolate Bar", "Hot Land Soundtrack",
    "Ghost-in-a-Box", "Pumpkin", "Dark Manor Soundtrack",
    #Water Land
    "Sun Clock", "Moon Clock", "Secret Island Soundtrack",
    "Jellyfish Light", "Aquarium", "Blub-Blub Ocean Soundtrack",
    "Treasure Rug", "Totem Pole", "Splash Beach Soundtrack",
    "Dangler Light", "Mast", "Deep-Dive Deep Soundtrack",
    "Pirate Ship", "Treasure Chest", "Treat Land Soundtrack",
    "Anemone Sofa", "Fossil", "Water Land Soundtrack",
    #Snow Land
    "Big Bear Bed", "Penguin Mirror", "Snowy Fields Soundtrack",
    "Fireplace", "Chimney", "Cozy Cabin Soundtrack",
    "Knit-Cap Sofa", "Snowman", "Mt. Slide Soundtrack",
    "Snow Clock", "Snow Globe", "Frosty Wheel Soundtrack",
    "Penguin Chest", "Sleigh", "Snow Land Soundtrack",
    "Holiday Tree", "Star Wreath", "Quilty Court Soundtrack",
    #Space Land
    "Space Monitor", "Space Table", "Future City Soundtrack",
    "Digital Clock", "Circuitry Rug", "Tube Town Soundtrack",
    "Communicator", "Space Food", "Space Land Soundtrack",
    "Robot Bed", "Star Candy", "Stellar Way Soundtrack",
    "Cosmic Bin", "Porthole", "Tankbot Soundtrack",
    "Saturn Stand", "Saturn Donuts", "Outer Rings Soundtrack",
    #Dream Land
    "Whispy Woods", "Apple Table", "Green Greens Soundtrack",
    "Bookcase", "Pancakes", "Butter Building Soundtrack",
    "Cloud Rug", "Bubbly Soda", "Bubbly Clouds Soundtrack",
    "Castle Dedede", "Dedede's Robe", "Gourment Race Soundtrack",
    "Palm Chair", "Ice Cream", "Ice Cream Island Soundtrack",
    "Galaxia Sword", "Knight Helmet", "Halberd Soundtrack",
    #Bosses
    "Fangora Soundtrack", "Hot Wings Soundtrack", "Squashini Soundtrack",
    "Capamari Soundtrack", "King Dedede Soundtrack", "Meta Knight Soundtrack"#,
    #"Yin-Yarn Soundtrack", "Dream Land Soundtrack", "Staff Credits Soundtrack"
]

#Locations
startLocation = {'Start':[]}

doorLocations = {
    'Patch Castle Goal':['Patch Castle'],

    'Fountain Gardens Goal':['Fountain Gardens'], 'Flower Fields Goal':['Flower Fields'], 'Rainbow Falls Goal':['Rainbow Falls'], 
    'Big-Bean Vine Goal':['Big-Bean Vine'], 'Mole Hole Goal':['Mole Hole'], 'Weird Woods Goal':['Weird Woods'],

    'Pyramid Sands Goal':['Pyramid Sands'], 'Lava Landing Goal':['Lava Landing'], 'Cool Cave Goal':['Cool Cave'], 
    'Dino Jungle Goal':['Dino Jungle'], 'Temper Temple Goal':['Temper Temple'], 'Dusk Dunes Goal':['Dusk Dunes'],

    'Toy Tracks Goal':['Toy Tracks'], 'Mushroom Run Goal':['Mushroom Run'], 'Sweets Park Goal':['Sweets Park'], 
    'Melody Town Goal':['Melody Town'], 'Cocoa Station Goal':['Cocoa Station'], 'Dark Manor Goal':['Dark Manor'],

    'Splash Beach Goal':['Splash Beach'], 'Blub-Blub Ocean Goal':['Blub-Blub Ocean'], 'Secret Island Goal':['Secret Island'], 
    'Deep-Dive Deep Goal':['Deep-Dive Deep'], 'Boom Boatyard Goal':['Boom Boatyard'], 'Fossil Reef Goal':['Fossil Reef'],

    'Snowy Fields Goal':['Snowy Fields'], 'Cozy Cabin Goal':['Cozy Cabin'], 'Mt. Slide Goal':['Mt. Slide'], 
    'Frosty Wheel Goal':['Frosty Wheel'], 'Frigid Fjords Goal':['Frigid Fjords'], 'Evergreen Lift Goal':['Evergreen Lift'],

    'Future City Goal':['Future City'], 'Tube Town Goal':['Tube Town'], 'Mysterious UFO Goal':['Mysterious UFO'], 
    'Stellar Way Goal':['Stellar Way'], 'Moon Base Goal':['Moon Base'], 'Outer Rings Goal':['Outer Rings'],

    "Whispy's Forest Goal":["Whispy's Forest"], 'Tempest Towers Goal':['Tempest Towers'], 'Cloud Palace Goal':['Cloud Palace'], 
    'Castle Dedede Goal':['Castle Dedede'], 'Meta Melon Isle Goal':['Meta Melon Isle'], 'Battleship Halberd Goal':['Battleship Halberd'],

    'Fangora Goal':['Fangora'], 'Hot Wings Goal':['Hot Wings'], 'Squashini Goal':['Squashini'], 
    'Capamari Goal':['Capamari'], 'King Dedede Goal':['King Dedede'], 'Meta Knight Goal':['Meta Knight']
}

chestLocations = {
    'Patch Castle 1':['Patch Castle'], 'Patch Castle 2':['Patch Castle'], 'Patch Castle 3':['Patch Castle'],

    'Fountain Gardens 1':['Fountain Gardens'], 'Fountain Gardens 2':['Fountain Gardens'], 'Fountain Gardens 3':['Fountain Gardens'],
    'Flower Fields 1':['Flower Fields'], 'Flower Fields 2':['Flower Fields'], 'Flower Fields 3':['Flower Fields'],
    'Rainbow Falls 1':['Rainbow Falls'], 'Rainbow Falls 2':['Rainbow Falls'], 'Rainbow Falls 3':['Rainbow Falls'],
    'Big-Bean Vine 1':['Big-Bean Vine'], 'Big-Bean Vine 2':['Big-Bean Vine'], 'Big-Bean Vine 3':['Big-Bean Vine'],
    'Mole Hole 1':['Mole Hole'], 'Mole Hole 2':['Mole Hole'], 'Mole Hole 3':['Mole Hole'],
    'Weird Woods 1':['Weird Woods'], 'Weird Woods 2':['Weird Woods'], 'Weird Woods 3':['Weird Woods'],

    'Pyramid Sands 1':['Pyramid Sands'], 'Pyramid Sands 2':['Pyramid Sands'], 'Pyramid Sands 3':['Pyramid Sands'],
    'Lava Land 1':['Lava Land'], 'Lava Land 2':['Lava Land'], 'Lava Land 3':['Lava Land'],
    'Cool Cave 1':['Cool Cave'], 'Cool Cave 2':['Cool Cave'], 'Cool Cave 3':['Cool Cave'],
    'Dino Jungle 1':['Dino Jungle'], 'Dino Jungle 2':['Dino Jungle'], 'Dino Jungle 3':['Dino Jungle'],
    'Temper Temple 1':['Temper Temple'], 'Temper Temple 2':['Temper Temple'], 'Temper Temple 3':['Temper Temple'],
    'Dusk Dunes 1':['Dusk Dunes'], 'Dusk Dunes 2':['Dusk Dunes'], 'Dusk Dunes 3':['Dusk Dunes'],

    'Toy Tracks 1':['Toy Tracks'], 'Toy Tracks 2':['Toy Tracks'], 'Toy Tracks 3':['Toy Tracks'],
    'Mushroom Run 1':['Mushroom Run'], 'Mushroom Run 2':['Mushroom Run'], 'Mushroom Run 3':['Mushroom Run'],
    'Sweets Park 1':['Sweets Park'], 'Sweets Park 2':['Sweets Park'], 'Sweets Park 3':['Sweets Park'],
    'Melody Town 1':['Melody Town'], 'Melody Town 2':['Melody Town'], 'Melody Town 3':['Melody Town'],
    'Cocoa Station 1':['Cocoa Station'], 'Cocoa Station 2':['Cocoa Station'], 'Cocoa Station 3':['Cocoa Station'],
    'Dark Manor 1':['Dark Manor'], 'Dark Manor 2':['Dark Manor'], 'Dark Manor 3':['Dark Manor'],

    'Splash Beach 1':['Splash Beach'], 'Splash Beach 2':['Splash Beach'], 'Splash Beach 3':['Splash Beach'],
    'Blub-Blub Ocean 1':['Blub-Blub Ocean'], 'Blub-Blub Ocean 2':['Blub-Blub Ocean'], 'Blub-Blub Ocean 3':['Blub-Blub Ocean'],
    'Secret Island 1':['Secret Island'], 'Secret Island 2':['Secret Island'], 'Secret Island 3':['Secret Island'],
    'Deep-Dive Deep 1':['Deep-Dive Deep'], 'Deep-Dive Deep 2':['Deep-Dive Deep'], 'Deep-Dive Deep 3':['Deep-Dive Deep'],
    'Boom Boatyard 1':['Boom Boatyard'], 'Boom Boatyard 2':['Boom Boatyard'], 'Boom Boatyard 3':['Boom Boatyard'],
    'Fossil Reef 1':['Fossil Reef'], 'Fossil Reef 2':['Fossil Reef'], 'Fossil Reef 3':['Fossil Reef'],

    'Snowy Fields 1':['Snowy Fields'], 'Snowy Fields 2':['Snowy Fields'], 'Snowy Fields 3':['Snowy Fields'],
    'Cozy Cabin 1':['Cozy Cabin'], 'Cozy Cabin 2':['Cozy Cabin'], 'Cozy Cabin 3':['Cozy Cabin'],
    'Mt. Slide 1':['Mt. Slide'], 'Mt. Slide 2':['Mt. Slide'], 'Mt. Slide 3':['Mt. Slide'],
    'Frosty Wheel 1':['Frosty Wheel'], 'Frosty Wheel 2':['Frosty Wheel'], 'Frosty Wheel 3':['Frosty Wheel'],
    'Frigid Fjords 1':['Frigid Fjords'], 'Frigid Fjords 2':['Frigid Fjords'], 'Frigid Fjords 3':['Frigid Fjords'],
    'Evergreen Lift 1':['Evergreen Lift'], 'Evergreen Lift 2':['Evergreen Lift'], 'Evergreen Lift 3':['Evergreen Lift'],

    'Future City 1':['Future City'], 'Future City 2':['Future City'], 'Future City 3':['Future City'],
    'Tube Town 1':['Tube Town'], 'Tube Town 2':['Tube Town'], 'Tube Town 3':['Tube Town'],
    'Mysterious UFO 1':['Mysterious UFO'], 'Mysterious UFO 2':['Mysterious UFO'], 'Mysterious UFO 3':['Mysterious UFO'],
    'Steller Way 1':['Steller Way'], 'Steller Way 2':['Steller Way'], 'Steller Way 3':['Steller Way'],
    'Moon Base 1':['Moon Base'], 'Moon Base 2':['Moon Base'], 'Moon Base 3':['Moon Base'],
    'Outer Rings 1':['Outer Rings'], 'Outer Rings 2':['Outer Rings'], 'Outer Rings 3':['Outer Rings'],

    'Whispy Forest 1':['Whispy Forest'], 'Whispy Forest 2':['Whispy Forest'], 'Whispy Forest 3':['Whispy Forest'],
    'Tempest Towers 1':['Tempest Towers'], 'Tempest Towers 2':['Tempest Towers'], 'Tempest Towers 3':['Tempest Towers'],
    'Cloud Palace 1':['Cloud Palace'], 'Cloud Palace 2':['Cloud Palace'], 'Cloud Palace 3':['Cloud Palace'],
    'Castle Dedede 1':['Castle Dedede'], 'Castle Dedede 2':['Castle Dedede'], 'Castle Dedede 3':['Castle Dedede'],
    'Meta Melon Isle 1':['Meta Melon Isle'], 'Meta Melon Isle 2':['Meta Melon Isle'], 'Meta Melon Isle 3':['Meta Melon Isle'],
    'Battle Ship Halberd 1':['Battle Ship Halberd'], 'Battle Ship Halberd 2':['Battle Ship Halberd'], 'Battle Ship Halberd 3':['Battle Ship Halberd'],

    'Fangora Disk':['Fangora'], 'Hot Wings Disk':['Hot Wings'], 'Squashini Disk':['Squashini'],
    'Capamari Disk':['Capamari'], 'King Dedede Disk':['King Dedede'], 'Meta Knight Disk':['Meta Knight']#,
    #'Yin-Yarn Disk 1':['Yin-Yarn'], Yin-Yarn Disk 2':['Yin-Yarn'], Yin-Yarn Disk 3':['Yin-Yarn'],

}

items = []

unrandom_items = items[:]
locations = {}

#Correct Disk Order
diskOrder = [
    'Quilty Square Soundtrack', 'Grass Land Soundtrack', 'Hot Land Soundtrack', 'Treat Land Soundtrack', 'Water Land Soundtrack', 'Snow Land Soundtrack', 'Space Land Soundtrack', 'Dream Land Soundtrack',
    'Quilty Court Soundtrack', 'Patch Castle Soundtrack', 
    'Fountain Gardens Soundtrack', 'Flower Fields Soundtrack', 'Rainbow Falls Soundtrack', 'Big-Bean Vine Soundtrack', 'Mole Hole Soundtrack', 'Weird Woods Soundtrack',
    'Pyramid Sands Soundtrack', 'Lava Landing Soundtrack', 'Cool Cave Soundtrack', 'Dino Jungle Soundtrack', 'Dusk Dunes Soundtrack',
    'Toy Tracks Soundtrack', 'Mushroom Run Soundtrack', 'Melody Town Soundtrack', 'Dark Manor Soundtrack', 
    'Splash Beach Soundtrack', 'Secret Island Soundtrack', 'Blub-Blub Ocean Soundtrack', 'Deep-Dive Deep Soundtrack',
    'Snowy Fields Soundtrack', 'Cozy Cabin Soundtrack', 'Mt. Slide Soundtrack', 'Frosty Wheel Soundtrack',
    'Future City Soundtrack', 'Tube Town Soundtrack', 'Stellar Way Soundtrack', 'Tankbot Soundtrack', 'Outer Rings Soundtrack',
    'Green Greens', 'Butter Building', 'Bubbly Clouds', 'Gourment Race', 'Ice Cream Island', 'Halberd',
    'Fangora Soundtrack', 'Hot Wings Soundtrack', 'Squashini Soundtrack', 'Capamari Soundtrack', 'King Dedede Soundtrack', 'Meta Knight Soundtrack', 'Yin-Yarn Soundtrack',
    'Staff Credits Soundtrack'
]
#Other Variables
seed = "0"
spoiler = {}

shuffleDoors = True
shuffleChests = True

pcUnlock = False
boss1Unlock = False
boss2Unlock = False
boss3Unlock = False
boss4Unlock = False
boss5Unlock = False
boss6Unlock = False
isBeaten = False