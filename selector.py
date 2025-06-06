import random

definiteEnterGames : list = [   "Grand Theft Auto V", "Uncharted 4: A Thief's End", "Mario Kart 8 Deluxe", "The Legend of Zelda: Tears of the Kingdom", 
                                "Baldur's Gate III", "New Super Mario Bros. Wii", "Hollow Knight", "Elden Ring", "The Legend of Zelda: Breath of the Wild", 
                                "Portal 2", "Red Dead Redemption 2", "Fortnite", "Stardew Valley", "Minecraft", "Terraria"  ]

gameCount : int = 48 - len(definiteEnterGames)

games : list = [    "Mario Kart Wii", "Super Mario Galaxy 2", "Warframe", "Roblox", "Final Fantasy VII", "Marvel Rivals", "VALORANT", "Persona 5 Royal", "Pokemon Omega Ruby/ Alpha Sapphire", 
                    "Super Mario Odyssey", "Grand Theft Auto IV", "Garry's Mod", "Sonic Robo Blast 2", "Sonic Generations", "Doctor Robotnik's Ring Racers", "Mother 3", 
                    "Persona 2: Eternal Punishment", "Blood", "Snatcher", "Half-Life", "Monster Hunter: World", "Mario Super Sluggers", "Wii Sports", "Madden NFL 25", "NHL 24", "Wii Fit", 
                    "Resident Evil 4 (Remake)", "Star Wars Jedi: Survivor", "God of War Ragnarok", "Rain World", "Pyschonauts", "Fallout: New Vegas", "Final Fantasy XIV", "Final Fantasy VIII", 
                    "Persona 5", "Lethal Company", "Destiny 2", "Hades", "Cup Head", "Nuclear Throne", "Slay the Spire", "Shovel Knight", "We Need to Go Deeper", "Heavy Bullets", "Halo 2", 
                    "The Legend of Zelda: A Link to the Past", "GoldenEye 007", "Clash Royale"  ]

gamesCopy : list = games[:]

if (len(definiteEnterGames) + len(gamesCopy)) < 48 or gameCount > len(gamesCopy):
    print("Error. Not enough games to fill out tournament.")

print("Number of games that are definitely getting in:", len(definiteEnterGames))
print("Number of games to randomly choose from:", len(gamesCopy)) # shows how many games there are to choose from
print("Number of games that will be randomly chosen:", 48 - len(definiteEnterGames))
print("Result size:", len(definiteEnterGames) + gameCount)
print()
gamesResult : list = [] # where the randomly selected games go
currentItem : str # the current game being chosen

for i in range(gameCount): # loop gameCount number of times
    currentItem = str(random.choice(gamesCopy)) # select a random game
    gamesCopy.remove(currentItem) # remove the game from the games list so it doesn't get chosen twice
    gamesResult.append(currentItem) # put the game in the result list

randomPlusDefiniteGames : list = definiteEnterGames + gamesResult # games that are definitely getting in plus the randomly chosen games. The total result
random.shuffle(randomPlusDefiniteGames)

file = open("output.csv", "wt") # create the spreadsheet

for item in randomPlusDefiniteGames: # put each item in the spreadsheets
    file.write(item)
    file.write(",\n")
file.close()

print("{", end="") # my dictionary shenanigans
for item in randomPlusDefiniteGames:
    print('"' + item + '"', end="")
    print(": None", end="")
    if item != randomPlusDefiniteGames[-1]:
        print(",")
print("}")