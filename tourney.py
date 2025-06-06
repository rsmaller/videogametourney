#!/usr/bin/python3
import os, sys, pathlib, math

tourney_items       : dict = {  "Persona 5 Royal": None,
                                "Doctor Robotnik's Ring Racers": None,
                                "Hollow Knight": None,
                                "New Super Mario Bros. Wii": None,
                                "Mario Kart 8 Deluxe": None,
                                "Hades": None,
                                "Sonic Robo Blast 2": None,
                                "Stardew Valley": None,
                                "Warframe": None,
                                "Star Wars Jedi: Survivor": None,
                                "Nuclear Throne": None,
                                "Fallout: New Vegas": None,
                                "Final Fantasy VIII": None,
                                "Heavy Bullets": None,
                                "Slay the Spire": None,
                                "Minecraft": None,
                                "The Legend of Zelda: Breath of the Wild": None,
                                "Marvel Rivals": None,
                                "Clash Royale": None,
                                "GoldenEye 007": None,
                                "Final Fantasy VII": None,
                                "Fortnite": None,
                                "We Need to Go Deeper": None,
                                "Red Dead Redemption 2": None,
                                "Blood": None,
                                "The Legend of Zelda: A Link to the Past": None,
                                "God of War Ragnarok": None,
                                "The Legend of Zelda: Tears of the Kingdom": None,
                                "Resident Evil 4 (Remake)": None,
                                "Final Fantasy XIV": None,
                                "Elden Ring": None,
                                "Wii Sports": None,
                                "Grand Theft Auto V": None,
                                "Rain World": None,
                                "Pyschonauts": None,
                                "Sonic Generations": None,
                                "Shovel Knight": None,
                                "Monster Hunter: World": None,
                                "Terraria": None,
                                "Cuphead": None,
                                "Halo 2": None,
                                "Mother 3": None,
                                "Uncharted 4: A Thief's End": None,
                                "Baldur's Gate III": None,
                                "Roblox": None,
                                "Mario Kart Wii": None,
                                "Portal 2": None,
                                "Half-Life": None   }

tourney_item_list   : list = list(tourney_items.keys())

scorers             : list = [  "Ryan", "Anthony", "Brandon", 
                                "Qwaelan", "Brian", "Kyle", "Brendan", "Jaylen", 
                                "Andy", "Jason"]

score_items         : list = [  "Gameplay", "Visuals or Art Style", "Music" ]

min_score                       : int = 1
max_score                       : int = 5
score_inputs_per_tourney_item   : int = len(scorers) * len(score_items)
number_of_scores                : int = len(tourney_item_list) * score_inputs_per_tourney_item

scores_file_path    : str = "./scores.csv"
scores_file_exists  : bool = pathlib.Path(scores_file_path).exists()

seconds_per_score   : int = 3

number_of_divisions = 4
items_per_division = math.ceil(len(tourney_item_list) / number_of_divisions)

def getScores(key_to_start : str, file_to_write):
    global tourney_items
    global scorers
    global score_items
    global min_score
    global max_score
    global tourney_item_list
    global number_of_scores
    global number_of_divisions
    global items_per_division

    current_score_input : str = ""
    exitPromptValue     : str = ""
    total_score_to_add  : int = 0
    index               : int = tourney_item_list.index(key_to_start)

    if scores_file_exists:
        index += 1

    current_sequence_item : int = index * len(scorers) * len(score_items)
    current_item          : int = index

    current_scorer_index : int = 1

    for tourney_item in tourney_item_list[index:]:
        for scorer in scorers:
            for score_item in score_items:
                current_score_int : int = max_score + 1 # mimic do while loop
                while (current_score_int < min_score or current_score_int > max_score):
                    print(f"-[Division {current_item // (items_per_division) + 1}]- Current Game: {tourney_item} ({current_item + 1} out of {len(tourney_item_list)})")
                    print(f"Scorer: {scorer} ({current_scorer_index} / {len(scorers)})")
                    current_score_input = input(f"\t[{round((seconds_per_score * (number_of_scores - current_sequence_item)) / 3600, 2)} hours left] - ({current_sequence_item + 1} / {number_of_scores}) Input score for {score_item} ({min_score}-{max_score}): ")
                    if current_score_input == "q":
                        if scorer != scorers[0] or score_item != score_items[0]:
                            while (exitPromptValue  != "y" and exitPromptValue != "n"):
                                exitPromptValue = input("A game is in the middle of being scored. Are you sure you want to exit? Scores for the current game will be voided. (y/n): ").rstrip().lower()
                                if (exitPromptValue == "y"):
                                    return
                                else:
                                    os.system("clear")
                                    exitPromptValue = ""
                                    break
                        else:
                            return
                    if not current_score_input.isdigit():
                        os.system("clear")
                        continue
                    current_sequence_item += 1
                    current_score_int = int(current_score_input)
                    os.system("clear")
                total_score_to_add += current_score_int
            current_scorer_index += 1
        current_item += 1
        tourney_items[tourney_item] = round(total_score_to_add / (len(scorers)))
        file_to_write.write(f"{tourney_item},{tourney_items[tourney_item]}\n")
        file_to_write.flush()
        total_score_to_add = 0
        current_scorer_index = 1
    file_to_write.close()

def fetchPreviouslyScoredItem(file_path) -> str:
    global tourney_items
    global scores_file_exists
    global tourney_item_list
    item    : str = ""
    score   : str = ""
    for line in open(file_path):
        try:
            item, score = line.split(',')
        except:
            print("This CSV file is not in the correct format to continue from. Please fix the CSV or generate a new one.")
            quit()
    if item == "" or score == "":
        scores_file_exists = False
        return tourney_item_list[0]
    return item

def main():
    global tourney_item_list
    global scores_file_exists
    global scores_file_path
    global score_inputs_per_tourney_item
    global seconds_per_score
    starting_key : str = tourney_item_list[0]
    scores_file_writer = open(scores_file_path, "at")
    if (scores_file_exists):
        scores_file_full_string = open(scores_file_path).read() # store this for later use. scores file reader data gets consumed as it's read.
        starting_key = fetchPreviouslyScoredItem(scores_file_path)
        if starting_key == tourney_item_list[-1]:
            print("CSV already complete. Exiting.")
            quit()
        if len(scores_file_full_string) != 0 and scores_file_full_string[-1] != "\n":
            scores_file_writer.write("\n")
            print("Adding newline to end of file.")
        if (scores_file_exists):
            print(f"Scores file already exists. Continuing from item after {starting_key}.")
        else:
            print(f"Scores file exists but is empty. Starting from beginning.")
        print()

    print(f"There are {score_inputs_per_tourney_item} scores per game in this tournament, and there are currently {len(tourney_item_list)} games implemented.")
    print(f"Furthermore, there are {len(scorers)} participants in the game currently.")
    print(f"They will provide {len(score_items)} scores between {min_score} and {max_score} for each game.")
    print(f"If each participant averages around {seconds_per_score} seconds for each score, the tournament should be finished in about {round((seconds_per_score * number_of_scores) / 3600, 2)} hours.\n")
    getScores(starting_key, scores_file_writer)
    for item in tourney_item_list[tourney_item_list.index(starting_key):]:
        print(f"\nItem: {item}, Score: {tourney_items[item]}")

main()